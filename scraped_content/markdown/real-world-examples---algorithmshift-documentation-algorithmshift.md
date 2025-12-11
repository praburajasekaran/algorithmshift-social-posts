# Real-World Examples - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/data-authorization/examples  
**Scraped:** 2025-12-10 14:04:21

**Description:** Complete real-world scenarios showing how to implement data authorization for CRM, multi-tenant SaaS, healthcare, and more.

---

Real-World Examples - AlgorithmShift Documentation | AlgorithmShiftDocumentationData Authorization & Security
# Real-World Examples

Complete implementation scenarios showing how to configure AlgorithmShift's security system for common use cases.
[### CRM System

Sales teams, territories, account hierarchies](https://www.algorithmshift.ai/docs/data-authorization/examples#crm)[### Multi-Tenant SaaS

Complete tenant isolation](https://www.algorithmshift.ai/docs/data-authorization/examples#saas)[### Healthcare

HIPAA compliance, PHI protection](https://www.algorithmshift.ai/docs/data-authorization/examples#healthcare)[### Education Platform

Students, teachers, courses](https://www.algorithmshift.ai/docs/data-authorization/examples#education)[### E-Commerce

Orders, customers, inventory](https://www.algorithmshift.ai/docs/data-authorization/examples#ecommerce)[### Enterprise ERP

Departments, branches, complex hierarchies](https://www.algorithmshift.ai/docs/data-authorization/examples#enterprise)
## Example 1: CRM System

Sales CRM with territories, account hierarchies, and opportunity management.

### Step 1: Group Structure
Copy
```
-- Create hierarchical sales organization
INSERT INTO sys_groups (id, name, parent_group_id, group_type_id) VALUES
  ('grp-sales', 'Sales Department', null, 'dept'),
  ('grp-na', 'North America', 'grp-sales', 'region'),
  ('grp-east', 'East Region', 'grp-na', 'region'),
  ('grp-west', 'West Region', 'grp-na', 'region'),
  ('grp-eu', 'Europe', 'grp-sales', 'region');

-- Add users to groups
INSERT INTO sys_user_groups (user_id, group_id) VALUES
  ('user-alice', 'grp-east'),  -- Alice in East
  ('user-bob', 'grp-west'),    -- Bob in West
  ('user-charlie', 'grp-eu');  -- Charlie in EU
```

### Step 2: Table Settings
Copy
```
-- Accounts: Private (sales rep ownership)
UPDATE sys_table_settings SET
  default_access = 'private',
  rls_enabled = true,
  sharing_enabled = true
WHERE table_name = 'accounts';

-- Opportunities: Private
UPDATE sys_table_settings SET
  default_access = 'private'
WHERE table_name = 'opportunities';

-- Contacts: Controlled by parent (follow account)
UPDATE sys_table_settings SET
  default_access = 'controlled_by_parent',
  parent_table_name = 'accounts',
  parent_id_column = 'account_id'
WHERE table_name = 'contacts';

-- Products: Public read-only
UPDATE sys_table_settings SET
  default_access = 'public_read_only'
WHERE table_name = 'products';
```

### Step 3: RLS Policy (Territory-Based)
Copy
```
-- Users can only see accounts in their territory
INSERT INTO sys_record_bindings (
  id, workspace_id, entity_name, condition, name
) VALUES (
  gen_random_uuid(),
  'workspace-123',
  'accounts',
  'territory = current_user_territory()',
  'Territory-Based Access'
);

-- Users can only see active opportunities
INSERT INTO sys_record_bindings (
  id, workspace_id, entity_name, condition, name
) VALUES (
  gen_random_uuid(),
  'workspace-123',
  'opportunities',
  'status IN (''open'', ''negotiating'', ''won'')',
  'Active Opportunities Only'
);
```

### Step 4: Result

- • Alice (East) sees her accounts + East team accounts in East territory
- • Bob (West) sees his accounts + West team accounts in West territory
- • Managers see all accounts in their region (via group hierarchy)
- • VP of Sales sees all accounts (member of parent Sales group)
- • Contacts automatically follow account access
- • Everyone can view products, only product managers can edit

## Example 2: Multi-Tenant SaaS

Complete tenant isolation with per-tenant data access.

### Implementation
Copy
```
-- All tables have tenant_id column
ALTER TABLE customers ADD COLUMN tenant_id UUID NOT NULL;
ALTER TABLE orders ADD COLUMN tenant_id UUID NOT NULL;
ALTER TABLE products ADD COLUMN tenant_id UUID NOT NULL;

-- Universal RLS policy: tenant isolation
INSERT INTO sys_record_bindings (
  id, workspace_id, entity_name, condition, name
) VALUES
  (gen_random_uuid(), 'ws-1', 'customers', 
   'tenant_id = current_user_tenant_id()', 'Tenant Isolation'),
  (gen_random_uuid(), 'ws-1', 'orders', 
   'tenant_id = current_user_tenant_id()', 'Tenant Isolation'),
  (gen_random_uuid(), 'ws-1', 'products', 
   'tenant_id = current_user_tenant_id()', 'Tenant Isolation');

-- Set session context on login
SET LOCAL app.current_tenant_id = 'tenant-acme';

-- All queries automatically filtered by tenant
SELECT * FROM customers;
-- Only returns Acme Corp's customers
```

## Example 3: Healthcare (HIPAA Compliance)

Protecting PHI with comprehensive security and audit logging.

### Table Settings + Field Permissions
Copy
```
-- Patients table: Private
UPDATE sys_table_settings SET
  default_access = 'private',
  rls_enabled = true
WHERE table_name = 'patients';

-- Hide PHI from non-medical staff
INSERT INTO sys_field_permissions 
  (table_name, column_name, principal_id, principal_type, access_level)
VALUES
  ('patients', 'ssn', 'role-admin-staff', 'role', 'none'),
  ('patients', 'medical_history', 'role-admin-staff', 'role', 'none'),
  ('patients', 'diagnoses', 'role-admin-staff', 'role', 'none');

-- RLS: Doctors see only their assigned patients
INSERT INTO sys_record_bindings VALUES (
  gen_random_uuid(), 'ws-1', 'patients',
  'assigned_doctor_id = current_user_id()', 
  'Doctor-Patient Assignment'
);

-- Enable comprehensive audit logging
UPDATE sys_table_settings SET
  track_created_by = true,
  track_updated_by = true,
  audit_all_access = true  -- Log every read
WHERE table_name = 'patients';
```

## Example 4: Education Platform

Students, teachers, courses with grade privacy.

### Implementation
Copy
```
-- Students see their own courses
INSERT INTO sys_record_bindings VALUES (
  gen_random_uuid(), 'ws-1', 'enrollments',
  'student_id = current_user_id()', 
  'Student Enrollment Access'
);

-- Teachers see courses they teach
INSERT INTO sys_record_bindings VALUES (
  gen_random_uuid(), 'ws-1', 'courses',
  'teacher_id = current_user_id()', 
  'Teacher Course Access'
);

-- Students see course materials
UPDATE sys_table_settings SET
  default_access = 'private'
WHERE table_name = 'course_materials';

-- Share materials with enrolled students
INSERT INTO sys_record_group_bindings (
  entity_name, entity_id, principal_id, principal_type, access_level
)
SELECT 
  'course_materials',
  material_id,
  student_id,
  'user',
  'read'
FROM enrollments
WHERE status = 'active';

-- Hide grades from students until published
INSERT INTO sys_field_permissions VALUES
  ('assignments', 'grade', 'user-type-student', 'user_type', 'none')
WHERE NOT published;
```

## Example 5: E-Commerce Platform

Customers see their orders, vendors manage their products.

### Implementation
Copy
```
-- Customers: Private (see only their data)
UPDATE sys_table_settings SET default_access = 'private'
WHERE table_name IN ('orders', 'addresses', 'payment_methods');

-- Products: Public read-only (everyone browses)
UPDATE sys_table_settings SET default_access = 'public_read_only'
WHERE table_name = 'products';

-- Vendors see only their products
INSERT INTO sys_record_bindings VALUES (
  gen_random_uuid(), 'ws-1', 'products',
  'vendor_id = current_user_vendor_id()', 
  'Vendor Product Access'
);

-- Customer support sees all orders (via group)
INSERT INTO sys_user_groups VALUES
  ('user-support-1', 'grp-support'),
  ('user-support-2', 'grp-support');

-- Share all orders with support group
UPDATE orders SET secondary_group_id = 'grp-support';

-- Mask payment info from support
INSERT INTO sys_field_permissions VALUES
  ('payment_methods', 'card_number', 'grp-support', 'group', 'read', true),
  ('payment_methods', 'cvv', 'grp-support', 'group', 'none');
```

## Example 6: Enterprise ERP

Complex multi-department, multi-location enterprise system.

### Hierarchical Structure
Copy
```
-- Corporate hierarchy
Company HQ
├── Finance Department
│   ├── Accounting
│   └── Payroll
├── Operations
│   ├── Manufacturing
│   │   ├── Plant A
│   │   └── Plant B
│   └── Distribution
│       ├── Warehouse 1
│       └── Warehouse 2
└── HR Department

-- Branch-based access (record-as-group)
UPDATE sys_table_settings SET
  record_as_group = true,
  record_group_type = 'branch',
  record_group_id_column = 'id',
  record_group_name_column = 'branch_name'
WHERE table_name = 'branches';

-- Employees see data from their branch
INSERT INTO sys_record_bindings VALUES (
  gen_random_uuid(), 'ws-1', 'inventory',
  'branch_id IN (current_user_branches())', 
  'Branch Access'
);

-- Finance sees all financials
INSERT INTO sys_user_groups VALUES
  ('user-cfo', 'grp-finance');

UPDATE financial_records 
SET primary_group_id = 'grp-finance';

-- Plant managers see only their plant
INSERT INTO sys_record_bindings VALUES (
  gen_random_uuid(), 'ws-1', 'production_orders',
  'plant_id = current_user_plant_id()', 
  'Plant-Based Access'
);
```

## Common Patterns Summary
PatternImplementationUse CaseTerritory-BasedRLS policy on territory fieldSales CRM, Regional operationsTenant Isolationtenant_id + RLS policyMulti-tenant SaaSDepartment-BasedGroups + primary_group_idEnterprise ERP, HospitalsAssignment-BasedRLS: assigned_to = current_userSupport tickets, TasksHierarchicalNested groups + inheritanceLarge organizationsParent-Childcontrolled_by_parent OWDOrder lines, Sub-recordsRole-BasedPermission sets + rolesFeature access control
## Learn More
[### Security Overview

Complete 5-layer model](https://www.algorithmshift.ai/docs/data-authorization)[### Best Practices

Implementation guidelines](https://www.algorithmshift.ai/docs/data-authorization/best-practices)[### Quick Start

Get started with AlgorithmShift](https://www.algorithmshift.ai/docs/quick-start)
