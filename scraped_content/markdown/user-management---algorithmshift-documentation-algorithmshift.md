# User Management - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/auth/users  
**Scraped:** 2025-12-10 14:03:54

**Description:** Manage users, groups, and user types. Create users, assign roles, and control access.

---

User Management - AlgorithmShift Documentation | AlgorithmShiftDocumentationAuthentication
# User Management

Manage user accounts, assign roles, configure permissions, and organize users into groups and types.

### User CRUD

Create, read, update, delete users

### Role Assignment

Assign workspace and custom roles

### Group Management

Organize users into groups

## Creating Users

#### Via UI

Navigate to Access Control → Identity → Users, click "Create User"

- • Enter name and email
- • Set initial password
- • Assign role
- • Add to groups (optional)

#### Via API
Copy
```
POST /api/v1/users
{
  "email": "john@example.com",
  "name": "John Doe",
  "password": "SecurePass123!",
  "role": "workspace_user",
  "groups": ["group-id-1"],
  "status": "active"
}
```

## User Roles

### workspace_admin

- Full workspace access
- Manage users and permissions
- Configure database and RLS
- Deploy applications

### workspace_user

- Access assigned applications
- View own data (via RLS)
- Limited permissions
- Cannot manage workspace settings

## Learn More
[### Roles & Permissions

Configure custom roles and permissions](https://www.algorithmshift.ai/docs/auth/roles)[### Groups

Organize users into hierarchical groups](https://www.algorithmshift.ai/docs/auth)
