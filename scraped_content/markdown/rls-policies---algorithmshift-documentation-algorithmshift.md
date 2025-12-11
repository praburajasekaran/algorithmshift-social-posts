# RLS Policies - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/data-authorization/rls-policies  
**Scraped:** 2025-12-10 14:04:13

**Description:** Create custom Row-Level Security policies with conditions. Layer 5 of the security model.

---

RLS Policies - AlgorithmShift Documentation | AlgorithmShiftDocumentationData Authorization & Security
# RLS Policies (Row-Level Security)

Layer 5: Custom security rules with conditions. Create fine-grained access policies that go beyond ownership, groups, and shares.

## What are RLS Policies?

RLS Policies (stored in sys_record_bindings) are custom security rules that add additional WHERE conditions to queries. Unlike layers 2-4 which use OR logic to expand access, RLS policies use AND logic to restrict access.

### Key Difference from Other Layers

Layers 2-4 (ownership, groups, shares) use OR logic - they add more records you can see.

Layer 5 (RLS policies) uses AND logic - they remove records, even if you have access via other layers.

## sys_record_bindings Schema
Copy
```
CREATE TABLE sys_record_bindings (
  id UUID PRIMARY KEY,
  workspace_id UUID NOT NULL,
  
  -- Which table this policy applies to
  entity_name VARCHAR NOT NULL,  -- Table name (e.g., "opportunities")
  
  -- Who this policy applies to
  principal_id UUID,             -- User, Group, or null (all users)
  principal_type VARCHAR,         -- 'user', 'group', or null
  
  -- The policy condition (SQL WHERE clause)
  condition TEXT NOT NULL,        -- e.g., "region = current_user_region()"
  
  -- Policy metadata
  name VARCHAR,
  description TEXT,
  is_active BOOLEAN DEFAULT true,
  
  created_at TIMESTAMP DEFAULT NOW(),
  created_by UUID
);
```

## RLS Functions

Use built-in functions in your RLS conditions:
FunctionReturnsDescription`current_user_id()`UUIDCurrent user's ID`current_user_email()`VARCHARCurrent user's email`current_user_groups()`UUID[]Array of user's group IDs`current_user_region()`VARCHARUser's region (custom field)`current_user_department()`VARCHARUser's department (custom field)`current_workspace_id()`UUIDCurrent workspace ID`is_workspace_admin()`BOOLEANTrue if user is workspace admin
## Creating RLS Policies

### Example 1: Regional Access

Users can only see opportunities in their region:
Copy
```
-- Create RLS policy for regional access
INSERT INTO sys_record_bindings (
  id,
  workspace_id,
  entity_name,
  principal_id,     -- null = applies to all users
  principal_type,   -- null = applies to all users
  condition,
  name,
  is_active
) VALUES (
  gen_random_uuid(),
  'workspace-123',
  'opportunities',
  null,             -- Apply to ALL users
  null,
  'region = current_user_region()',  -- The condition
  'Regional Access Policy',
  true
);

-- Now all queries are filtered by region
-- User Alice (region = 'US')
SELECT * FROM opportunities;
-- Returns: Only opportunities where region = 'US'

-- User Bob (region = 'EU')
SELECT * FROM opportunities;
-- Returns: Only opportunities where region = 'EU'
```

### Example 2: Department Restrictions

Users can only see records from their department:
Copy
```
-- Department-based policy
INSERT INTO sys_record_bindings (
  id,
  workspace_id,
  entity_name,
  condition,
  name
) VALUES (
  gen_random_uuid(),
  'workspace-123',
  'projects',
  'department_id = current_user_department_id()',
  'Department Access Policy'
);

-- Result: Users only see projects from their department
```

### Example 3: Status-Based Visibility

Regular users can only see active records:
Copy
```
-- Status policy (only for non-admins)
INSERT INTO sys_record_bindings (
  id,
  workspace_id,
  entity_name,
  condition,
  name
) VALUES (
  gen_random_uuid(),
  'workspace-123',
  'customers',
  'status IN (''active'', ''pending'') OR is_workspace_admin()',
  'Active Records Only Policy'
);

-- Regular users: Only see active/pending customers
-- Admins: See all customers (bypass via is_workspace_admin())
```

### Example 4: Complex Multi-Condition Policy
Copy
```
-- Multi-condition policy
INSERT INTO sys_record_bindings (
  id,
  workspace_id,
  entity_name,
  condition,
  name
) VALUES (
  gen_random_uuid(),
  'workspace-123',
  'opportunities',
  $$(
    region = current_user_region()
    AND 
    (
      amount < 10000  -- Small deals visible to all
      OR 
      created_by = current_user_id()  -- Or deals you created
      OR
      primary_group_id IN (current_user_groups())  -- Or your team's deals
    )
    AND
    status != 'archived'  -- Never show archived
  )$$,
  'Complex Opportunity Policy'
);
```

## Group-Specific Policies

Apply policies to specific groups only:
Copy
```
-- Policy that only applies to Sales Team
INSERT INTO sys_record_bindings (
  id,
  workspace_id,
  entity_name,
  principal_id,
  principal_type,
  condition,
  name
) VALUES (
  gen_random_uuid(),
  'workspace-123',
  'accounts',
  'grp-sales',    -- Only applies to Sales Team
  'group',
  'account_type = ''prospect'' OR account_type = ''customer''',
  'Sales Team Account Type Policy'
);

-- Sales Team members: See only prospects and customers
-- Other users: See all account types (policy doesn't apply)
-- Admins: See all accounts (bypass)
```

## How RLS Policies Are Applied
Copy
```
-- Complete query transformation with all 5 layers
SELECT * FROM opportunities

-- Transformed to:
SELECT * FROM opportunities
WHERE (
  -- Layer 0: Admin bypass
  is_workspace_admin()
  
  OR
  
  (
    -- Layers 2-4: Ownership, Groups, Shares (OR logic)
    (
      owner_id = current_user_id()
      OR
      primary_group_id IN (current_user_groups())
      OR
      EXISTS (explicit shares)
    )
    
    AND
    
    -- Layer 5: RLS Policies (AND logic - restricts access)
    (
      region = current_user_region()  -- Policy 1
      AND
      status IN ('active', 'pending')  -- Policy 2
      AND
      ... (other active policies)
    )
  )
)
```

## Visual Builder for RLS Policies

Create policies using the visual interface:

### RLS Policy Builder

Navigate to: /{workspaceId}/access-control/authorization/record-bindings

Visual Condition Builder

Drag-and-drop interface for building conditions

Function Reference

Browse and insert RLS functions

Test Policies

Preview what data users will see

Policy Templates

Common policy patterns

## Best Practices

### RLS Policy Best Practices

✓ Keep policies simple

Complex policies impact query performance

✓ Use indexed columns in conditions

Create indexes on region, department_id, status, etc.

✓ Test policies thoroughly

Verify they don't accidentally hide too much or too little data

✓ Document policy purpose

Use descriptive names and descriptions

✓ Combine with OWD for efficiency

Use OWD=Private + RLS policies instead of just policies

⚠️ Remember: AND logic restricts

RLS policies can hide records you own or have been shared

## Learn More
[### Universal RLS

How RLS is automatically applied](https://www.algorithmshift.ai/docs/data-authorization/universal-rls)[### How Access Works

Complete access evaluation flow](https://www.algorithmshift.ai/docs/data-authorization/access-flow)[### Table Settings

Enable/disable RLS per table](https://www.algorithmshift.ai/docs/data-authorization/table-settings)
