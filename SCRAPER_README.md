# Website Scraper

A Python script to scrape the entire content of AlgorithmShift.ai (or any website).

## Features

- ✅ Scrapes all pages on the website by following internal links
- ✅ Extracts text content, images, and metadata
- ✅ Saves HTML files, images, and other assets
- ✅ Creates organized output with JSON summaries
- ✅ Respects rate limits with configurable delays
- ✅ Handles errors gracefully

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage (scrape AlgorithmShift.ai)
```bash
python scrape_website.py
```

### Scrape a Different Website
```bash
python scrape_website.py https://example.com
```

### Custom Output Directory
```bash
python scrape_website.py -o my_scraped_content
```

### Adjust Request Delay (be more/less aggressive)
```bash
python scrape_website.py -d 2.0  # 2 second delay between requests
```

### Limit Number of Pages
```bash
python scrape_website.py -m 10  # Only scrape first 10 pages
```

### All Options
```bash
python scrape_website.py [URL] -o OUTPUT_DIR -d DELAY -m MAX_PAGES
```

## Output Structure

After scraping, you'll find:

```
scraped_content/
├── pages/              # HTML files for each page
├── images/             # All images from the website
├── assets/             # CSS, JS, and other assets
├── summary.json        # Quick overview of scraped content
├── full_data.json      # Complete data with all content
└── all_content.txt     # All text content in one file
```

## Example Output Files

- **summary.json**: Overview with titles, descriptions, and previews
- **full_data.json**: Complete data including full text, images, links
- **all_content.txt**: Plain text version of all scraped content

## Notes

- The scraper only follows links within the same domain
- Images and assets are downloaded to local directories
- The script includes a 1-second delay by default to be respectful
- JavaScript-rendered content may not be captured (use Selenium for that)

## Troubleshooting

If you encounter issues:
1. Make sure you have internet connectivity
2. Check that the website is accessible
3. Verify Python dependencies are installed: `pip install -r requirements.txt`
4. For JavaScript-heavy sites, consider using Selenium-based scraping







