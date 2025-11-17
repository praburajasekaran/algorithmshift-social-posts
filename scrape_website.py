#!/usr/bin/env python3
"""
Website Scraper for AlgorithmShift.ai
Scrapes entire website content including text, images, and linked pages.
"""

import os
import re
import time
import json
import requests
from urllib.parse import urljoin, urlparse, urlunparse
from bs4 import BeautifulSoup
from pathlib import Path
from typing import Set, List, Dict, Optional
import argparse
from datetime import datetime


class WebsiteScraper:
    def __init__(self, base_url: str, output_dir: str = "scraped_content", delay: float = 1.0, 
                 titles_only: bool = False, path_prefix: Optional[str] = None):
        """
        Initialize the website scraper.
        
        Args:
            base_url: The base URL of the website to scrape
            output_dir: Directory to save scraped content
            delay: Delay between requests in seconds (to be respectful)
            titles_only: If True, only extract page titles (for marketing ideas)
            path_prefix: Only scrape URLs that start with this path (e.g., '/docs')
        """
        self.base_url = base_url.rstrip('/')
        self.domain = urlparse(base_url).netloc
        self.output_dir = Path(output_dir)
        self.delay = delay
        self.titles_only = titles_only
        self.path_prefix = path_prefix
        
        # Create output directories
        self.output_dir.mkdir(exist_ok=True)
        (self.output_dir / "markdown").mkdir(exist_ok=True)
        
        # Track visited URLs and content
        self.visited_urls: Set[str] = set()
        self.to_visit: List[str] = [base_url]
        self.scraped_data: Dict[str, Dict] = {}
        # Track URL to filename mapping to avoid duplicates
        self.url_to_filename: Dict[str, str] = {}
        
        # Session for connection pooling
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
    
    def is_valid_url(self, url: str) -> bool:
        """Check if URL belongs to the same domain and is valid."""
        parsed = urlparse(url)
        
        # Skip non-HTTP(S) protocols
        if parsed.scheme not in ('http', 'https', ''):
            return False
        
        # Skip mailto, tel, javascript, etc.
        if parsed.scheme in ('mailto', 'tel', 'javascript', 'data'):
            return False
        
        # Normalize URL
        if not parsed.scheme:
            url = urljoin(self.base_url, url)
            parsed = urlparse(url)
        
        # Only scrape same domain
        if parsed.netloc and parsed.netloc != self.domain:
            return False
        
        # If path_prefix is set and titles_only is enabled, allow following links outside prefix
        # (so we can scrape non-docs URLs with full content while docs get titles-only)
        # Otherwise, if path_prefix is set, only scrape URLs with that prefix
        if self.path_prefix:
            path = parsed.path
            if not path.startswith(self.path_prefix):
                # If titles_only is enabled, allow following links outside prefix
                # This enables scraping non-docs URLs with full content
                if not self.titles_only:
                    return False
                # If titles_only is enabled, we still want to follow these links
                # but they'll get full content scraping
        
        # Skip anchors and fragments
        url_without_fragment = urlunparse(parsed._replace(fragment=''))
        
        # Skip common file extensions we don't want to scrape
        skip_extensions = {'.pdf', '.zip', '.exe', '.dmg', '.jpg', '.jpeg', '.png', 
                          '.gif', '.svg', '.ico', '.css', '.js', '.woff', '.woff2', '.ttf'}
        path_lower = parsed.path.lower()
        if any(path_lower.endswith(ext) for ext in skip_extensions):
            return False
        
        return True
    
    def normalize_url(self, url: str) -> str:
        """Normalize URL by removing fragments and trailing slashes."""
        parsed = urlparse(url)
        
        # Add scheme if missing
        if not parsed.scheme:
            url = urljoin(self.base_url, url)
            parsed = urlparse(url)
        
        # Remove fragment
        normalized = urlunparse(parsed._replace(fragment=''))
        
        # Remove trailing slash (except for root)
        if normalized.endswith('/') and len(parsed.path) > 1:
            normalized = normalized.rstrip('/')
        
        return normalized
    
    def extract_links(self, soup: BeautifulSoup, current_url: str) -> List[str]:
        """Extract all internal links from a page."""
        links = []
        
        for tag in soup.find_all(['a', 'link'], href=True):
            href = tag['href']
            full_url = urljoin(current_url, href)
            
            if self.is_valid_url(full_url):
                normalized = self.normalize_url(full_url)
                if normalized not in self.visited_urls:
                    links.append(normalized)
        
        return links
    
    def extract_images(self, soup: BeautifulSoup, page_url: str) -> List[Dict]:
        """Extract image references from a page (without downloading)."""
        images = []
        
        for img in soup.find_all('img', src=True):
            img_url = urljoin(page_url, img['src'])
            
            # Just collect image info, don't download
            images.append({
                'url': img_url,
                'alt': img.get('alt', ''),
                'title': img.get('title', '')
            })
        
        return images
    
    def clean_text(self, soup: BeautifulSoup) -> str:
        """Extract and clean text content from HTML."""
        # Remove script and style elements
        for script in soup(["script", "style", "meta", "link", "noscript"]):
            script.decompose()
        
        # Get text
        text = soup.get_text()
        
        # Clean up whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return text
    
    def html_to_markdown(self, soup: BeautifulSoup, url: str, images: List[Dict]) -> str:
        """Convert HTML content to Markdown format."""
        # Create a working copy
        md_soup = BeautifulSoup(str(soup), 'html.parser')
        
        # Remove unwanted elements
        for element in md_soup(["script", "style", "meta", "link", "noscript", "nav", "footer", "header"]):
            element.decompose()
        
        # Convert headings
        for i in range(1, 7):
            for heading in md_soup.find_all(f'h{i}'):
                text = heading.get_text().strip()
                if text:
                    heading.replace_with(f"\n{'#' * i} {text}\n")
        
        # Convert paragraphs
        for p in md_soup.find_all('p'):
            text = p.get_text().strip()
            if text:
                p.replace_with(f"\n{text}\n")
        
        # Convert links
        for a in md_soup.find_all('a', href=True):
            link_text = a.get_text().strip()
            href = a.get('href', '')
            if link_text and href:
                # Convert relative URLs to absolute
                if not href.startswith('http'):
                    href = urljoin(url, href)
                a.replace_with(f"[{link_text}]({href})")
        
        # Convert lists
        for ul in md_soup.find_all(['ul', 'ol']):
            items = []
            for li in ul.find_all('li', recursive=False):
                item_text = li.get_text().strip()
                if item_text:
                    prefix = "- " if ul.name == 'ul' else "1. "
                    items.append(f"{prefix}{item_text}")
            if items:
                ul.replace_with("\n" + "\n".join(items) + "\n")
        
        # Convert images (just reference URLs, don't download)
        for img in md_soup.find_all('img', src=True):
            img_src = img.get('src', '')
            alt_text = img.get('alt', '') or img.get('title', '') or 'Image'
            full_url = urljoin(url, img_src)
            img.replace_with(f"\n![{alt_text}]({full_url})\n")
        
        # Convert strong/bold
        for strong in md_soup.find_all(['strong', 'b']):
            text = strong.get_text().strip()
            if text:
                strong.replace_with(f"**{text}**")
        
        # Convert emphasis/italic
        for em in md_soup.find_all(['em', 'i']):
            text = em.get_text().strip()
            if text:
                em.replace_with(f"*{text}*")
        
        # Convert code blocks
        for pre in md_soup.find_all('pre'):
            code = pre.get_text()
            pre.replace_with(f"\n```\n{code}\n```\n")
        
        # Convert inline code
        for code in md_soup.find_all('code'):
            text = code.get_text().strip()
            if text and code.parent.name != 'pre':
                code.replace_with(f"`{text}`")
        
        # Convert blockquotes
        for blockquote in md_soup.find_all('blockquote'):
            text = blockquote.get_text().strip()
            if text:
                lines = text.split('\n')
                quoted = '\n'.join(f"> {line}" for line in lines)
                blockquote.replace_with(f"\n{quoted}\n")
        
        # Get the final text
        markdown = md_soup.get_text()
        
        # Clean up excessive newlines
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)
        
        return markdown.strip()
    
    def scrape_page(self, url: str) -> Dict:
        """Scrape a single page and return its content."""
        print(f"📄 Scraping: {url}")
        
        try:
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            
            # Check if it's HTML
            content_type = response.headers.get('Content-Type', '')
            if 'text/html' not in content_type:
                print(f"  ⏭️  Skipping non-HTML content: {content_type}")
                return None
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract content
            title = soup.find('title')
            title_text = title.get_text().strip() if title else "No Title"
            
            # Extract meta description
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            description = meta_desc.get('content', '') if meta_desc else ''
            
            # Extract links for crawling
            links = self.extract_links(soup, url)
            
            # Determine if this is a /docs URL - apply titles-only mode conditionally
            parsed_url = urlparse(url)
            is_docs_url = parsed_url.path.startswith('/docs')
            
            # If this is a /docs URL and titles_only mode is enabled, return title-only data
            # OR if global titles_only flag is set (for backward compatibility)
            if (is_docs_url and self.titles_only) or (self.titles_only and not self.path_prefix):
                page_data = {
                    'url': url,
                    'title': title_text,
                    'description': description,
                    'links_found': links,
                    'scraped_at': datetime.now().isoformat()
                }
                print(f"  ✅ Title: {title_text}")
                return page_data
            
            # For non-docs URLs (or when titles_only is False), extract full content
            # Extract main content
            main_content = soup.find('main') or soup.find('article') or soup.find('body')
            if main_content:
                main_html = str(main_content)
                main_text = self.clean_text(BeautifulSoup(main_html, 'html.parser'))
            else:
                main_html = str(soup.find('body') or '')
                main_text = self.clean_text(soup)
            
            # Extract all text
            full_text = self.clean_text(soup)
            
            # Extract images
            images = self.extract_images(soup, url)
            
            # Check if we've already assigned a filename for this URL
            if url in self.url_to_filename:
                safe_filename = self.url_to_filename[url]
            else:
                # Generate safe filename from title and URL
                # Use title for filename, fallback to URL path
                if title_text and title_text != "No Title":
                    # Create filename from title
                    safe_title = re.sub(r'[^\w\s\-_]', '', title_text)
                    safe_title = re.sub(r'\s+', '-', safe_title)
                    safe_title = safe_title.lower()[:100]  # Limit length
                    safe_filename = safe_title or 'page'
                else:
                    # Fallback to URL path
                    safe_filename = re.sub(r'[^\w\-_\.]', '_', parsed_url.path) or 'index'
                    if safe_filename.endswith('_'):
                        safe_filename += 'index'
                
                # Ensure unique filename by adding counter if needed
                # Check both existing files and already-assigned filenames
                base_filename = safe_filename
                counter = 1
                while (self.output_dir / "markdown" / f"{safe_filename}.md").exists() or safe_filename in self.url_to_filename.values():
                    safe_filename = f"{base_filename}-{counter}"
                    counter += 1
                
                # Store the mapping
                self.url_to_filename[url] = safe_filename
            
            # Convert to Markdown and save as separate file
            markdown_content = self.html_to_markdown(soup, url, images)
            markdown_file = self.output_dir / "markdown" / f"{safe_filename}.md"
            
            # Create markdown with metadata
            desc_section = f'**Description:** {description}\n\n' if description else ''
            separator = '---\n\n' if description else ''
            markdown_with_meta = f"""# {title_text}

**URL:** {url}  
**Scraped:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

{desc_section}{separator}{markdown_content}
"""
            markdown_file.write_text(markdown_with_meta, encoding='utf-8')
            
            page_data = {
                'url': url,
                'title': title_text,
                'description': description,
                'text': full_text,
                'main_text': main_text,
                'markdown_file': str(markdown_file.relative_to(self.output_dir)),
                'markdown_content': markdown_content,
                'images': images,
                'links_found': links,
                'scraped_at': datetime.now().isoformat()
            }
            
            print(f"  ✅ Scraped: {title_text}")
            print(f"     📄 Saved to: {markdown_file.name} ({len(full_text)} chars, {len(images)} image refs, {len(links)} links)")
            
            return page_data
            
        except requests.exceptions.RequestException as e:
            print(f"  ❌ Error fetching {url}: {e}")
            return None
        except Exception as e:
            print(f"  ❌ Error processing {url}: {e}")
            return None
    
    def scrape(self, max_pages: int = None):
        """Scrape the entire website."""
        if self.titles_only and self.path_prefix:
            mode_text = f"titles only for {self.path_prefix}, full content for others"
        elif self.titles_only:
            mode_text = "titles only (all pages)"
        else:
            mode_text = "full content (all pages)"
        path_text = f" (path filter: {self.path_prefix})" if self.path_prefix else ""
        print(f"🚀 Starting scrape of {self.base_url}")
        print(f"📁 Output directory: {self.output_dir}")
        print(f"📋 Mode: {mode_text}{path_text}")
        print(f"⏱️  Delay between requests: {self.delay}s\n")
        
        page_count = 0
        
        while self.to_visit:
            if max_pages and page_count >= max_pages:
                print(f"\n⏹️  Reached maximum page limit ({max_pages})")
                break
            
            url = self.to_visit.pop(0)
            
            # Skip if already visited
            if url in self.visited_urls:
                continue
            
            self.visited_urls.add(url)
            
            # Scrape the page
            page_data = self.scrape_page(url)
            
            if page_data:
                self.scraped_data[url] = page_data
                page_count += 1
                
                # Add new links to visit queue
                if 'links_found' in page_data:
                    for link in page_data['links_found']:
                        if link not in self.visited_urls and link not in self.to_visit:
                            self.to_visit.append(link)
            
            # Be respectful - delay between requests
            if self.to_visit:
                time.sleep(self.delay)
        
        # Save summary
        self.save_summary()
        
        print(f"\n✅ Scraping complete!")
        print(f"   Pages scraped: {page_count}")
        print(f"   Total URLs visited: {len(self.visited_urls)}")
        print(f"   Data saved to: {self.output_dir}")
    
    def save_summary(self):
        """Save a summary JSON file with all scraped data."""
        summary = {
            'base_url': self.base_url,
            'scraped_at': datetime.now().isoformat(),
            'total_pages': len(self.scraped_data),
            'pages': {}
        }
        
        # Separate pages with full content from titles-only pages
        full_content_pages = {}
        titles_only_pages = {}
        
        for url, data in self.scraped_data.items():
            # Check if page has full content (has 'text' or 'markdown_content' key)
            has_full_content = 'text' in data or 'markdown_content' in data
            
            if has_full_content:
                full_content_pages[url] = data
                summary['pages'][url] = {
                    'title': data['title'],
                    'description': data.get('description', ''),
                    'text_length': len(data.get('text', '')),
                    'image_count': len(data.get('images', [])),
                    'markdown_file': data.get('markdown_file', ''),
                    'scraped_at': data['scraped_at']
                }
            else:
                titles_only_pages[url] = data
                summary['pages'][url] = {
                    'title': data['title'],
                    'description': data.get('description', ''),
                    'scraped_at': data['scraped_at']
                }
        
        # Save summary
        summary_file = self.output_dir / "summary.json"
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        
        # Save full data JSON
        full_data_file = self.output_dir / "full_data.json"
        with open(full_data_file, 'w', encoding='utf-8') as f:
            json.dump(self.scraped_data, f, indent=2, ensure_ascii=False)
        
        saved_files = [summary_file, full_data_file]
        
        # Save titles list for /docs pages (titles-only pages)
        if titles_only_pages:
            titles_file = self.output_dir / "page_titles.md"
            with open(titles_file, 'w', encoding='utf-8') as f:
                f.write(f"# Page Titles: {self.base_url}\n\n")
                f.write(f"**Scraped:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"**Total Pages:** {len(titles_only_pages)}\n")
                if self.path_prefix:
                    f.write(f"**Path Filter:** {self.path_prefix}\n")
                f.write("\n---\n\n")
                f.write("## All Page Titles\n\n")
                
                for url, data in sorted(titles_only_pages.items(), key=lambda x: x[1]['title']):
                    f.write(f"- **{data['title']}**\n")
                    f.write(f"  - URL: {url}\n")
                    if data.get('description'):
                        f.write(f"  - Description: {data['description']}\n")
                    f.write("\n")
            
            # Also save as simple list
            titles_list_file = self.output_dir / "titles_list.txt"
            with open(titles_list_file, 'w', encoding='utf-8') as f:
                for url, data in sorted(titles_only_pages.items(), key=lambda x: x[1]['title']):
                    f.write(f"{data['title']}\n")
            
            saved_files.extend([titles_file, titles_list_file])
        
        # Save full content files only for pages with full content
        if full_content_pages:
            # Save all text content in one file
            all_text_file = self.output_dir / "all_content.txt"
            with open(all_text_file, 'w', encoding='utf-8') as f:
                f.write(f"Website Content Scrape: {self.base_url}\n")
                f.write(f"Scraped: {datetime.now().isoformat()}\n")
                f.write("=" * 80 + "\n\n")
                
                for url, data in full_content_pages.items():
                    f.write(f"\n{'=' * 80}\n")
                    f.write(f"URL: {url}\n")
                    f.write(f"Title: {data['title']}\n")
                    f.write(f"{'-' * 80}\n\n")
                    f.write(data.get('text', ''))
                    f.write("\n\n")
            
            # Save all content in one markdown file
            all_markdown_file = self.output_dir / "all_content.md"
            with open(all_markdown_file, 'w', encoding='utf-8') as f:
                f.write(f"# Website Content: {self.base_url}\n\n")
                f.write(f"**Scraped:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"**Total Pages:** {len(full_content_pages)}\n\n")
                f.write("---\n\n")
                
                for url, data in full_content_pages.items():
                    f.write(f"\n# {data['title']}\n\n")
                    f.write(f"**URL:** {url}\n\n")
                    if data.get('description'):
                        f.write(f"**Description:** {data['description']}\n\n")
                    f.write("---\n\n")
                    if 'markdown_content' in data:
                        f.write(data['markdown_content'])
                    else:
                        f.write(data.get('text', ''))
                    f.write("\n\n---\n\n")
            
            saved_files.extend([all_text_file, all_markdown_file])
            print(f"\n💾 Files saved:")
            for file_path in saved_files:
                print(f"   - {file_path}")
            if full_content_pages:
                print(f"   - Markdown files in: {self.output_dir / 'markdown'}")
        else:
            print(f"\n💾 Files saved:")
            for file_path in saved_files:
                print(f"   - {file_path}")


def main():
    parser = argparse.ArgumentParser(description='Scrape entire website content')
    parser.add_argument('url', nargs='?', default='https://www.algorithmshift.ai/',
                       help='URL to scrape (default: https://www.algorithmshift.ai/)')
    parser.add_argument('-o', '--output', default='scraped_content',
                       help='Output directory (default: scraped_content)')
    parser.add_argument('-d', '--delay', type=float, default=1.0,
                       help='Delay between requests in seconds (default: 1.0)')
    parser.add_argument('-m', '--max-pages', type=int, default=None,
                       help='Maximum number of pages to scrape (default: unlimited)')
    parser.add_argument('-t', '--titles-only', action='store_true',
                       help='Only extract page titles (for marketing ideas, no full content)')
    parser.add_argument('-p', '--path-prefix', type=str, default=None,
                       help='Only scrape URLs that start with this path (e.g., /docs)')
    
    args = parser.parse_args()
    
    # Auto-detect path prefix from URL if it contains /docs
    if '/docs' in args.url and not args.path_prefix:
        parsed = urlparse(args.url)
        if '/docs' in parsed.path:
            args.path_prefix = '/docs'
            print(f"🔍 Auto-detected path prefix: {args.path_prefix}")
    
    scraper = WebsiteScraper(args.url, args.output, args.delay, args.titles_only, args.path_prefix)
    scraper.scrape(max_pages=args.max_pages)


if __name__ == '__main__':
    main()
