# Permission Sets - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/data-authorization/permission-sets  
**Scraped:** 2025-12-10 14:04:14

**Description:** Deterministic UUID-based permission system for fast, in-memory permission checks.

---

Permission Sets - AlgorithmShift Documentation | AlgorithmShiftDocumentationData Authorization & Security
# Permission Sets

AlgorithmShift's unique deterministic UUID-based permission system enables instant, in-memory permission checks without database lookups.

## What Makes Permission Sets Special?

### Deterministic UUID v5 System

Traditional permission systems require database lookups: "Does user X have permission Y?"

AlgorithmShift uses deterministic UUIDs (UUID v5) for permissions. The same permission name always generates the same UUID.

Result: Check permissions in-memory with simple UUID array lookups. No database calls needed.

## How It Works
Copy
```
// Permission name → Deterministic UUID (always the same)
"ps_tbl_customers_r" → "8a7c9f2e-3b4d-5e6f-7a8b-9c0d1e2f3a4b"
"ps_tbl_customers_w" → "1b2c3d4e-5f6a-7b8c-9d0e-1f2a3b4c5d6e"

// User's permissions stored as UUID array
user.permissions = [
  "8a7c9f2e-3b4d-5e6f-7a8b-9c0d1e2f3a4b",  // read customers
  "1b2c3d4e-5f6a-7b8c-9d0e-1f2a3b4c5d6e",  // write customers
  ...
]

// Permission check (in-memory, instant)
function hasPermission(permissionName) {
  const uuid = generateUUIDv5(permissionName);  // Deterministic
  return user.permissions.includes(uuid);       // Array lookup
}

// No database query needed! ⚡
```

## Permission Set Naming Convention

All permission sets follow a consistent naming pattern:

#### Table Permissions
Copy
```
ps_tbl_{table_name}_{operation}

Examples:
  ps_tbl_customers_r       → Read customers table
  ps_tbl_customers_w       → Write customers table
  ps_tbl_customers_d       → Delete from customers table
  ps_tbl_opportunities_r   → Read opportunities table
  ps_tbl_opportunities_w   → Write opportunities table
```

#### Entity/API Permissions
Copy
```
ps_entities_{operation}

Examples:
  ps_entities_read         → Read entity metadata
  ps_entities_write        → Write entity metadata
  ps_entities_create       → Create new entities
  ps_entities_edit         → Edit existing entities
  ps_entities_delete       → Delete entities
```

#### Feature Permissions
Copy
```
ps_{feature}_{operation}

Examples:
  ps_workflows_create      → Create workflows
  ps_workflows_execute     → Execute workflows
  ps_ai_agents_manage      → Manage AI agents
  ps_portals_admin         → Administer portals
  ps_reports_create        → Create reports
  ps_reports_export        → Export report data
```

## UUID v5 Generation

Permission UUIDs are generated using UUID v5 with a namespace:
Copy
```
import { v5 as uuidv5 } from 'uuid';

// Workspace-specific namespace
const PERMISSION_NAMESPACE = 'workspace-123-permissions';

// Generate deterministic permission UUID
function getPermissionUUID(permissionName) {
  return uuidv5(permissionName, PERMISSION_NAMESPACE);
}

// Example usage
const readCustomersUUID = getPermissionUUID('ps_tbl_customers_r');
// Always returns: "8a7c9f2e-3b4d-5e6f-7a8b-9c0d1e2f3a4b"

// Multiple calls return the SAME UUID
console.log(getPermissionUUID('ps_tbl_customers_r'));
// "8a7c9f2e-3b4d-5e6f-7a8b-9c0d1e2f3a4b"
console.log(getPermissionUUID('ps_tbl_customers_r'));
// "8a7c9f2e-3b4d-5e6f-7a8b-9c0d1e2f3a4b"  ← Same!
```

## User Permission Storage
Copy
```
-- sys_user_permissions table
CREATE TABLE sys_user_permissions (
  id UUID PRIMARY KEY,
  workspace_id UUID NOT NULL,
  user_id UUID NOT NULL,
  
  -- The deterministic permission UUID
  permission_id UUID NOT NULL,
  
  -- Optional: Store the name for reference
  permission_name VARCHAR,
  
  -- Grant metadata
  granted_at TIMESTAMP DEFAULT NOW(),
  granted_by UUID,
  
  UNIQUE(workspace_id, user_id, permission_id)
);

-- Grant permission to user
INSERT INTO sys_user_permissions (
  id,
  workspace_id,
  user_id,
  permission_id,
  permission_name
) VALUES (
  gen_random_uuid(),
  'workspace-123',
  'user-alice',
  '8a7c9f2e-3b4d-5e6f-7a8b-9c0d1e2f3a4b',  -- UUID for ps_tbl_customers_r
  'ps_tbl_customers_r'
);
```

