# Record Sharing - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/data-authorization/sharing  
**Scraped:** 2025-12-10 14:04:12

**Description:** Explicit record sharing with users, groups, and principals. Layer 4 of the security model.

---

Record Sharing - AlgorithmShift Documentation | AlgorithmShiftDocumentationData Authorization & Security
# Record Sharing

Layer 4: Explicit manual sharing of records with users, groups, or other records. Grant access beyond ownership and group membership.

## What is Record Sharing?

Record sharing allows you to grant access to specific records to specific principals (users, groups, or other records), regardless of ownership or group membership.

### sys_record_group_bindings Table

All record shares are stored in the sys_record_group_bindings table. This table links records to principals with specific access levels.

## Access Levels

When sharing a record, you specify one of three access levels:

### read

View only

User can view the record but cannot edit or delete it

### read_write

View and edit

User can view and edit the record but cannot delete or share it

### manage

Full control

User can view, edit, delete, and share the record (like ownership)

## sys_record_group_bindings Schema
Copy
```
CREATE TABLE sys_record_group_bindings (
  id UUID PRIMARY KEY,
  workspace_id UUID NOT NULL,
  
  -- Which record is being shared
  entity_name VARCHAR NOT NULL,  -- Table name (e.g., "customers")
  entity_id UUID NOT NULL,       -- Record ID
  
  -- Who gets access (principal)
  principal_id UUID NOT NULL,    -- User ID, Group ID, or Record ID
  principal_type VARCHAR,         -- 'user', 'group', or 'record'
  
  -- What level of access
  access_level VARCHAR NOT NULL,  -- 'read', 'read_write', or 'manage'
  
  -- Metadata
  created_at TIMESTAMP DEFAULT NOW(),
  created_by UUID,
  
  -- Prevent duplicates
  UNIQUE(workspace_id, entity_name, entity_id, principal_id)
);
```

## Share with a User

Grant access to a specific user:
Copy
```
-- Share customer record with Bob (read-only)
INSERT INTO sys_record_group_bindings (
  id,
  workspace_id,
  entity_name,
  entity_id,
  principal_id,
  principal_type,
  access_level
) VALUES (
  gen_random_uuid(),
  'workspace-123',
  'customers',
  'customer-456',    -- The customer record being shared
  'user-bob',        -- Bob's user ID
  'user',
  'read'             -- Bob can only view
);

-- Now Bob can see this customer in his queries
SELECT * FROM customers WHERE id = 'customer-456';
-- Returns: customer-456 (Bob has explicit share)
```

## Share with a Group

Grant access to an entire group:
Copy
```
-- Share opportunity with entire Support Team (read/write)
INSERT INTO sys_record_group_bindings (
  id,
  workspace_id,
  entity_name,
  entity_id,
  principal_id,
  principal_type,
  access_level
) VALUES (
  gen_random_uuid(),
  'workspace-123',
  'opportunities',
  'opp-789',
  'grp-support',     -- Support Team group ID
  'group',
  'read_write'       -- Support Team can view and edit
);

-- All members of Support Team can now see and edit this opportunity
-- Alice (member of Support Team)
SELECT * FROM opportunities WHERE id = 'opp-789';
-- Returns: opp-789

-- Bob (member of Support Team)
UPDATE opportunities SET status = 'in_progress' WHERE id = 'opp-789';
-- Success! Bob can edit
```

## Share with a Record (Record as Principal)

Share records based on relationships (e.g., all contacts of an account):
Copy
```
-- Share contact with the parent Account record
-- Anyone who can see the Account can see this Contact
INSERT INTO sys_record_group_bindings (
  id,
  workspace_id,
  entity_name,
  entity_id,
  principal_id,
  principal_type,
  access_level
) VALUES (
  gen_random_uuid(),
  'workspace-123',
  'contacts',
  'contact-111',
  'account-222',     -- The parent Account record
  'record',
  'read'
);

-- This creates a relationship:
-- "Anyone who has access to Account 222 also has read access to Contact 111"

-- Example:
-- Alice owns Account 222 → Alice can see Contact 111
-- Bob has explicit share to Account 222 → Bob can see Contact 111
-- Charlie has NO access to Account 222 → Charlie CANNOT see Contact 111
```

