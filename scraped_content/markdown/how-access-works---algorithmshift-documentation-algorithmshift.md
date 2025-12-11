# How Access Works - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/data-authorization/access-flow  
**Scraped:** 2025-12-10 14:04:17

**Description:** Complete access evaluation flow showing how all 5 security layers combine to determine record access.

---

How Access Works - AlgorithmShift Documentation | AlgorithmShiftDocumentationData Authorization & Security
# How Access Works

Complete step-by-step evaluation flow showing how AlgorithmShift's 5-layer security model determines which records a user can access.

## The Complete Access Evaluation Flow
0
### Layer 0: Admin Bypass Check

First evaluation - highest priority
Copy
```
IF user.role = 'workspace_admin' THEN
  -- Return ALL records (no filtering)
  RETURN query_without_security
ELSE
  -- Continue to layers 1-5
  GOTO Layer_1
END IF
```

Result: Admins see everything, skip all other layers
1
### Layer 1: Organization-Wide Defaults (OWD)

Table-level baseline access
Copy
```
table_settings = GET table_settings WHERE table_name = 'customers'

IF table_settings.default_access = 'public_read_write' THEN
  -- Return ALL records (no filtering)
  RETURN query_without_layers_2_to_5
  
ELSE IF table_settings.default_access = 'public_read_only' THEN
  -- For READ: Return ALL records
  -- For WRITE/DELETE: Continue to layers 2-5
  IF operation = 'SELECT' THEN
    RETURN query_without_layers_2_to_5
  ELSE
    GOTO Layer_2
  END IF
  
ELSE
  -- Private or controlled_by_parent
  GOTO Layer_2
END IF
```

Result: Public access modes may skip layers 2-4
2-4
### Layers 2-4: Ownership + Groups + Shares (OR Logic)

Combine with OR - expand access
Copy
```
-- Build WHERE clause with OR conditions
WHERE (
  -- Layer 2: Ownership
  owner_id = current_user_id()
  OR
  owner_id IN (SELECT group_id FROM user_groups 
               WHERE user_id = current_user_id())
  
  OR
  
  -- Layer 3: Primary Group
  primary_group_id IN (
    SELECT group_id FROM user_groups_hierarchy 
    WHERE user_id = current_user_id()
  )
  
  OR
  
  -- Layer 3: Secondary Group
  secondary_group_id IN (
    SELECT group_id FROM user_groups_hierarchy 
    WHERE user_id = current_user_id()
  )
  
  OR
  
  -- Layer 4: Explicit Shares
  EXISTS (
    SELECT 1 FROM sys_record_group_bindings rgb
    WHERE rgb.entity_name = 'customers'
    AND rgb.entity_id = customers.id
    AND rgb.principal_id IN (current_user_principals())
    AND rgb.access_level IN ('read', 'read_write', 'manage')
  )
)

-- Continue to Layer 5
GOTO Layer_5
```

Result: User can see records from ANY of these conditions
5
### Layer 5: RLS Policies (AND Logic)

Custom rules - restrict access
Copy
```
-- Get active RLS policies for table
policies = SELECT condition FROM sys_record_bindings
           WHERE entity_name = 'customers'
           AND is_active = true
           AND (principal_id IS NULL 
                OR principal_id IN (current_user_principals()))

-- Apply each policy with AND logic
AND (policy_1_condition)  -- e.g., region = current_user_region()
AND (policy_2_condition)  -- e.g., status IN ('active', 'pending')
AND (policy_N_condition)

-- Return final filtered records
RETURN records
```

Result: Records must pass ALL RLS policy conditions

## Complete SQL Example

#### What You Write
Copy
```
SELECT * 
FROM customers 
WHERE name LIKE 'A%';
```