## Permission Checking (Lightning Fast)

### In-Memory Check (No Database)
Copy
```
// Load user's permissions once (on login)
const userPermissions = [
  '8a7c9f2e-3b4d-5e6f-7a8b-9c0d1e2f3a4b',  // ps_tbl_customers_r
  '1b2c3d4e-5f6a-7b8c-9d0e-1f2a3b4c5d6e',  // ps_tbl_customers_w
  '2c3d4e5f-6a7b-8c9d-0e1f-2a3b4c5d6e7f',  // ps_workflows_create
  // ... stored in session/JWT
];

// Check permission (instant, in-memory)
function hasPermission(permissionName) {
  const permissionUUID = getPermissionUUID(permissionName);
  return userPermissions.includes(permissionUUID);
}

// Usage
if (hasPermission('ps_tbl_customers_w')) {
  // Allow write to customers
} else {
  // Deny access
}

// Performance: O(1) hash lookup, ~1 microsecond 🚀
```

### Permission Check in SQL
Copy
```
-- Check if user has permission (PostgreSQL)
CREATE FUNCTION has_permission(permission_name VARCHAR)
RETURNS BOOLEAN AS $$
DECLARE
  permission_uuid UUID;
BEGIN
  -- Generate deterministic UUID
  permission_uuid := uuid_generate_v5(
    'workspace-123-permissions'::uuid,
    permission_name
  );
  
  -- Check if user has this permission
  RETURN EXISTS (
    SELECT 1 FROM sys_user_permissions
    WHERE user_id = current_user_id()
    AND permission_id = permission_uuid
  );
END;
$$ LANGUAGE plpgsql;

-- Usage
SELECT * FROM customers
WHERE has_permission('ps_tbl_customers_r');
```

## Assigning Permission Sets to Roles
Copy
```
-- Create role with multiple permission sets
INSERT INTO sys_roles (
  id,
  workspace_id,
  name,
  permission_sets  -- Array of permission NAMES (not UUIDs)
) VALUES (
  gen_random_uuid(),
  'workspace-123',
  'Sales Manager',
  ARRAY[
    'ps_tbl_accounts_r',
    'ps_tbl_accounts_w',
    'ps_tbl_opportunities_r',
    'ps_tbl_opportunities_w',
    'ps_tbl_reports_r',
    'ps_workflows_create'
  ]
);

-- When user is assigned this role, convert names → UUIDs
-- and insert into sys_user_permissions
INSERT INTO sys_user_permissions (
  id, workspace_id, user_id, permission_id, permission_name
)
SELECT 
  gen_random_uuid(),
  'workspace-123',
  'user-alice',
  uuid_generate_v5('workspace-123-permissions'::uuid, permission_name),
  permission_name
FROM unnest(ARRAY[
  'ps_tbl_accounts_r',
  'ps_tbl_accounts_w',
  'ps_tbl_opportunities_r',
  'ps_tbl_opportunities_w',
  'ps_tbl_reports_r',
  'ps_workflows_create'
]) AS permission_name;
```

## Benefits of Deterministic Permission UUIDs

### Lightning Fast

No database lookups. Check thousands of permissions per second with simple array includes.

### Deterministic

Same permission name always generates the same UUID across all servers and environments.

### Cacheable

Store user permissions in JWT, session, or memory. No cache invalidation needed.

### Secure

UUIDs are not guessable. Even if an attacker has a UUID, they can't create permissions.

### Developer Friendly

Use readable permission names in code. UUIDs are generated automatically.

### Scalable

Works with millions of users and billions of permission checks per day.

## Common Permission Sets
CategoryPermission SetDescriptionTables`ps_tbl_{table}_r`Read from tableTables`ps_tbl_{table}_w`Write to tableTables`ps_tbl_{table}_d`Delete from tableEntities`ps_entities_read`Read entity definitionsEntities`ps_entities_write`Modify entity definitionsWorkflows`ps_workflows_create`Create workflowsWorkflows`ps_workflows_execute`Execute workflowsAI Agents`ps_ai_agents_manage`Manage AI agentsPortals`ps_portals_admin`Administer portalsReports`ps_reports_export`Export report data
## Learn More
[### Roles & Permissions

Create roles with permission sets](https://www.algorithmshift.ai/docs/data-authorization/roles)[### API Resource Protection

Protect endpoints with permissions](https://www.algorithmshift.ai/docs/data-authorization/api-resources)[### Security Overview

Complete security model](https://www.algorithmshift.ai/docs/data-authorization)