## How Shares Are Applied in Queries
Copy
```
-- Layer 4: Record sharing filter (automatically applied)
SELECT * FROM customers
WHERE (
  -- Layers 0-3 (admin bypass, OWD, ownership, groups)
  ... other layers ...
  
  OR
  
  -- Layer 4: Explicit shares
  EXISTS (
    SELECT 1 FROM sys_record_group_bindings rgb
    WHERE rgb.entity_name = 'customers'
    AND rgb.entity_id = customers.id
    AND (
      -- Share with current user
      (rgb.principal_type = 'user' AND rgb.principal_id = current_user_id())
      OR
      -- Share with current user's groups
      (rgb.principal_type = 'group' AND rgb.principal_id IN (current_user_groups()))
      OR
      -- Share with records the user has access to (record as principal)
      (rgb.principal_type = 'record' AND rgb.principal_id IN (current_user_records()))
    )
  )
)
```

## Managing Shares in the UI

Share records from the admin interface:

### Record Sharing Interface

Navigate to: /{workspaceId}/access-control/authorization/record-shares

Features:

- • Select any table and record
- • Search for users or groups
- • Choose access level (read, read_write, manage)
- • View all shares for a record
- • Bulk sharing operations
- • Remove shares

## Real-World Examples

### Example 1: Cross-Department Collaboration
Copy
```
-- Scenario: Sales owns an account, but Support needs access
-- 1. Sales creates account
INSERT INTO accounts (id, name, owner_id)
VALUES ('acc-123', 'Acme Corp', 'user-sales-alice');

-- 2. Share with Support team (read_write)
INSERT INTO sys_record_group_bindings
VALUES (..., 'accounts', 'acc-123', 'grp-support', 'group', 'read_write');

-- Result:
-- ✓ Alice (owner) can see and edit
-- ✓ Sales team (via Alice's group) can see and edit
-- ✓ Support team (via explicit share) can see and edit
-- ✗ Marketing cannot see (no access)
```

### Example 2: Executive Visibility
Copy
```
-- Scenario: CEO needs to see all high-value opportunities
-- 1. Create CEO group
INSERT INTO sys_groups (id, name) VALUES ('grp-executives', 'Executives');

-- 2. Share all opportunities > $100k with Executives (read-only)
INSERT INTO sys_record_group_bindings (
  id, workspace_id, entity_name, entity_id, principal_id, principal_type, access_level
)
SELECT 
  gen_random_uuid(),
  workspace_id,
  'opportunities',
  id,
  'grp-executives',
  'group',
  'read'
FROM opportunities
WHERE amount > 100000;

-- Result: CEO can view (but not edit) all high-value deals
```

### Example 3: Hierarchical Record Access
Copy
```
-- Scenario: Account → Contacts → Notes (all follow account access)
-- 1. Alice owns Account
INSERT INTO accounts (id, name, owner_id)
VALUES ('acc-456', 'Big Corp', 'user-alice');

-- 2. Create Contact, share with Account record
INSERT INTO contacts (id, name, account_id)
VALUES ('con-789', 'John Doe', 'acc-456');

INSERT INTO sys_record_group_bindings
VALUES (..., 'contacts', 'con-789', 'acc-456', 'record', 'read_write');

-- 3. Create Note, share with Contact record
INSERT INTO notes (id, content, contact_id)
VALUES ('note-111', 'Important note', 'con-789');

INSERT INTO sys_record_group_bindings
VALUES (..., 'notes', 'note-111', 'con-789', 'record', 'read');

-- Result:
-- Alice owns Account → Can see Account
-- Alice can see Account → Can see Contact (shared with Account)
-- Alice can see Contact → Can see Note (shared with Contact)
-- Transitive access through record-as-principal!
```

## Best Practices

Use shares for exceptions

Shares are for special cases. Use OWD and groups for general access patterns.

Share with groups, not individual users

Sharing with groups is more maintainable as team membership changes.

Use record-as-principal for relationships

Parent-child relationships are perfect for record-based sharing.

Choose appropriate access levels

Use "read" for visibility, "read_write" for collaboration, "manage" rarely.

Audit shares regularly

Review sys_record_group_bindings to ensure appropriate access.

## Learn More
[### Principals Concept

Deep dive into principal-based access](https://www.algorithmshift.ai/docs/data-authorization/principals)[### Ownership & Groups

Automatic access through ownership](https://www.algorithmshift.ai/docs/data-authorization/ownership)[### How Access Works

Complete access evaluation flow](https://www.algorithmshift.ai/docs/data-authorization/access-flow)
