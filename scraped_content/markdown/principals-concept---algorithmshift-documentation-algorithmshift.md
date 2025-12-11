# Principals Concept - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/data-authorization/principals  
**Scraped:** 2025-12-10 14:04:18

**Description:** Users, groups, and records as security principals. The foundation of AlgorithmShift's flexible access control.

---

Principals Concept - AlgorithmShift Documentation | AlgorithmShiftDocumentationData Authorization & Security
# Principals Concept

In AlgorithmShift, a "principal" is any entity that can own data, have permissions, or be granted access. Users, groups, and even records can be principals.

### What is a Principal?

A principal is an entity that can participate in the security system. Think of it as "who or what" in "who has access to what". AlgorithmShift supports three types of principals.

## The Three Types of Principals

### User Principal

Individual accounts

A user is the most common principal type

- • Can own records
- • Can be assigned permissions
- • Can have records shared with them
- • Can belong to groups

### Group Principal

Collections of users

Groups can act as principals themselves

- • Can own records
- • Can have records shared with them
- • All members inherit access
- • Hierarchical relationships

### Record Principal

Records as groups

Records can act as implicit groups

- • Account → implicit group
- • Related records auto-shared
- • Hierarchical access
- • Parent-child relationships

## User as Principal
Copy
```
-- User owns a customer record
INSERT INTO customers (id, name, owner_id)
VALUES ('cust-123', 'Acme Corp', 'user-alice');

-- User Alice can access this customer via ownership (Layer 2)

-- Record is shared with user Bob
INSERT INTO sys_record_group_bindings (
  entity_name, entity_id, principal_id, principal_type, access_level
) VALUES (
  'customers', 'cust-123', 'user-bob', 'user', 'read'
);

-- User Bob can now access via sharing (Layer 4)
```

## Group as Principal

Groups can own records and have records shared with them:
Copy
```
-- Group owns a record
INSERT INTO opportunities (id, name, owner_id)
VALUES ('opp-456', 'Big Deal', 'grp-sales-team');

-- ALL members of Sales Team can access via ownership
-- Alice (member of Sales Team) → Can access
-- Bob (member of Sales Team) → Can access
-- Charlie (NOT in Sales Team) → Cannot access

-- Record is shared with Engineering group
INSERT INTO sys_record_group_bindings (
  entity_name, entity_id, principal_id, principal_type, access_level
) VALUES (
  'opportunities', 'opp-456', 'grp-engineering', 'group', 'read'
);

-- Now ALL members of Engineering can read via sharing (Layer 4)
```

## Record as Principal (Advanced)

Records can act as implicit groups, enabling hierarchical access patterns:

### Example: Account Hierarchy
Copy
```
-- Alice owns Account "Acme Corp"
INSERT INTO accounts (id, name, owner_id)
VALUES ('acc-123', 'Acme Corp', 'user-alice');

-- Contact is "shared with" the Account record (record-as-principal)
INSERT INTO contacts (id, name, account_id)
VALUES ('con-456', 'John Doe', 'acc-123');

INSERT INTO sys_record_group_bindings (
  entity_name, entity_id, 
  principal_id, principal_type, access_level
) VALUES (
  'contacts', 'con-456',
  'acc-123', 'record', 'read_write'  -- Account is the principal!
);

-- Result: Anyone who can access Account acc-123 can also access Contact con-456
-- Alice owns Account → Alice can access Contact
-- If Bob is granted access to Account → Bob can access Contact too
-- Transitive access through record-as-principal!
```

### Example: Multi-Level Hierarchy
Copy
```
-- Three-level hierarchy: Account → Contact → Note
-- 1. Alice owns Account
INSERT INTO accounts VALUES ('acc-1', 'Acme', 'user-alice');

-- 2. Contact shared with Account (record-as-principal)
INSERT INTO contacts VALUES ('con-1', 'John', 'acc-1');
INSERT INTO sys_record_group_bindings VALUES
  ('contacts', 'con-1', 'acc-1', 'record', 'read_write');

-- 3. Note shared with Contact (record-as-principal)
INSERT INTO notes VALUES ('note-1', 'Important', 'con-1');
INSERT INTO sys_record_group_bindings VALUES
  ('notes', 'note-1', 'con-1', 'record', 'read');

-- Access Chain:
-- Alice owns Account acc-1
-- → Alice can access Contact con-1 (shared with acc-1)
-- → Alice can access Note note-1 (shared with con-1)

-- If Bob is granted access to the Account:
-- Bob gets access to Account → Contact → Note
-- Entire hierarchy cascades!
```

## Principal Resolution

How the system determines which principals a user belongs to:
Copy
```
-- Function: current_user_principals()
-- Returns all principal IDs the current user belongs to

CREATE FUNCTION current_user_principals() 
RETURNS UUID[] AS $$
  SELECT ARRAY(
    -- 1. User themselves
    SELECT current_user_id()
    
    UNION
    
    -- 2. All groups user belongs to (with hierarchy)
    SELECT group_id 
    FROM user_groups_hierarchy 
    WHERE user_id = current_user_id()
    
    UNION
    
    -- 3. All records user has access to (via ownership or sharing)
    SELECT DISTINCT entity_id::uuid
    FROM accessible_records
    WHERE user_id = current_user_id()
  );
$$ LANGUAGE SQL STABLE;

-- Usage in sharing check
SELECT * FROM customers
WHERE EXISTS (
  SELECT 1 FROM sys_record_group_bindings rgb
  WHERE rgb.entity_name = 'customers'
  AND rgb.entity_id = customers.id
  AND rgb.principal_id IN (current_user_principals())  -- Check all principals
);
```

## Benefits of Principal-Based Access

### Flexibility

- • Share with users, groups, or records
- • Create complex hierarchies
- • Model real-world organizations
- • Support multi-tenant scenarios

### Maintainability

- • Change group membership → access updates automatically
- • No need to reshare individual records
- • Hierarchies propagate changes
- • Single source of truth

### Scalability

- • Efficient database queries
- • Works with millions of records
- • Indexed principal lookups
- • Cached principal resolution

### Intuitive

- • Mirrors real-world relationships
- • "Give Sales Team access to Account"
- • Natural parent-child access
- • Matches user mental models

## Learn More
[### Identity Management

Create users and groups](https://www.algorithmshift.ai/docs/data-authorization/identity)[### Record Sharing

Share with principals](https://www.algorithmshift.ai/docs/data-authorization/sharing)[### Ownership & Groups

How principals grant access](https://www.algorithmshift.ai/docs/data-authorization/ownership)
