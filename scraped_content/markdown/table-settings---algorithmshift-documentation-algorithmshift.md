# Table Settings - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/data-authorization/table-settings  
**Scraped:** 2025-12-10 14:04:23

**Description:** Configure table-level security settings including OWD, RLS, sharing, and record-as-group features.

---

Table Settings - AlgorithmShift Documentation | AlgorithmShiftDocumentationData Authorization & Security
# Table Settings

Configure security and behavior settings for each table. Control OWD, RLS, sharing, audit tracking, and advanced record-as-group features.

## sys_table_settings Schema
Copy
```
CREATE TABLE sys_table_settings (
  id UUID PRIMARY KEY,
  workspace_id UUID NOT NULL,
  table_name VARCHAR NOT NULL,
  display_name VARCHAR,
  
  -- Organization-Wide Defaults (OWD)
  default_access VARCHAR DEFAULT 'private',
    -- 'public_read_write', 'public_read_only', 'private', 'controlled_by_parent'
  
  -- Parent Table Configuration (for controlled_by_parent)
  parent_table_name VARCHAR,
  parent_id_column VARCHAR DEFAULT 'parent_id',
  
  -- Security Toggles
  rls_enabled BOOLEAN DEFAULT true,
  sharing_enabled BOOLEAN DEFAULT true,
  manual_sharing_enabled BOOLEAN DEFAULT true,
  rls_policies_enabled BOOLEAN DEFAULT true,
  
  -- Business Entity Configuration
  is_business_entity BOOLEAN DEFAULT false,
  
  -- Record-as-Group Feature
  record_as_group BOOLEAN DEFAULT false,
  record_group_type VARCHAR,
  record_group_id_column VARCHAR,
  record_group_name_column VARCHAR,
  
  -- Audit Configuration
  track_created_by BOOLEAN DEFAULT true,
  track_created_at BOOLEAN DEFAULT true,
  track_updated_by BOOLEAN DEFAULT true,
  track_updated_at BOOLEAN DEFAULT true,
  
  -- Metadata
  access_description TEXT,
  created_by UUID,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_by UUID,
  updated_at TIMESTAMP DEFAULT NOW(),
  
  UNIQUE(workspace_id, table_name)
);
```

## Key Settings

### default_access

Organization-Wide Default access level (Layer 1)
`public_read_write` - Everyone sees and edits all`public_read_only` - See all, edit yours`private` - See and edit only yours`controlled_by_parent` - Inherit from parent
### rls_enabled

Enable or disable Row-Level Security for this table
Copy
```
true  → Apply all 5 security layers
false → No security (admin-only access)
```

⚠️ Disabling RLS makes table admin-only

### sharing_enabled

Allow records to be shared with users/groups
Copy
```
true  → Layer 4 (shares) active
false → No manual sharing allowed
```

### rls_policies_enabled

Apply custom RLS policies from sys_record_bindings
Copy
```
true  → Layer 5 (RLS policies) active
false → Skip custom policies
```

## Record-as-Group Feature

Advanced feature: Treat each record as a security principal (group). Anyone who has access to the record automatically becomes a "member" of that record-group.

### Use Case: Branch-Based Access
Copy
```
-- Configure branches table as record-as-group
UPDATE sys_table_settings
SET 
  record_as_group = true,
  record_group_type = 'branch',
  record_group_id_column = 'id',
  record_group_name_column = 'branch_name'
WHERE table_name = 'branches';

-- Now each branch record acts as a group!
-- Branch: "San Francisco HQ" (id: branch-sf)
-- Branch: "New York Office" (id: branch-ny)

-- User Alice has access to branch-sf
-- → Alice is automatically in "branch-sf" group
-- → Any record with primary_group_id = 'branch-sf' is accessible to Alice

-- Example: Assign customer to a branch
INSERT INTO customers (id, name, primary_group_id)
VALUES ('cust-123', 'Acme Corp', 'branch-sf');

-- Result: Everyone with access to SF branch can see this customer
```

## Audit Tracking Configuration

#### track_created_by / track_created_at

Automatically populate created_by and created_at on INSERT
Copy
```
INSERT INTO customers (name)
VALUES ('Acme');
-- Automatically adds:
-- created_by = current_user_id()
-- created_at = NOW()
```

#### track_updated_by / track_updated_at

Automatically update updated_by and updated_at on UPDATE
Copy
```
UPDATE customers
SET name = 'Acme Corp';
-- Automatically updates:
-- updated_by = current_user_id()
-- updated_at = NOW()
```

## Configuring Table Settings
Copy
```
-- Create/update table settings
INSERT INTO sys_table_settings (
  id,
  workspace_id,
  table_name,
  display_name,
  default_access,
  rls_enabled,
  sharing_enabled,
  manual_sharing_enabled,
  rls_policies_enabled,
  is_business_entity,
  track_created_by,
  track_updated_by
) VALUES (
  gen_random_uuid(),
  'workspace-123',
  'opportunities',
  'Sales Opportunities',
  'private',              -- Private by default
  true,                   -- RLS enabled
  true,                   -- Sharing enabled
  true,                   -- Manual sharing enabled
  true,                   -- RLS policies enabled
  true,                   -- Business entity
  true,                   -- Track who created
  true                    -- Track who updated
)
ON CONFLICT (workspace_id, table_name)
DO UPDATE SET
  default_access = EXCLUDED.default_access,
  rls_enabled = EXCLUDED.rls_enabled,
  sharing_enabled = EXCLUDED.sharing_enabled,
  updated_at = NOW();
```

## Common Configurations

### Customer/Account Tables (CRM)
Copy
```
default_access: 'private'
rls_enabled: true
sharing_enabled: true
manual_sharing_enabled: true
rls_policies_enabled: true
is_business_entity: true
record_as_group: false

→ Secure, shareable, with full RLS
```

### Reference Data Tables
Copy
```
default_access: 'public_read_write'
rls_enabled: false
sharing_enabled: false
manual_sharing_enabled: false
rls_policies_enabled: false
is_business_entity: false

→ Everyone can read/write, no security needed
```

### Branch/Department Tables (Record-as-Group)
Copy
```
default_access: 'private'
rls_enabled: true
sharing_enabled: true
record_as_group: true
record_group_type: 'branch'
record_group_id_column: 'id'
record_group_name_column: 'name'

→ Each record is a group for hierarchical access
```

### Child Records (Controlled by Parent)
Copy
```
default_access: 'controlled_by_parent'
parent_table_name: 'orders'
parent_id_column: 'order_id'
rls_enabled: true
sharing_enabled: false

→ Inherits access from parent orders table
```

## Managing Settings in UI

### Table Settings Interface

Navigate to: /{workspaceId}/access-control/authorization/table-settings

Browse Tables

View all tables with current settings

Edit Settings

Modal with all configuration options

Security Summary

View active security layers per table

Bulk Configuration

Apply settings to multiple tables

## Learn More
[### Organization-Wide Defaults

Understand default_access modes](https://www.algorithmshift.ai/docs/data-authorization/owd)[### RLS Policies

Configure custom security rules](https://www.algorithmshift.ai/docs/data-authorization/rls-policies)[### Record Sharing

Manual sharing configuration](https://www.algorithmshift.ai/docs/data-authorization/sharing)
