# Security Best Practices - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/data-authorization/best-practices  
**Scraped:** 2025-12-10 14:04:30

**Description:** Best practices for implementing and maintaining secure data authorization in AlgorithmShift.

---

Security Best Practices - AlgorithmShift Documentation | AlgorithmShiftDocumentationData Authorization & Security
# Security Best Practices

Essential guidelines for implementing and maintaining secure data authorization in your AlgorithmShift workspace.

## Organization-Wide Defaults (OWD)

### ✓ Start with Private, Open as Needed

Set default_access to 'private' for sensitive tables, then grant access through groups and shares.
Copy
```
-- Good: Secure by default
default_access: 'private'
-- Then explicitly grant access via groups

-- Bad: Too open
default_access: 'public_read_write'  ❌
```

### ✓ Use Public Read for Reference Data

Tables like countries, states, categories can be public_read_only or public_read_write.

### ✓ Use Controlled by Parent for Child Records

Order line items, contact notes, account attachments should inherit parent access.

## Groups & Hierarchies

### ✓ Mirror Your Organization Structure

Create groups that match your real-world departments, teams, and regions.
Copy
```
Company
├── Sales
│   ├── North America
│   └── Europe
├── Engineering
│   ├── Frontend
│   └── Backend
└── Support
```

### ✓ Use primary_group_id for Main Team

Assign records to the primary responsible team via primary_group_id.

### ✓ Use secondary_group_id for Cross-Functional

Use secondary_group_id for project teams, temporary collaborators, or secondary ownership.

### ✗ Don't Create Too Many Nested Levels

Keep hierarchy depth under 5 levels for performance. More than 5 levels can slow queries.

## RLS Policies

### ✓ Keep Policies Simple

Complex RLS policies impact query performance. Keep conditions simple and well-indexed.
Copy
```
-- Good: Simple, indexed
region = current_user_region()

-- Bad: Complex, unindexed
LOWER(region) LIKE LOWER(current_user_region() || '%')  ❌
```

### ✓ Index Fields Used in RLS
Copy
```
-- Create indexes for RLS policy fields
CREATE INDEX idx_customers_region ON customers(region);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_leads_assigned_to ON leads(assigned_to);
```

### ✓ Test RLS Policies Thoroughly

Test with multiple user accounts to ensure policies work as expected and don't over-restrict.

### ✗ Don't Use RLS for Business Logic

RLS is for security, not business rules. Use application logic or database triggers for business rules.

## Roles & Permissions

### ✓ Follow Principle of Least Privilege

Grant only the minimum permissions needed for users to do their job.

### ✓ Use Roles, Not Individual Permissions

Create roles (Sales Rep, Support Agent) and assign roles, not individual permissions.

### ✓ Grant workspace_admin Sparingly

Admin role bypasses ALL security. Only grant to fully trusted users.

### ✓ Regular Access Reviews

Quarterly review of who has what permissions. Remove access no longer needed.

## Field-Level Security

### ✓ Hide PII from Regular Users
Copy
```
-- Hide sensitive fields
access_level: 'none' for SSN, DOB, Tax ID
```

### ✓ Mask Financial Data
Copy
```
-- Mask instead of hide when UI needs field
access_level: 'read', mask_value: true
-- Shows: ****-****-****-1234
```

### ✓ Make Audit Fields Read-Only

created_at, created_by, updated_at, updated_by should be read-only for all users.

## Sharing & Collaboration

### ✓ Share with Groups, Not Users

Sharing with groups is more maintainable as team membership changes.

### ✓ Use Appropriate Access Levels

- • read - For visibility only
- • read_write - For collaboration
- • manage - Rarely needed (like ownership)

### ✗ Don't Over-Share

Excessive manual shares make security hard to audit. Use groups and OWD instead when possible.

## Performance Optimization

### Database Indexes
Copy
```
CREATE INDEX idx_owner ON customers(owner_id);
CREATE INDEX idx_primary_group ON customers(primary_group_id);
CREATE INDEX idx_secondary_group ON customers(secondary_group_id);
```

### Session Caching

- • Cache user groups in session
- • Cache permissions in JWT
- • Cache table settings in app

## Security Checklist
All sensitive tables set to private OWDGroups mirror organizational structureRLS policies are simple and indexedAdmin role granted to < 5% of usersPII fields have field-level securityAudit logging enabled on all tablesRegular access reviews (quarterly)API keys have expiration datesPermission sets follow least privilegeTest security with non-admin accounts
## Learn More
[### Security Overview

Complete 5-layer security model](https://www.algorithmshift.ai/docs/data-authorization)[### Real-World Examples

Complete implementation scenarios](https://www.algorithmshift.ai/docs/data-authorization/examples)[### Audit & Compliance

Track and log security events](https://www.algorithmshift.ai/docs/data-authorization/audit)
