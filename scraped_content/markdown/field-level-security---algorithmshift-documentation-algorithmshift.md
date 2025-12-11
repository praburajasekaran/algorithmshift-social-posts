# Field-Level Security - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/data-authorization/field-permissions  
**Scraped:** 2025-12-10 14:04:20

**Description:** Column-level access control with read, edit, and mask permissions for sensitive data protection.

---

Field-Level Security - AlgorithmShift Documentation | AlgorithmShiftDocumentationData Authorization & Security
# Field-Level Security (FLS)

Control access to individual columns. Hide sensitive fields, mask confidential data, or make fields read-only for specific users and groups.

## What is Field-Level Security?

Field-Level Security (FLS) provides column-level access control. While RLS controls which rows users can see, FLS controls which columns they can access.

### Complementary to Row-Level Security

RLS: "Which customer records can Alice see?" → Filters rows

FLS: "Can Alice see the SSN field?" → Filters columns

## Access Levels

Field permissions support three access levels:

### none

Completely hidden

Field is completely removed from query results. User cannot see the field exists.
Copy
```
// Query result
{
  id: "123",
  name: "John",
  // ssn: HIDDEN
}
```

### read

View only / masked

User can see the field but cannot edit it. Can optionally be masked.
Copy
```
// With mask_value: true
{
  credit_card: "****-****-****-1234"
}

// With mask_value: false
{
  created_at: "2024-01-15"
}
```

### edit

Full access

User can read and write to the field (default for all fields).
Copy
```
// Full access
{
  email: "john@example.com"
}
// Can be updated
```

## sys_field_permissions Schema
Copy
```
CREATE TABLE sys_field_permissions (
  permission_id UUID PRIMARY KEY,
  workspace_id UUID NOT NULL,
  
  -- Which field this applies to
  table_name VARCHAR NOT NULL,
  column_name VARCHAR NOT NULL,
  
  -- Who this applies to (principal)
  principal_id UUID NOT NULL,        -- User, Group, or Role
  principal_type VARCHAR NOT NULL,   -- 'user', 'group', or 'role'
  
  -- Access configuration
  access_level VARCHAR NOT NULL,     -- 'none', 'read', or 'edit'
  mask_value BOOLEAN DEFAULT false,  -- Mask the value (for 'read' only)
  
  -- Metadata
  created_by UUID,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  
  UNIQUE(workspace_id, table_name, column_name, principal_id)
);
```

## Common Use Cases

### Hide PII from Regular Users
Copy
```
-- Hide SSN, DOB, and Tax ID from all workspace users
INSERT INTO sys_field_permissions 
  (permission_id, workspace_id, table_name, column_name, 
   principal_id, principal_type, access_level)
VALUES
  -- SSN field
  (gen_random_uuid(), 'workspace-123', 'customers', 'ssn',
   'role-workspace-user', 'role', 'none'),
  
  -- Date of birth
  (gen_random_uuid(), 'workspace-123', 'customers', 'date_of_birth',
   'role-workspace-user', 'role', 'none'),
  
  -- Tax ID
  (gen_random_uuid(), 'workspace-123', 'customers', 'tax_id',
   'role-workspace-user', 'role', 'none');

-- Result: Regular users see customer records but these fields are hidden
-- Admins still see everything (bypass FLS)
```

### Mask Financial Data
Copy
```
-- Allow users to see credit card exists, but mask the number
INSERT INTO sys_field_permissions 
  (permission_id, workspace_id, table_name, column_name,
   principal_id, principal_type, access_level, mask_value)
VALUES
  (gen_random_uuid(), 'workspace-123', 'payments', 'credit_card_number',
   'role-workspace-user', 'role', 'read', true),
  
  (gen_random_uuid(), 'workspace-123', 'accounts', 'bank_account',
   'role-workspace-user', 'role', 'read', true);

-- Result: 
-- Original: credit_card_number = "4532-1234-5678-9010"
-- User sees: credit_card_number = "****-****-****-9010"
```

### Read-Only Audit Fields
Copy
```
-- Make audit fields read-only for all users
INSERT INTO sys_field_permissions 
  (permission_id, workspace_id, table_name, column_name,
   principal_id, principal_type, access_level)
SELECT
  gen_random_uuid(),
  'workspace-123',
  table_name,
  column_name,
  'role-workspace-user',
  'role',
  'read'
FROM (
  VALUES 
    ('customers', 'created_at'),
    ('customers', 'created_by'),
    ('customers', 'updated_at'),
    ('customers', 'updated_by')
) AS fields(table_name, column_name);

-- Result: Users can see when/who created/updated, but cannot modify
```

### Department-Specific Fields
Copy
```
-- Only HR can see salary and performance fields
INSERT INTO sys_field_permissions 
  (permission_id, workspace_id, table_name, column_name,
   principal_id, principal_type, access_level)
VALUES
  -- Hide from non-HR
  (gen_random_uuid(), 'workspace-123', 'employees', 'salary',
   'grp-sales', 'group', 'none'),
  
  (gen_random_uuid(), 'workspace-123', 'employees', 'performance_rating',
   'grp-sales', 'group', 'none');

-- HR group members: See all employee fields
-- Sales group members: Cannot see salary or performance_rating
```

## How FLS is Applied
Copy
```
// Server-side query processing with FLS

// 1. User queries customers table
SELECT * FROM customers WHERE id = '123';

// 2. RLS filters rows (which customers)
-- Result: User can access customer 123

// 3. FLS filters columns (which fields)
-- Check sys_field_permissions for user/group/role

// 4. Apply field restrictions
{
  id: "123",
  name: "Acme Corp",
  email: "contact@acme.com",
  // ssn: REMOVED (access_level = 'none')
  created_at: "2024-01-15",  // Read-only
  created_by: "user-alice",  // Read-only
  credit_card: "****-****-****-1234"  // Masked
}

// 5. Return filtered record to user
```

## Field Permission Templates

Pre-configured templates for common FLS scenarios:
TemplateFieldsAccess LevelHide PIIssn, date_of_birth, tax_id, passportnoneMask Financialcredit_card, bank_account, salaryread (masked)Read-Only Auditcreated_at, created_by, updated_at, updated_byreadHide Admin Fieldsinternal_notes, admin_status, approval_statusnoneManager Onlyperformance_rating, disciplinary_actionsnone (for non-managers)
## Managing Field Permissions

### Field Permissions Interface

Navigate to: /{workspaceId}/access-control/authorization/field-permissions

Browse by Table

Select table and configure field permissions

Templates

Apply pre-configured permission templates

Bulk Operations

Apply same permission to multiple fields

Test Access

Preview what users will see

## Best Practices

### Field-Level Security Best Practices

✓ Use FLS for sensitive fields only

Too many field restrictions impact query performance

✓ Apply to roles/groups, not individual users

Easier to maintain as team membership changes

✓ Use templates for common patterns

PII, financial, and audit field templates ensure consistency

✓ Mask instead of hide when possible

Masking (read + mask_value) preserves UI layout vs hiding (none)

✓ Test with real user accounts

Verify field permissions work as expected before deploying

⚠️ Remember: Admins bypass FLS

workspace_admin role sees all fields regardless of FLS

## Learn More
[### Table Settings

Configure table-level security settings](https://www.algorithmshift.ai/docs/data-authorization/table-settings)[### Roles & Permissions

Assign permissions through roles](https://www.algorithmshift.ai/docs/data-authorization/roles)[### Audit & Compliance

Track field access and changes](https://www.algorithmshift.ai/docs/data-authorization/audit)
