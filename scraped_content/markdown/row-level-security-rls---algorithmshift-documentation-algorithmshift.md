# Row-Level Security (RLS) - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/auth/rls  
**Scraped:** 2025-12-10 14:03:08

**Description:** Implement row-level security to control data access at the database level. Secure your data with RLS policies.

---

Row-Level Security (RLS) - AlgorithmShift Documentation | AlgorithmShiftDocumentationAuthentication
# Row-Level Security (RLS)

Control data access at the row level. Ensure users can only see and modify data they're authorized to access. Enforced at the database level for maximum security.

### Database-Level

Can't be bypassed

### Automatic

No code changes needed

### Flexible

User, group, role-based

### Performant

PostgreSQL optimized

## How RLS Works

### RLS Overview

Row-Level Security policies are enforced at the PostgreSQL database level. When a user queries a table, the RLS policy automatically filters results based on the policy conditions.
Copy
```
-- User queries: SELECT * FROM tasks

-- PostgreSQL automatically applies RLS:
SELECT * FROM tasks 
WHERE user_id = current_user_id()

-- User only sees their own tasks!
```

## Common RLS Patterns

### Owner-Based Access

Users can only access records they created

#### Policy Configuration
Copy
```
{
  "table": "tasks",
  "policyName": "owner_access",
  "operation": "SELECT",
  "condition": "created_by = {{ current_user.id }}"
}
```

#### Generated SQL
Copy
```
CREATE POLICY owner_access 
ON tasks
FOR SELECT
USING (created_by = current_user_id());
```

Users can only SELECT rows where they are the creator.

### Group-Based Access

Users can access records belonging to their group
Copy
```
{
  "table": "projects",
  "policyName": "group_access",
  "operation": "ALL",
  "condition": "group_id IN (SELECT group_id FROM user_groups WHERE user_id = {{ current_user.id }})"
}

-- Users can access projects from any group they belong to
```

### Role-Based Access

Different access based on user role
Copy
```
{
  "table": "customers",
  "policyName": "role_based_access",
  "operation": "SELECT",
  "condition": `CASE
    WHEN {{ current_user.role }} = 'admin' THEN true
    WHEN {{ current_user.role }} = 'manager' THEN department_id = {{ current_user.department_id }}
    ELSE assigned_to = {{ current_user.id }}
  END`
}

-- Admins: See all customers
-- Managers: See customers in their department
-- Others: See only assigned customers
```

### Hierarchical Access

Access based on organizational hierarchy
Copy
```
{
  "table": "employees",
  "policyName": "hierarchy_access",
  "operation": "SELECT",
  "condition": `id = {{ current_user.id }} 
  OR manager_id = {{ current_user.id }}
  OR id IN (
    SELECT e.id FROM employees e
    WHERE e.manager_id IN (
      SELECT id FROM employees WHERE manager_id = {{ current_user.id }}
    )
  )`
}

-- Users can see: themselves, their direct reports, 
-- and their reports' reports
```

## Enabling RLS
1
### Navigate to Table Settings

Go to Access Control → Data Management → Tables, select your table, and click "Enable RLS"
2
### Create Policy

Click "Add Policy" and configure:

Policy Name

user_can_read_own_tasks

Operation

SELECT (or ALL, INSERT, UPDATE, DELETE)

Condition

user_id = {{ current_user.id }}
3
### Test the Policy

Query the table and verify users only see authorized data:
Copy
```
// User A queries tasks
GET /api/v1/tables/tasks

// Returns only tasks where user_id = User A's ID
{
  "data": [
    { "id": 1, "title": "My task", "user_id": "user-a" }
    // Other users' tasks NOT included
  ]
}
```

### Important Security Notes

- RLS is enforced at the database level - it cannot be bypassed through the API
- Always test RLS policies thoroughly before production
- Use workspace_admin role to bypass RLS for administration
- Monitor RLS performance on large tables

## Advanced RLS Patterns

### Time-Based Access
Copy
```
{
  "table": "subscriptions",
  "condition": "valid_from <= NOW() AND valid_until >= NOW()"
}

-- Users can only access active subscriptions within the valid period
```

### Shared Records
Copy
```
{
  "table": "documents",
  "condition": `
    owner_id = {{ current_user.id }}
    OR id IN (
      SELECT document_id 
      FROM document_shares 
      WHERE shared_with_user_id = {{ current_user.id }}
    )
  `
}

-- Users can access documents they own OR that are shared with them
```

### Multi-Tenant Isolation
Copy
```
{
  "table": "all_tables",
  "condition": "tenant_id = {{ current_user.tenant_id }}"
}

-- Ensures complete data isolation between tenants
-- Critical for SaaS applications
```

## RLS Functions

Use built-in RLS functions in your policies:
FunctionReturnsDescription`current_user_id()`UUIDCurrent authenticated user ID`current_user_role()`VARCHARUser's primary role`user_groups()`UUID[]Array of user's group IDs`has_permission(perm)`BOOLEANCheck if user has permission`is_admin()`BOOLEANCheck if workspace admin
## Learn More
[### User Management

Manage users and groups](https://www.algorithmshift.ai/docs/auth/users)[### Roles & Permissions

Role-based access control](https://www.algorithmshift.ai/docs/auth/roles)
