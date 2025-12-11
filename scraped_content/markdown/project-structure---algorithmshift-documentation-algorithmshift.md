# Project Structure - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/project-structure  
**Scraped:** 2025-12-10 14:02:32

**Description:** Understand how AlgorithmShift organizes workspaces, applications, databases, and resources.

---

Project Structure - AlgorithmShift Documentation | AlgorithmShiftDocumentationGetting Started
# Project Structure

Learn how AlgorithmShift organizes your workspaces, applications, databases, and other resources.

## Organizational Hierarchy

AlgorithmShift uses a hierarchical structure to organize your resources:
Copy
```
Organization (Tenant)
│
├── Workspace 1
│   ├── Applications
│   │   ├── Web App 1
│   │   ├── Mobile App 1
│   │   └── Web App 2
│   ├── Database
│   │   ├── Tables
│   │   ├── Views
│   │   └── Relationships
│   ├── Access Control
│   │   ├── Users
│   │   ├── Groups
│   │   ├── Roles
│   │   └── Permissions
│   ├── Workflows
│   ├── AI Agents
│   ├── Portals
│   ├── Knowledge Base
│   ├── API Hub
│   ├── Functions
│   └── Storage
│
└── Workspace 2
    └── ...
```

## Core Components

### Organization

Top-level entity (tenant) representing your company or team

### Workspace

Isolated environment for development, staging, or production

### Applications

Web and mobile apps built with the visual builder

### Database

PostgreSQL tables, views, and relationships

### Access Control

Users, groups, roles, and permissions management

### Workflows

Automation and business logic processes

## Workspace Structure

Each workspace contains the following sections:

### Applications

Build web and mobile applications

App Builder

Visual drag-and-drop interface
`/[workspaceId]/app`
Pages

Individual app pages and routes
`/[workspaceId]/app/[appId]`
Templates

Reusable app, page, and section templates
`/[workspaceId]/app/templates`
### Database & Data

Manage your data and schemas

Tables

Database table management
`/[workspaceId]/access-control/data-management/tables`
Views

Database views and queries
`/[workspaceId]/access-control/data-management/views`
Data Sheets

Excel-like data editing interface
`/[workspaceId]/app/[appId]/sheets`
### Access Control

Security and permissions

Identity Management

- • Users - User accounts and profiles
- • Groups - Hierarchical user groups
- • User Types - Custom user categories

Authorization

- • Roles - Role definitions
- • Permissions - Permission management
- • Record Bindings - Row-level security
- • Field Permissions - Column-level access

API Security

- • API Keys - Key generation and management
- • API Resources - Endpoint protection

### Workflows

Automation and business logic

Workflow Builder

Visual workflow designer
`/[workspaceId]/workflows/[workflowId]/edit`
Workflow Runs

Execution history and logs
`/[workspaceId]/workflows/[workflowId]/runs`
### AI Agents

Intelligent assistants and chatbots

Agent Builder

Create and configure AI agents
`/[workspaceId]/agents/[agentId]/edit`
Agent Analytics

Performance and usage metrics
`/[workspaceId]/agents/[agentId]`
### Portals

Customer-facing portal applications

Portal Configuration

Branding, auth, and settings
`/[workspaceId]/portals/[portalId]`
Portal Apps

Assign apps to portals
`/[workspaceId]/portals/[portalId]/apps`
## Database Schema Organization

Your workspace database follows a structured schema:
Copy
```
-- Workspace Schema: ws_my_company

-- System Tables (Auto-created)
users
groups
group_types
user_types
roles
permissions
api_keys
api_resources

-- Your Custom Tables
tasks
projects
customers
invoices
...

-- System Views
v_user_permissions
v_group_hierarchy
v_role_assignments

-- Your Custom Views
v_active_projects
v_customer_stats
...
```

## File System Structure

Storage is organized by workspace and resource type:
Copy
```
s3://algorithmshift-storage/
│
├── workspaces/
│   └── my-company/
│       ├── uploads/
│       │   ├── users/
│       │   │   └── {user_id}/
│       │   │       ├── avatar.jpg
│       │   │       └── documents/
│       │   ├── apps/
│       │   │   └── {app_id}/
│       │   │       └── assets/
│       │   └── public/
│       │       └── images/
│       ├── exports/
│       │   ├── database/
│       │   └── code/
│       └── temp/
│           └── {session_id}/

```

## URL Structure

AlgorithmShift uses a consistent URL pattern:
ResourceURL PatternExampleAdmin App`/[workspace]`/my-company/appApp Builder`/[workspace]/app/[appId]/builder`/my-company/app/123/builderREST API`/api/v1/tables/[table]`/api/v1/tables/tasksGraphQL`/graphql/[workspace]`/graphql/my-companyPortal`/portals/[portalId]`/portals/customer-portalPublished App`[workspace].algorithmshift.app`my-company.algorithmshift.app
## API Endpoints Structure

All workspace APIs follow consistent patterns:

### Admin API

Workspace administration and configuration
Copy
```
# Base URL
https://api.algorithmshift.ai/api/v1/

# Endpoints
/workspaces                    # Workspace management
/apps                         # Application CRUD
/workflows                    # Workflow management
/agents                       # AI agent management
/portals                      # Portal management
/knowledge-base              # Knowledge base operations
```

### Client API

Data access and business logic
Copy
```
# Base URL
https://api.algorithmshift.ai/api/v1/

# Data Operations
/tables/{table_name}          # CRUD operations
/views/{view_name}            # View queries
/entities/{table_name}        # Advanced queries with filters

# Access Control
/users                        # User management
/groups                       # Group operations
/permissions                  # Permission checks
/roles                        # Role assignments
```

## Environment Isolation

Use multiple workspaces to separate environments:

### Development

Active development and testing

my-company-dev

### Staging

Pre-production testing

my-company-staging

### Production

Live applications

my-company

## Next Steps

Now that you understand the project structure:
[### Start Building Apps

Learn the visual app builder](https://www.algorithmshift.ai/docs/visual-builder)[### Design Your Database

Create tables and relationships](https://www.algorithmshift.ai/docs/database)[### Configure Access Control

Set up users, roles, and permissions](https://www.algorithmshift.ai/docs/auth)[### Explore the APIs

Understand the REST and GraphQL APIs](https://www.algorithmshift.ai/docs/api)
