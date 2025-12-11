# Data Authorization & Security - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/data-authorization  
**Scraped:** 2025-12-10 14:04:07

**Description:** Comprehensive multi-layered security system with Row-Level Security, Organization-Wide Defaults, and principal-based access control.

---

Data Authorization & Security - AlgorithmShift Documentation | AlgorithmShiftDocumentationData Authorization & Security
# Data Authorization & Row-Level Security

AlgorithmShift's enterprise-grade, Salesforce-style multi-layered security system. Database-enforced access control that cannot be bypassed, with 5 layers of protection for your data.

### Why This System is Special

Unlike traditional application-level security, AlgorithmShift enforces access control at the database level. This means:

- Cannot be bypassed: Security is enforced by PostgreSQL, not application code
- Automatic: No manual security checks needed in your code
- Performant: Optimized at the database query level
- Flexible: 5 complementary layers for any security requirement

## The 5-Layer Security Model

AlgorithmShift's security system uses 5 complementary layers that work together to control data access:
0
### Workspace Admin Bypass

First line of evaluation

Users with workspace_admin role automatically see all data, bypassing all other layers.
Copy
```
-- If user has workspace_admin role
SELECT * FROM customers  -- Returns ALL records (no filtering)
```
1
### Organization-Wide Defaults (OWD)

Table-level default access

Each table has a default access level: Public Read/Write, Public Read Only, Private, or Controlled by Parent.

Public Read/Write

Everyone sees & edits all

Public Read Only

See all, edit own

Private

See & edit only own

Controlled by Parent

Inherit parent access
2
### Ownership

Record owner access

Users automatically have access to records they own (via owner_id field).
Copy
```
-- User can access their own records
owner_id = current_user_id()
```
3
### Group Membership

Group-based access

Users have access to records belonging to their groups (via primary_group_id and secondary_group_id).
Copy
```
-- User can access records from their groups
primary_group_id IN (SELECT group_id FROM user_groups WHERE user_id = current_user_id())
OR
secondary_group_id IN (SELECT group_id FROM user_groups WHERE user_id = current_user_id())
```
4
### Explicit Shares

Manual record sharing

Records can be explicitly shared with users, groups, or other records via sys_record_group_bindings.
Copy
```
-- User can access explicitly shared records
EXISTS (
  SELECT 1 FROM sys_record_group_bindings rgb
  WHERE rgb.entity_name = 'customers'
  AND rgb.entity_id = customers.id
  AND rgb.principal_id IN (current_user_groups())
)
```
5
### RLS Policies

Custom security rules

Custom Row-Level Security policies with conditions via sys_record_bindings.
Copy
```
-- Custom RLS policy example
region = current_user_region()
AND 
department_id = current_user_department()
AND
status IN ('active', 'pending')
```

## How Layers Combine
Copy
```
Layer 0 (Admin Bypass):
  IF user.role = 'workspace_admin' THEN
    → Return ALL records (skip other layers)
  END IF

Layer 1 (Table OWD):
  IF table.default_access = 'public_read_write' THEN
    → Return ALL records (skip layers 2-4)
  ELSE IF table.default_access = 'public_read_only' THEN
    → Return ALL records (read), apply layers 2-4 for write
  END IF

Layers 2-4 (Ownership, Groups, Shares) - Combined with OR:
  WHERE (
    owner_id = current_user                    -- Layer 2: Ownership
    OR
    primary_group_id IN (user_groups)          -- Layer 3: Groups
    OR
    secondary_group_id IN (user_groups)
    OR
    EXISTS (explicit shares)                   -- Layer 4: Shares
  )

Layer 5 (RLS Policies) - Combined with AND:
  AND (
    custom_rls_conditions                      -- Layer 5: Policies
  )
```

## Complete Example

Here's how a simple query gets transformed by the security system:

#### Your Code
Copy
```
// Simple query
SELECT * FROM customers
```

#### What Actually Executes
Copy
```
SELECT * FROM customers
WHERE (
  -- Layer 2: Ownership
  owner_id = 'user-123'
  OR
  -- Layer 3: Groups  
  primary_group_id IN ('grp-1', 'grp-2')
  OR
  secondary_group_id IN ('grp-1', 'grp-2')
  OR
  -- Layer 4: Shares
  EXISTS (
    SELECT 1 FROM sys_record_group_bindings
    WHERE entity_name = 'customers'
    AND entity_id = customers.id
    AND principal_id IN ('user-123', 'grp-1', 'grp-2')
  )
)
AND (
  -- Layer 5: RLS Policies
  region = 'US'
  AND status = 'active'
)
```

## Key Features

### Database-Enforced

Security applied by PostgreSQL, impossible to bypass through API or code

### Automatic

Universal RLS automatically applies all security layers to every query

### Multi-Layered

5 complementary layers: admin bypass, OWD, ownership, groups, shares, policies

### Principal-Based

Users, groups, and even records can be principals with access rights

### Hierarchical Groups

Nested group structures with inherited permissions

### Field-Level Security

Control access to specific columns, hide sensitive data

## Access Control Components

The system is organized into four main categories in the admin interface:

### Identity Management

- • Users - Individual accounts
- • Groups - Hierarchical organization
- • Group Types - Custom categories
- • User Types - Custom user categories

### Authorization

- • Roles - Role definitions
- • Permissions - Granular permissions
- • Record Bindings - RLS policies
- • Record Shares - Manual sharing
- • Field Permissions - Column access
- • Table Settings - OWD configuration

### API Security

- • API Keys - Key generation
- • API Resources - Endpoint protection

### Data Management

- • Tables - Schema management
- • Views - Query management
- • Data - Excel-like editing

## Learn More

Explore each component of the data authorization system:
[### Organization-Wide Defaults

Configure table-level default access modes](https://www.algorithmshift.ai/docs/data-authorization/owd)[### Ownership & Groups

Understand ownership and group-based access](https://www.algorithmshift.ai/docs/data-authorization/ownership)[### Record Sharing

Share records with users, groups, and principals](https://www.algorithmshift.ai/docs/data-authorization/sharing)[### RLS Policies

Create custom security policies](https://www.algorithmshift.ai/docs/data-authorization/rls-policies)[### Permission Sets

Deterministic UUID-based permissions](https://www.algorithmshift.ai/docs/data-authorization/permission-sets)[### Universal RLS

Automatic security injection for all queries](https://www.algorithmshift.ai/docs/data-authorization/universal-rls)[### How Access Works

Complete access evaluation flow](https://www.algorithmshift.ai/docs/data-authorization/access-flow)[### Principals

Users, groups, and records as security principals](https://www.algorithmshift.ai/docs/data-authorization/principals)[### Field Permissions

Column-level access control](https://www.algorithmshift.ai/docs/data-authorization/field-permissions)[### Real-World Examples

CRM, multi-tenant, department scenarios](https://www.algorithmshift.ai/docs/data-authorization/examples)
## Salesforce Comparison

If you're familiar with Salesforce security, here's how AlgorithmShift compares:
Salesforce FeatureAlgorithmShift EquivalentOrganization-Wide Defaults (OWD)`sys_table_settings.default_access`Role HierarchyHierarchical GroupsSharing Rules`sys_record_group_bindings`Manual SharingRecord Shares (principal-based)ProfilesRoles + Permission SetsPermission SetsPermission Sets (deterministic UUIDs)Field-Level SecurityField PermissionsRecord TypesUser Types + Group Types
