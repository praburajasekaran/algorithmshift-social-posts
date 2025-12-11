# Authentication & Access Control - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/auth  
**Scraped:** 2025-12-10 14:03:09

**Description:** Secure your applications with built-in authentication, role-based access control, and row-level security.

---

Authentication & Access Control - AlgorithmShift Documentation | AlgorithmShiftDocumentationAuthentication
# Authentication & Access Control

Secure your applications with enterprise-grade authentication, role-based access control (RBAC), and row-level security (RLS). Built-in support for OAuth, SAML, and multi-factor authentication.

### User Management

Complete user lifecycle management

### RBAC

Role-based permissions

### Row-Level Security

Data access control

### OAuth & SSO

Social login and enterprise SSO

### API Keys

Programmatic access

### Groups

Hierarchical organization

## Authentication Methods

AlgorithmShift supports multiple authentication methods to fit your needs:

### Email & Password

Traditional username/password authentication

#### Features

- Email verification
- Password reset flow
- Password policies (min length, complexity)
- Two-factor authentication (2FA)

#### Sign-Up Example
Copy
```
// POST /api/auth/signup
{
  "email": "user@example.com",
  "password": "SecurePass123!",
  "name": "John Doe"
}

// Response
{
  "success": true,
  "user": {
    "id": "user-123",
    "email": "user@example.com",
    "email_verified": false
  },
  "message": "Verification email sent"
}
```

### OAuth Providers

Social login with Google, Microsoft, GitHub

#### Supported Providers

Google

Microsoft

GitHub

LinkedIn

#### Configuration
Copy
```
// OAuth configuration
{
  "providers": {
    "google": {
      "enabled": true,
      "clientId": "{{ secrets.GOOGLE_CLIENT_ID }}",
      "clientSecret": "{{ secrets.GOOGLE_CLIENT_SECRET }}",
      "scope": ["email", "profile"]
    },
    "microsoft": {
      "enabled": true,
      "clientId": "{{ secrets.MS_CLIENT_ID }}",
      "tenant": "common"
    }
  }
}
```

### SAML SSO

Enterprise single sign-on

#### Use Cases

- • Enterprise customer portals
- • B2B applications
- • Large organization deployments
- • Compliance requirements

#### SAML Endpoints
Copy
```
// Service Provider URLs
SSO URL: https://auth.algorithmshift.ai/saml/sso
ACS URL: https://auth.algorithmshift.ai/saml/acs
Entity ID: https://algorithmshift.ai

// Identity Provider Configuration
{
  "idpEntityId": "https://idp.example.com",
  "idpSsoUrl": "https://idp.example.com/sso",
  "idpCertificate": "-----BEGIN CERTIFICATE-----..."
}
```

## Access Control Structure

AlgorithmShift uses a comprehensive access control system:
Copy
```
Identity Layer
├── Users (individual accounts)
├── Groups (organizational units)
│   ├── Departments
│   ├── Teams
│   └── Hierarchies (parent-child)
└── User Types (custom categories)

Authorization Layer
├── Roles (collections of permissions)
│   └── workspace_admin, workspace_user, custom_role
├── Permissions (granular access rights)
│   └── resource.action (e.g., tasks.create, users.read)
└── Record Bindings (row-level security)
    └── Principal-based data access

API Security
├── API Keys (programmatic access)
└── API Resources (endpoint protection)
```

## Role-Based Access Control (RBAC)

Control access with roles and permissions:

### Creating Roles

#### Built-in Roles

workspace_admin

Full access to workspace

workspace_user

Limited access

#### Custom Role Example
Copy
```
// Create custom role
{
  "name": "Project Manager",
  "description": "Manage projects and tasks",
  "permissions": [
    "projects.read",
    "projects.create",
    "projects.update",
    "tasks.read",
    "tasks.create",
    "tasks.update",
    "tasks.assign",
    "users.read"
  ]
}
```

### Permission Model

Permissions follow the format: resource.action
ResourceActionsExample`tasks`read, create, update, delete`tasks.create``users`read, create, update, delete`users.read``projects`read, create, update, delete, manage`projects.manage``reports`read, create, export`reports.export`
## Row-Level Security (RLS)

Control data access at the row level:

### What is RLS?

Row-Level Security ensures users can only access data they're authorized to see. It's enforced at the database level, making it impossible to bypass.
Copy
```
// Example: Users can only see their own tasks
{
  "table": "tasks",
  "policy": "user_access",
  "condition": "user_id = {{ current_user.id }}"
}

// Example: Managers can see their team's tasks
{
  "table": "tasks",
  "policy": "manager_access",
  "condition": "user_id IN (SELECT user_id FROM team_members WHERE manager_id = {{ current_user.id }})"
}
```

### RLS Policies

Owner-based Access

Users can only access records they created
Copy
```
created_by = {{ current_user.id }}
```

Group-based Access

Users can access records belonging to their group
Copy
```
group_id IN (SELECT group_id FROM user_groups WHERE user_id = {{ current_user.id }})
```

Role-based Access

Different access based on user role
Copy
```
CASE
  WHEN {{ current_user.role }} = 'admin' THEN true
  WHEN {{ current_user.role }} = 'manager' THEN department_id = {{ current_user.department_id }}
  ELSE user_id = {{ current_user.id }}
END
```

## API Keys

Generate API keys for programmatic access:

### Creating API Keys

#### Key Properties
Format`as_[64-char-hex]`User`workspace_admin`Expiration`Optional`Permissions`Inherited from user`
#### Using API Keys
Copy
```
// In HTTP requests
curl -X GET \
  https://api.algorithmshift.ai/api/v1/tables/tasks \
  -H "Authorization: Bearer as_1234..." \
  -H "Content-Type: application/json"

// In JavaScript
fetch('/api/v1/tables/tasks', {
  headers: {
    'Authorization': `Bearer ${apiKey}`,
    'Content-Type': 'application/json'
  }
})
```

### Security Best Practices

- Store API keys in environment variables, never in code
- Set expiration dates on API keys
- Use different keys for development and production
- Rotate keys regularly
- Monitor API key usage for suspicious activity

## Learn More
[### User Management

Manage users, groups, and user types](https://www.algorithmshift.ai/docs/auth/users)[### Roles & Permissions

Define roles and assign permissions](https://www.algorithmshift.ai/docs/auth/roles)[### Row-Level Security

Implement data access policies](https://www.algorithmshift.ai/docs/auth/rls)[### OAuth Providers

Configure social login](https://www.algorithmshift.ai/docs/auth/oauth)[### SAML SSO

Enterprise single sign-on](https://www.algorithmshift.ai/docs/auth/saml)[### API Keys

Generate and manage API keys](https://www.algorithmshift.ai/docs/auth/api-keys)
