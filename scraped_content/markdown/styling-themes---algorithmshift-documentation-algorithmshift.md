# Styling & Themes - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/styling  
**Scraped:** 2025-12-10 14:03:18

**Description:** Customize your applications with colors, fonts, spacing, and responsive design. Built-in dark mode and theme support.

---

Styling & Themes - AlgorithmShift Documentation | AlgorithmShiftDocumentationApp Builder
# Styling & Themes

Customize every aspect of your application's appearance. Control colors, typography, spacing, and create responsive designs that work on all devices.

### Visual Styling

No CSS knowledge needed

### Responsive Design

Different styles per device

### Dark Mode

Built-in light/dark themes

### Typography

Google Fonts integration

## Style Properties

Every component has a comprehensive set of styling options:

### Layout & Spacing
PropertyValuesExample`width`px, %, auto, full`width: "100%"``height`px, %, auto, full`height: "400px"``padding`0-20 (4px increments)`padding: 4` = 16px`margin`0-20 (4px increments)`margin: 2` = 8px`gap`0-20 (4px increments)`gap: 3` = 12px
### Colors & Backgrounds

#### Color Formats
`#3B82F6`Hex`rgb(59, 130, 246)`RGB`rgba(59, 130, 246, 0.5)`RGBA
#### Example Styling
Copy
```
{
  "backgroundColor": "#3B82F6",
  "color": "#FFFFFF",
  "borderColor": "#2563EB",
  "backgroundImage": "linear-gradient(to right, #3B82F6, #8B5CF6)"
}
```

### Typography

#### Font Properties
fontFamily`Inter, Roboto, etc.`fontSize`12-72 (px)`fontWeight`100-900`lineHeight`1.0-3.0`letterSpacing`-2 to 10 (px)`
#### Text Styling
Copy
```
{
  "fontFamily": "Inter",
  "fontSize": 16,
  "fontWeight": 600,
  "lineHeight": 1.5,
  "letterSpacing": 0,
  "textAlign": "left",
  "textTransform": "none",
  "textDecoration": "none"
}
```

### Borders & Shadows

#### Border Styling
Copy
```
{
  "borderWidth": 1,
  "borderColor": "#E5E7EB",
  "borderStyle": "solid",
  "borderRadius": 8
}

// Individual sides
{
  "borderTopWidth": 2,
  "borderBottomWidth": 0,
  "borderLeftWidth": 0,
  "borderRightWidth": 0
}
```

#### Box Shadow
Copy
```
{
  "boxShadow": "0 1px 3px rgba(0,0,0,0.1)"
}

// Presets
"shadow-sm"   // Small shadow
"shadow-md"   // Medium shadow
"shadow-lg"   // Large shadow
"shadow-xl"   // Extra large shadow
```

## Responsive Design

Create designs that adapt to different screen sizes:

### Breakpoints
BreakpointMin WidthTypical Device`mobile`0pxPhones (portrait)`sm`640pxPhones (landscape)`md`768pxTablets`lg`1024pxLaptops`xl`1280pxDesktops`2xl`1536pxLarge monitors
### Responsive Styling Example
Copy
```
// Component with responsive styles
{
  "styles": {
    // Default (mobile-first)
    "padding": 2,      // 8px
    "fontSize": 14,
    "gridColumns": 1
  },
  "responsiveStyles": {
    "md": {
      // Tablet and up
      "padding": 4,    // 16px
      "fontSize": 16,
      "gridColumns": 2
    },
    "lg": {
      // Desktop and up
      "padding": 6,    // 24px
      "fontSize": 18,
      "gridColumns": 3
    }
  }
}
```

## Theme Configuration

Create consistent themes across your entire application:
Copy
```
// Global theme configuration
{
  "colors": {
    "primary": "#3B82F6",
    "secondary": "#8B5CF6",
    "success": "#10B981",
    "warning": "#F59E0B",
    "error": "#EF4444",
    "background": "#FFFFFF",
    "surface": "#F9FAFB",
    "text": {
      "primary": "#111827",
      "secondary": "#6B7280",
      "disabled": "#9CA3AF"
    },
    "border": "#E5E7EB"
  },
  "typography": {
    "fontFamily": {
      "primary": "Inter",
      "heading": "Inter",
      "mono": "JetBrains Mono"
    },
    "fontSize": {
      "xs": 12,
      "sm": 14,
      "base": 16,
      "lg": 18,
      "xl": 20,
      "2xl": 24,
      "3xl": 30,
      "4xl": 36
    },
    "fontWeight": {
      "light": 300,
      "normal": 400,
      "medium": 500,
      "semibold": 600,
      "bold": 700
    }
  },
  "spacing": {
    "unit": 4,  // Base unit in px
    "scale": [0, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80]
  },
  "borderRadius": {
    "sm": 4,
    "md": 8,
    "lg": 12,
    "xl": 16,
    "full": 9999
  },
  "shadows": {
    "sm": "0 1px 2px rgba(0,0,0,0.05)",
    "md": "0 4px 6px rgba(0,0,0,0.1)",
    "lg": "0 10px 15px rgba(0,0,0,0.1)",
    "xl": "0 20px 25px rgba(0,0,0,0.1)"
  }
}
```

## Dark Mode

Built-in support for light and dark color schemes:

### Theme Switching

#### Light Theme
Copy
```
{
  "backgroundColor": "#FFFFFF",
  "color": "#111827",
  "borderColor": "#E5E7EB"
}
```

#### Dark Theme
Copy
```
{
  "backgroundColor": "#1F2937",
  "color": "#F9FAFB",
  "borderColor": "#374151"
}
```

Define both light and dark styles for each component. The system automatically switches based on user preference.

## Pre-built Style Presets

Use pre-configured style presets for common patterns:

### Card Styles

Default

Border + shadow

Filled

Background only

Outlined

Prominent border

### Button Variants

Primary

Outline

Secondary

Link

### Input Styles

## Tailwind CSS Integration

AlgorithmShift uses Tailwind CSS utility classes for rapid styling:

#### Visual Editor

Use the visual properties panel - no Tailwind knowledge needed!

Properties Panel:

- • Color picker for backgrounds
- • Slider for padding/margin
- • Dropdown for fonts
- • Number input for sizes

#### Advanced: Custom Classes
Copy
```
// Add custom Tailwind classes
{
  "className": "hover:shadow-lg transition-all duration-300 backdrop-blur-sm"
}

// Responsive classes
{
  "className": "w-full md:w-1/2 lg:w-1/3"
}
```

## Common Styling Patterns

### Card with Shadow
Copy
```
{
  "backgroundColor": "#FFFFFF",
  "borderRadius": 8,
  "boxShadow": "0 1px 3px rgba(0,0,0,0.1)",
  "padding": 4
}
```

### Gradient Background
Copy
```
{
  "backgroundImage": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
  "color": "#FFFFFF"
}
```

### Hover Effects
Copy
```
{
  "backgroundColor": "#3B82F6",
  "transition": "all 0.3s ease",
  "hover": {
    "backgroundColor": "#2563EB",
    "transform": "scale(1.05)"
  }
}
```

### Glassmorphism
Copy
```
{
  "backgroundColor": "rgba(255, 255, 255, 0.1)",
  "backdropFilter": "blur(10px)",
  "borderRadius": 16,
  "border": "1px solid rgba(255, 255, 255, 0.2)"
}
```

## Learn More
[### Component Library

Explore all available components](https://www.algorithmshift.ai/docs/components)[### Visual Builder

Learn the app builder interface](https://www.algorithmshift.ai/docs/visual-builder)
