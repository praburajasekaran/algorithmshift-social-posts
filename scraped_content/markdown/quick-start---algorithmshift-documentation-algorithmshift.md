# Quick Start - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/quick-start  
**Scraped:** 2025-12-10 14:02:29

**Description:** Get started with AlgorithmShift in 5 minutes. Create your first application and deploy it to production.

---

Quick Start - AlgorithmShift Documentation | AlgorithmShiftDocumentationGetting Started
# Quick Start Guide

Get up and running with AlgorithmShift in 5 minutes. This guide will walk you through creating your first application.

### What You'll Build

In this quick start, you'll create a simple task management application with:

- ✓ Database tables for storing tasks
- ✓ Auto-generated REST APIs
- ✓ Visual app builder interface
- ✓ User authentication
- ✓ Deployed to production

## Prerequisites

Before you begin, make sure you have:

AlgorithmShift Account

Sign up at algorithmshift.ai

Web Browser

Chrome, Firefox, or Safari

## Step 1: Create a Workspace

A workspace is your isolated development environment. Each workspace has its own database, APIs, and team members.
1
### Navigate to the Dashboard

After logging in, you'll be prompted to create your first workspace.
Copy
```
// Your workspace will be automatically provisioned with:
- PostgreSQL database (isolated schema)
- REST API endpoints
- GraphQL API
- Authentication system
- Storage bucket (AWS S3)
```
2
### Enter Workspace Details

Provide a name and slug for your workspace.

Workspace Name

My Company

Workspace Slug

my-company (used in URLs)
3
### Workspace Created!

Your workspace is now ready. You'll automatically be assigned as the workspace_admin.

## Step 2: Create a Database Table

Let's create a table to store our tasks. AlgorithmShift will automatically generate REST APIs for this table.

### Using the Visual Schema Designer

1. 1. Navigate to Data Management → Tables
1. 2. Click "Create Table"
1. 3. Name it tasks
1. 4. Add the following columns:
Column NameTypeConstraints`id`UUIDPrimary Key`title`VARCHAR(255)NOT NULL`description`TEXT-`status`VARCHAR(50)Default: 'pending'`created_at`TIMESTAMPDefault: NOW()
### Auto-Generated APIs

When you create a table, AlgorithmShift automatically generates REST APIs:
Copy
```
GET    /api/v1/tables/tasks          # List all tasks
POST   /api/v1/tables/tasks          # Create a task
GET    /api/v1/tables/tasks/:id      # Get single task
PUT    /api/v1/tables/tasks/:id      # Update a task
DELETE /api/v1/tables/tasks/:id      # Delete a task
```

## Step 3: Test Your API

Let's test the auto-generated API by creating a task.

#### Using cURL
Copy
```
curl -X POST \
  https://api.algorithmshift.ai/api/v1/tables/tasks \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My First Task",
    "description": "Testing the API",
    "status": "pending"
  }'
```

#### Using JavaScript
Copy
```
const response = await fetch(
  'https://api.algorithmshift.ai/api/v1/tables/tasks',
  {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_API_KEY',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      title: 'My First Task',
      description: 'Testing the API',
      status: 'pending'
    })
  }
);
const task = await response.json();
```

#### API Response
Copy
```
{
  "success": true,
  "data": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "title": "My First Task",
    "description": "Testing the API",
    "status": "pending",
    "created_at": "2024-01-15T10:30:00Z"
  }
}
```

## Step 4: Build the User Interface

Now let's create a visual interface for our task management app using the drag-and-drop builder.

### Create Your First App

1. 1. Navigate to App Builder → Apps
1. 2. Click "Create App"
1. 3. Choose "Web App" or "Mobile App"
1. 4. Name it "Task Manager"
1. 5. Click "Open Builder"
+
### Add Components to Your Page

Drag and drop components from the left sidebar onto the canvas:

Container

Layout wrapper

Table

Display tasks

Form

Add new tasks

Button

Actions

### Connect to Your Data

Bind the Table component to your tasks table:

1. 1. Select the Table component
1. 2. In the properties panel, set Data Source to "tasks"
1. 3. The table will automatically display your tasks

## Step 5: Add Authentication

Protect your app with built-in authentication.
Copy
```
// Enable authentication in your app settings
{
  "authentication": {
    "required": true,
    "providers": ["email", "google"],
    "redirectUrl": "/dashboard"
  }
}
```

### Row-Level Security (RLS)

For multi-user apps, enable RLS on your tasks table so users can only see their own tasks. Learn more in the RLS documentation.

## Step 6: Deploy Your App

Deploy your app to production with a single click.

### Instant Deploy

Click "Deploy" button in the app builder

### Auto Scaling

Your app automatically scales with traffic

### Live URL

Get a production URL instantly
Copy
```
# Your app is now live at:
https://your-workspace.algorithmshift.app/task-manager

# Or use a custom domain:
https://tasks.yourcompany.com
```

## Next Steps

Congratulations! You've built and deployed your first app. Here's what to explore next:
[### Learn the Visual Builder

Explore all components, layouts, and advanced features](https://www.algorithmshift.ai/docs/visual-builder)[### Master Database & APIs

Create complex schemas, relationships, and custom queries](https://www.algorithmshift.ai/docs/database)[### Secure Your App

Add authentication, roles, and row-level security](https://www.algorithmshift.ai/docs/auth)[### Automate with Workflows

Create automated processes and business logic](https://www.algorithmshift.ai/docs/workflows)[### Build Mobile Apps

Create native iOS and Android applications](https://www.algorithmshift.ai/docs/mobile)[### Add AI Agents

Build intelligent chatbots and assistants](https://www.algorithmshift.ai/docs/ai-agents)
### Need Help?

Join our community or check out more resources:
[Tutorials →](https://www.algorithmshift.ai/docs/tutorials)[Code Examples →](https://www.algorithmshift.ai/docs/examples)[Community →](https://www.algorithmshift.ai/docs/community)
