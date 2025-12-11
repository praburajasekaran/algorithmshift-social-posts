# Roles & Permissions - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/auth/roles  
**Scraped:** 2025-12-10 14:03:55

**Description:** Configure role-based access control. Define custom roles and assign granular permissions.

---

Roles & Permissions - AlgorithmShift Documentation | AlgorithmShiftDocumentationAuthentication
# Roles & Permissions

Implement role-based access control (RBAC) with custom roles and granular permissions.

## Permission Model
Copy
```
// Permission format: resource.action

// Examples:
tasks.read          // View tasks
tasks.create        // Create new tasks
tasks.update        // Edit tasks
tasks.delete        // Delete tasks
tasks.assign        // Assign tasks to others

users.read          // View users
users.manage        // Manage user accounts

reports.export      // Export reports
settings.configure  // Modify settings
```

## Creating Custom Roles

#### Role Configuration
Copy
```
{
  "name": "Project Manager",
  "description": "Manage projects and teams",
  "permissions": [
    "projects.read",
    "projects.create",
    "projects.update",
    "tasks.read",
    "tasks.create",
    "tasks.update",
    "tasks.assign",
    "users.read",
    "teams.read",
    "reports.view"
  ]
}
```

#### Assign to Users
Copy
```
// Assign role to user
POST /api/v1/users/{userId}/roles
{
  "roleId": "project-manager"
}

// User inherits all permissions
// from the role
```

## Built-in Roles

### workspace_admin

- All permissions
- Manage workspace settings
- Bypass RLS policies
- Manage other admins

### workspace_user

- Access assigned apps
- View own data (RLS applied)
- Limited API access
- Cannot manage workspace
