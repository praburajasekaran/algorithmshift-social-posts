# Roles & Permissions - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/data-authorization/roles  
**Scraped:** 2025-12-10 14:04:26

**Description:** Role-based access control with workspace admin and workspace user roles, plus custom permission assignment.

---

Roles & Permissions - AlgorithmShift Documentation | AlgorithmShiftDocumentationData Authorization & Security
# Roles & Permissions

Role-based access control system with built-in workspace roles and custom permission assignment.

## Built-In Workspace Roles

Every user in a workspace has one of two roles:

### workspace_admin

Full control

Capabilities:

- • Bypass all RLS: See all data regardless of security layers
- • Manage workspace: Settings, billing, integrations
- • Manage users: Create, edit, delete users and groups
- • Manage security: Configure OWD, RLS policies, permissions
- • Manage tables: Create, modify, delete database tables
- • Manage apps: Create and deploy applications

### workspace_user

Limited access

Capabilities:

- • Subject to RLS: See only authorized data
- • Use apps: Access granted applications
- • View data: Based on permissions and security layers
- • Edit data: Based on permissions and ownership
- • Limited admin: Cannot change security or structure
- • Custom permissions: Can be granted additional access

## User Role Field
Copy
```
-- Users table includes role field
CREATE TABLE sys_users (
  id UUID PRIMARY KEY,
  email VARCHAR UNIQUE NOT NULL,
  name VARCHAR,
  
  -- Role assignment
  role VARCHAR NOT NULL DEFAULT 'workspace_user',
    -- 'workspace_admin' or 'workspace_user'
  
  status VARCHAR DEFAULT 'active',
    -- 'active', 'inactive', 'suspended'
  
  user_type_id UUID,  -- Optional custom user type
  
  -- Metadata
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Check user's role
SELECT role FROM sys_users WHERE id = current_user_id();
```

## Admin Bypass (Layer 0)

Workspace admins automatically bypass all security layers:
Copy
```
-- Security evaluation for ANY query
IF user.role = 'workspace_admin' THEN
  -- Return ALL records (no filtering)
  RETURN query_without_security_filters
ELSE
  -- Apply all 5 security layers
  RETURN query_with_security_filters
END IF

-- Example: Admin query
SELECT * FROM customers;
-- Admin sees: ALL 10,000 customers

-- Example: Regular user query
SELECT * FROM customers;
-- User sees: Only 45 customers they have access to
```

## Permissions System

Beyond roles, users can be granted specific permissions through Permission Sets:

### Table Permissions

CRUD operations on specific tables

- • ps_tbl_{table}_r (read)
- • ps_tbl_{table}_w (write)
- • ps_tbl_{table}_d (delete)

### API Permissions

Access to API endpoints

- • ps_api_{endpoint}_access
- • ps_entities_read
- • ps_entities_write

### Feature Permissions

Access to platform features

- • ps_workflows_create
- • ps_ai_agents_manage
- • ps_portals_admin

## Custom Roles

Create custom roles by combining permission sets:
Copy
```
-- Custom role: "Sales Manager"
-- Stored in sys_roles table
INSERT INTO sys_roles (
  id,
  workspace_id,
  name,
  description,
  permission_sets
) VALUES (
  gen_random_uuid(),
  'workspace-123',
  'Sales Manager',
  'Can manage sales data and view reports',
  ARRAY[
    'ps_tbl_accounts_r',
    'ps_tbl_accounts_w',
    'ps_tbl_opportunities_r',
    'ps_tbl_opportunities_w',
    'ps_tbl_reports_r',
    'ps_workflows_create',
    'ps_entities_read'
  ]
);

-- Assign role to user
INSERT INTO sys_user_roles (
  user_id,
  role_id
) VALUES (
  'user-alice',
  'role-sales-manager'
);

-- Alice now has all Sales Manager permissions
```

## Permission Checking

Check if a user has a specific permission:
Copy
```
-- Check if current user has permission
SELECT has_permission('ps_tbl_accounts_w');
-- Returns: true or false

-- Check multiple permissions (requires ALL)
SELECT has_all_permissions(ARRAY[
  'ps_tbl_accounts_r',
  'ps_tbl_accounts_w'
]);

-- Check any permission (requires ANY)
SELECT has_any_permission(ARRAY[
  'ps_workflows_create',
  'ps_workflows_edit'
]);

-- In application code (automatic)
-- User tries to create a workflow
IF !has_permission('ps_workflows_create') THEN
  RETURN 403 Forbidden
END IF
```

## Role Management Interface

### Roles Management

Navigate to: /{workspaceId}/access-control/authorization/roles

Create Custom Roles

Define roles with specific permission sets

Assign Roles to Users

Grant roles to individual users

Role Templates

Pre-configured roles for common use cases

Permission Browser

Browse and select from available permissions

## Common Custom Roles

### Sales Representative
Copy
```
Permissions:
  - Read/Write: Accounts, Contacts, Opportunities
  - Read: Products, Price Books, Reports
  - Create: Activities, Notes
  - Execute: Email workflows
```

### Support Agent
Copy
```
Permissions:
  - Read: Accounts, Contacts, Products
  - Read/Write: Cases, Support Tickets
  - Create: Internal Notes
  - Access: Knowledge Base
  - Execute: Ticket workflows
```

### Marketing User
Copy
```
Permissions:
  - Read: Accounts, Contacts, Leads
  - Read/Write: Campaigns, Email Templates
  - Create: Marketing workflows
  - Access: Marketing analytics
  - Execute: Email campaigns
```

### Report Viewer
Copy
```
Permissions:
  - Read: All data tables (via RLS)
  - Read: Reports, Dashboards
  - Export: Data to CSV
  - No write permissions
```

## Best Practices

Use workspace_admin sparingly

Only grant admin role to trusted users who need full access

Create role-based groups

Combine custom roles with groups for department-level access

Follow principle of least privilege

Grant only the minimum permissions needed for each role

Use permission sets, not individual permissions

Group related permissions into sets for easier management

Regular access audits

Review user roles and permissions quarterly

## Learn More
[### Permission Sets

Understand the permission set system](https://www.algorithmshift.ai/docs/data-authorization/permission-sets)[### Identity Management

Manage users and assign roles](https://www.algorithmshift.ai/docs/data-authorization/identity)[### Security Overview

Complete security model](https://www.algorithmshift.ai/docs/data-authorization)
