# Visual App Builder - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/visual-builder  
**Scraped:** 2025-12-10 14:02:34

**Description:** Build web and mobile applications with AlgorithmShift's drag-and-drop visual builder. No coding required, but code access available.

---

Visual App Builder - AlgorithmShift Documentation | AlgorithmShiftDocumentationApp Builder
# Visual App Builder

Build production-ready web and mobile applications with our intuitive drag-and-drop interface. Design visually, export code, and deploy instantly.

### Drag & Drop

Visual interface builder with no coding required

### Web & Mobile

Build for web browsers and native iOS/Android

### Live Preview

See changes in real-time as you build

### Rich Components

50+ pre-built components ready to use

### Instant Deploy

Deploy to production with one click

### Code Export

Export clean React/React Native code

## Choose Your Platform

AlgorithmShift supports both web and mobile application development with the same intuitive builder.
[### Web Applications

Browser-based apps
React/Next.js componentsResponsive design (desktop, tablet, mobile)SEO optimizedPWA supportLearn more →](https://www.algorithmshift.ai/docs/visual-builder/web-apps)[### Mobile Applications

iOS & Android native apps
React Native componentsNative performanceLive mobile previewApp Store deploymentLearn more →](https://www.algorithmshift.ai/docs/visual-builder/mobile-apps)
## Builder Interface

The visual builder consists of four main areas designed for maximum productivity:
1
### Component Library (Left Sidebar)

Browse and drag components onto your canvas. Organized by category:

Layout

Grid, Flex, Container

Forms

Input, Select, Checkbox

Data Display

Table, List, Card

Navigation

NavBar, Tabs, Menu

Media

Image, Video, Icon

Charts

Line, Bar, Pie
2
### Visual Canvas (Center)

Your main workspace where you design your application. Features include:

- Live Preview: See your changes in real-time
- Responsive Views: Switch between desktop, tablet, mobile, and app modes
- Smart Guides: Alignment and spacing helpers
- Component Tree: Navigate nested components
3
### Properties Panel (Right Sidebar)

Configure selected components with:

Styling

Colors, spacing, typography, borders

Actions

Click handlers, navigation, API calls

Data Binding

Connect to database tables and APIs
4
### Top Toolbar
Undo/RedoSavePreviewCode ExportDeploySettings
## Creating Your First App

Follow these steps to create your first application:
1
### Create New App

Navigate to the Apps section and click "Create App"
Copy
```
// Navigate to:
/{workspaceId}/app

// Click "Create App" and fill in:
{
  "name": "My Task Manager",
  "type": "web",  // or "mobile"
  "description": "A simple task management app",
  "status": "development"
}
```
2
### Choose Template (Optional)

Start from scratch or use a pre-built template:

Blank Canvas

Start from scratch

Dashboard

Analytics dashboard layout

CRM

Customer management

E-commerce

Product catalog
3
### Design Your Pages

Drag components from the library onto your canvas:
Copy
```
// Example: Building a task list page

1. Drag a Container component
2. Add a Typography component for the title
3. Drop a Table component inside
4. Configure data source: "tasks" table
5. Add a Form component for new tasks
6. Style components to match your brand
```
4
### Configure Data & Actions

Connect your components to data sources and define actions:
Copy
```
// Table component data binding
{
  "dataSource": "tasks",
  "columns": ["title", "status", "created_at"],
  "filters": {
    "status": "active"
  },
  "sort": { "field": "created_at", "order": "desc" }
}

// Button click action
{
  "onClick": {
    "type": "api_call",
    "method": "POST",
    "endpoint": "/api/v1/tables/tasks",
    "body": "{{ formData }}",
    "onSuccess": "refreshTable"
  }
}
```
5
### Preview & Test

Test your app in different screen sizes:
Desktop (1920x1080)Tablet (768x1024)Mobile (390x844)App (375x812)6
### Deploy

Deploy your app to production with one click:
Copy
```
// Your app will be available at:
https://{workspace}.algorithmshift.app/{app-slug}

// Example:
https://my-company.algorithmshift.app/task-manager
```

## Key Features

### Data Binding

Connect any component to your database tables, APIs, or state:
Copy
```
// Simple data binding
dataSource: "tasks"

// Advanced filtering
dataSource: {
  table: "tasks",
  filter: { status: "active" },
  sort: { created_at: "desc" },
  limit: 10
}
```

### Event Handlers

Define actions for clicks, form submissions, and more:
Copy
```
{
  "onClick": "navigateTo('/dashboard')",
  "onSubmit": "createRecord",
  "onChange": "updateState"
}
```

### Conditional Rendering

Show/hide components based on conditions:
Copy
```
// Show only if user is admin
visible: "{{ user.role === 'admin' }}"

// Show based on data
visible: "{{ tasks.length > 0 }}"
```

### Code Export

Export clean, production-ready code:

- • React/Next.js for web apps
- • React Native for mobile apps
- • Complete project structure
- • All dependencies included

## Learn More

Explore detailed guides for different aspects of the visual builder:
[### Component Library

Complete reference of all available components](https://www.algorithmshift.ai/docs/visual-builder/components)[### Templates

Pre-built app, page, and section templates](https://www.algorithmshift.ai/docs/visual-builder/templates)[### Styling & Themes

Customize colors, fonts, and styles](https://www.algorithmshift.ai/docs/styling)[### Forms & Validation

Build forms with validation and submission](https://www.algorithmshift.ai/docs/forms)[### Data Tables

Display and manage tabular data](https://www.algorithmshift.ai/docs/tables)[### State Management

Manage application state and data flow](https://www.algorithmshift.ai/docs/state)
