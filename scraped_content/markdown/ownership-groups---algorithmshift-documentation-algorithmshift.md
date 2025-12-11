# Ownership & Groups - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/data-authorization/ownership  
**Scraped:** 2025-12-10 14:04:10

**Description:** Record ownership, group membership, and hierarchical access control through owner_id, primary_group_id, and secondary_group_id fields.

---

Ownership & Groups - AlgorithmShift Documentation | AlgorithmShiftDocumentationData Authorization & Security
# Ownership & Groups

Layers 2 and 3 of the security model: ownership-based and group-based access control. These automatic mechanisms grant access based on record fields.

## The Three Key Fields

Every table can have three special fields that control access:

### owner_id

UUID reference to the user or group who owns this record

Layer 2: Ownership

### primary_group_id

UUID reference to the primary group that has access

Layer 3: Groups

### secondary_group_id

UUID reference to a secondary group for additional access

Layer 3: Groups

## Layer 2: Ownership (owner_id)

Records with an owner_id field automatically grant full access to the owner.

### How Ownership Works

Automatic Access

If owner_id matches your user ID, you automatically have access

Full Control

Owners can read, update, and delete their records

Group Ownership

owner_id can reference a group; all group members get access
Copy
```
-- Ownership filter (automatically applied)
WHERE owner_id = current_user_id()

-- If owner_id is a group
WHERE owner_id IN (SELECT group_id FROM user_groups WHERE user_id = current_user_id())
```

### Example: Customer Records
Copy
```
-- Create a customer record
INSERT INTO customers (id, name, owner_id)
VALUES (
  '123e4567-e89b-12d3-a456-426614174000',
  'Acme Corp',
  'user-alice-uuid'  -- Alice owns this customer
);

-- Alice's query (automatically filtered)
SELECT * FROM customers;
-- Returns: Acme Corp (and any other records Alice owns)

-- Bob's query (different user)
SELECT * FROM customers;
-- Returns: Nothing (unless Bob has access through other layers)
```

## Layer 3: Group Membership

Records with primary_group_id or secondary_group_id grant access to all group members.

### Group Access Pattern
Copy
```
-- Group membership filter (automatically applied)
WHERE 
  primary_group_id IN (
    SELECT group_id FROM user_groups WHERE user_id = current_user_id()
  )
  OR
  secondary_group_id IN (
    SELECT group_id FROM user_groups WHERE user_id = current_user_id()
  )
```

### Example: Sales Team Records
Copy
```
-- Setup: Alice and Bob are in "Sales Team" group
INSERT INTO sys_groups (id, name) VALUES ('grp-sales', 'Sales Team');
INSERT INTO sys_user_groups (user_id, group_id) VALUES 
  ('user-alice', 'grp-sales'),
  ('user-bob', 'grp-sales');

-- Create an opportunity for the Sales Team
INSERT INTO opportunities (id, name, primary_group_id)
VALUES (
  'opp-123',
  'Big Deal',
  'grp-sales'  -- Assigned to Sales Team
);

-- Alice's query
SELECT * FROM opportunities;
-- Returns: Big Deal (Alice is in Sales Team)

-- Bob's query
SELECT * FROM opportunities;
-- Returns: Big Deal (Bob is also in Sales Team)

-- Charlie's query (not in Sales Team)
SELECT * FROM opportunities;
-- Returns: Nothing (unless Charlie has access through other layers)
```

## Hierarchical Groups

Groups can have parent-child relationships. Members of child groups automatically inherit access from parent groups.
Copy
```
-- Group hierarchy
Company (grp-company)
└── Sales Department (grp-sales) [parent: grp-company]
    ├── East Region (grp-east) [parent: grp-sales]
    │   └── Team A (grp-team-a) [parent: grp-east]
    └── West Region (grp-west) [parent: grp-sales]

-- User memberships
Alice → Member of "Team A"
Bob → Member of "East Region"
Charlie → Member of "Sales Department"

-- Record assigned to "Sales Department"
INSERT INTO opportunities (id, name, primary_group_id)
VALUES ('opp-456', 'Enterprise Deal', 'grp-sales');

-- Who can see this opportunity?
✓ Alice (via Team A → East Region → Sales Department)
✓ Bob (via East Region → Sales Department)
✓ Charlie (direct member of Sales Department)
✗ Diana (not in hierarchy)

-- Hierarchy function (automatically applied)
current_user_groups_with_hierarchy()
-- Returns: ['grp-team-a', 'grp-east', 'grp-sales', 'grp-company'] for Alice
```

## Primary vs Secondary Group

Why two group fields? Different use cases and flexibility.

#### primary_group_id

Main organizational group

- • Department or team
- • Primary ownership group
- • Default assignment
- • Used for reporting

Example: "Sales Department"

#### secondary_group_id

Secondary access group

- • Cross-functional team
- • Project group
- • Temporary assignment
- • Additional collaborators

Example: "Project Phoenix"

## Combined Example

Ownership and groups work together with OR logic:
Copy
```
-- Complete filter for Layers 2 & 3
SELECT * FROM opportunities
WHERE (
  -- Layer 2: Ownership
  owner_id = current_user_id()
  OR
  owner_id IN (current_user_groups())
  
  OR
  
  -- Layer 3: Primary Group
  primary_group_id IN (current_user_groups_with_hierarchy())
  
  OR
  
  -- Layer 3: Secondary Group
  secondary_group_id IN (current_user_groups_with_hierarchy())
)
-- Plus other layers (OWD, shares, RLS policies)

-- Real scenario:
Alice is user 'user-alice'
Alice is in groups: ['grp-team-a', 'grp-east', 'grp-sales']

Opportunity #1:
  owner_id: 'user-alice'
  ✓ Alice can see (Layer 2: owner)

Opportunity #2:
  owner_id: 'user-bob'
  primary_group_id: 'grp-sales'
  ✓ Alice can see (Layer 3: Alice in grp-sales)

Opportunity #3:
  owner_id: 'user-bob'
  primary_group_id: 'grp-west'
  secondary_group_id: 'grp-team-a'
  ✓ Alice can see (Layer 3: Alice in grp-team-a via secondary)

Opportunity #4:
  owner_id: 'user-charlie'
  primary_group_id: 'grp-west'
  ✗ Alice CANNOT see (no matching layer)
```

## Best Practices

### Ownership & Group Best Practices

✓ Use owner_id for individual ownership

Assign records to individual users who are responsible for them

✓ Use primary_group_id for team access

Share records with entire teams or departments automatically

✓ Use secondary_group_id for cross-functional work

Grant access to project teams or temporary collaborators

✓ Leverage group hierarchies

Organize groups in a tree structure for automatic access inheritance

✓ Combine with OWD for baseline security

Set table OWD to "private", then use groups to grant team access

## Learn More
[### Identity Management

Create and manage users and groups](https://www.algorithmshift.ai/docs/data-authorization/identity)[### Record Sharing

Explicit sharing beyond ownership](https://www.algorithmshift.ai/docs/data-authorization/sharing)[### Organization-Wide Defaults

Set baseline table access levels](https://www.algorithmshift.ai/docs/data-authorization/owd)
