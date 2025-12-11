# Identity Management - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/data-authorization/identity  
**Scraped:** 2025-12-10 14:04:24

**Description:** Manage users, groups, user types, and group types. The foundation of your security model.

---

Identity Management - AlgorithmShift Documentation | AlgorithmShiftDocumentationData Authorization & Security
# Identity Management

Manage the identities in your system: users, groups, user types, and group types. These form the foundation of your entire security model.

### Users

Individual accounts

### Groups

Organizational units

### User Types

Custom categories

### Group Types

Group categories

## Users

Users are individual accounts in your workspace. Each user has:

### User Properties
FieldTypeDescription`id`UUIDUnique identifier`email`VARCHAREmail address (unique)`name`VARCHARFull name`status`VARCHARactive, inactive, suspended`role`VARCHARworkspace_admin, workspace_user`user_type_id`UUIDLink to user type (optional)
### User Roles

workspace_admin

- • Full workspace access
- • Bypass all RLS policies
- • Manage users and permissions
- • Configure security settings

workspace_user

- • Limited access
- • Subject to RLS policies
- • See only authorized data
- • Cannot manage workspace

## Groups (Hierarchical Organization)

Groups organize users into hierarchical structures (like departments, teams, or organizational units).

### Group Properties
FieldDescription`id`Unique identifier`name`Group name (e.g., "Sales Team")`parent_group_id`Parent group for hierarchy (can be null)`group_type_id`Category (Department, Team, etc.)`kind`Group classification
### Hierarchical Structure Example
Copy
```
Company
├── Sales Department (parent_group_id: null)
│   ├── East Region (parent_group_id: Sales)
│   │   ├── Team A (parent_group_id: East Region)
│   │   └── Team B (parent_group_id: East Region)
│   └── West Region (parent_group_id: Sales)
│       └── Team C (parent_group_id: West Region)
└── Engineering (parent_group_id: null)
    ├── Frontend Team (parent_group_id: Engineering)
    └── Backend Team (parent_group_id: Engineering)

// Users in "Team A" automatically belong to:
// - Team A
// - East Region (parent)
// - Sales Department (grandparent)
```

## User Types

User Types are custom categories for organizing users (similar to Salesforce Record Types).

Employee

Internal staff members

Customer

External customers

Partner

Business partners

Contractor

Temporary contractors

Admin

System administrators

Manager

Department managers

Use user types to apply different security policies, UI layouts, or business logic based on user category.

## Group Types

Group Types categorize groups for better organization and policy application.

Department

Company departments

Team

Project or functional teams

Region

Geographic regions

Division

Business divisions

Office

Physical office locations

Role-Based

Role-specific groups

## Managing Identities

Access identity management from the admin interface:

### Access Control Interface

Navigate to: /{workspaceId}/access-control/identity

Users

CRUD operations, search, filter, pagination, role assignment

Groups

Hierarchical view, drag-drop organization, member management

User Types

Define categories, assign users, manage roles

Group Types

Categorize groups, apply policies

## Principal Concept

A principal is any entity that can have permissions or own data:

### User as Principal

Individual users can:

- • Own records (owner_id)
- • Be assigned permissions
- • Have records shared with them
- • Belong to groups

### Group as Principal

Groups can:

- • Own records (owner_id = group_id)
- • Have records shared with them
- • Grant access to all members
- • Have hierarchical relationships

### Record as Principal

Records can act as groups:

- • Account record = group
- • Related records auto-shared
- • Access inherited
- • Complex hierarchies

## Learn More
[### Ownership & Groups

How ownership and group membership grant access](https://www.algorithmshift.ai/docs/data-authorization/ownership)[### Principals Concept

Deep dive into principal-based access](https://www.algorithmshift.ai/docs/data-authorization/principals)[### Roles & Permissions

Assign roles and manage permissions](https://www.algorithmshift.ai/docs/data-authorization/roles)