#### What Actually Executes
Copy
```
SELECT * 
FROM customers 
WHERE name LIKE 'A%'

-- Layer 0: Admin bypass
AND (
  is_workspace_admin()
  OR
  (
    -- Layers 2-4: OR logic
    (
      owner_id = 'user-alice'
      OR
      primary_group_id IN ('grp-1', 'grp-2')
      OR
      secondary_group_id IN ('grp-1', 'grp-2')
      OR
      EXISTS (...)  -- shares
    )
    
    -- Layer 5: AND logic
    AND region = 'US'
    AND status = 'active'
  )
);
```

## Real-World Scenario
Copy
```
Scenario: Alice queries customer table

User: Alice (user-alice)
Role: workspace_user
Groups: ['grp-sales-team', 'grp-east-region']
Region: 'US'

Table: customers
  default_access: 'private'
  
RLS Policies:
  1. region = current_user_region()
  2. status IN ('active', 'pending')

Records in Database:
  Customer A: owner_id='user-alice', region='US', status='active'
  Customer B: owner_id='user-bob', region='US', status='active'  
  Customer C: owner_id='user-bob', primary_group_id='grp-sales-team', region='US', status='active'
  Customer D: owner_id='user-bob', primary_group_id='grp-west-team', region='US', status='active'
  Customer E: owner_id='user-alice', region='EU', status='active'
  Customer F: owner_id='user-alice', region='US', status='archived'

Evaluation:

Layer 0 (Admin Bypass):
  → Alice is NOT admin, continue to Layer 1

Layer 1 (OWD):
  → default_access = 'private', continue to Layers 2-4

Layers 2-4 (Ownership/Groups/Shares - OR):
  Customer A: ✓ owner_id matches Alice
  Customer B: ✗ No match
  Customer C: ✓ primary_group_id = 'grp-sales-team' (Alice is member)
  Customer D: ✗ primary_group_id = 'grp-west-team' (Alice not member)
  Customer E: ✓ owner_id matches Alice
  Customer F: ✓ owner_id matches Alice
  
  Passed Layer 2-4: A, C, E, F

Layer 5 (RLS Policies - AND):
  Policy 1: region = 'US'
    Customer A: ✓ region='US'
    Customer C: ✓ region='US'
    Customer E: ✗ region='EU' ← BLOCKED
    Customer F: ✓ region='US'
  
  Policy 2: status IN ('active', 'pending')
    Customer A: ✓ status='active'
    Customer C: ✓ status='active'
    Customer F: ✗ status='archived' ← BLOCKED
  
FINAL RESULT: Alice sees Customers A and C only
```

## Decision Tree Visualization
Copy
```
                         [Query Start]
                              |
                    [Layer 0: Admin?]
                    /              \
                 YES                NO
                  |                  |
          [Return ALL]      [Layer 1: OWD]
                            /       |        \
              public_r_w  public_r  private/controlled
                    |        |             |
             [Return ALL] [Read: ALL]  [Layer 2-4]
                          [Write: →]     (OR Logic)
                                   |          |
                                   |    [Ownership?]
                                   |    [Groups?]
                                   |    [Shares?]
                                   |          |
                                   ←----------+
                                   |
                          [Layer 5: RLS]
                           (AND Logic)
                                   |
                          [Return Filtered]
```

## Performance Considerations

### Optimizations

- • Admin bypass at query start (no filtering needed)
- • OWD can skip layers 2-4 for public tables
- • Indexes on owner_id, primary_group_id, secondary_group_id
- • User's groups cached in session
- • RLS policies compiled once, reused

### Database Level

- • All filtering happens in PostgreSQL
- • Query planner optimizes combined conditions
- • No application-level loops
- • Single database roundtrip
- • Scales to millions of records

## Learn More
[### Universal RLS

How security is automatically injected](https://www.algorithmshift.ai/docs/data-authorization/universal-rls)[### OWD

Organization-Wide Defaults detail](https://www.algorithmshift.ai/docs/data-authorization/owd)[### Real-World Examples

Complete scenarios and use cases](https://www.algorithmshift.ai/docs/data-authorization/examples)
