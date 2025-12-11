# API Resource Protection - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/data-authorization/api-resources  
**Scraped:** 2025-12-10 14:04:27

**Description:** Protect API endpoints with permission sets and API keys using deterministic UUID-based authorization.

---

API Resource Protection - AlgorithmShift Documentation | AlgorithmShiftDocumentationData Authorization & Security
# API Resource Protection

Protect API endpoints with permission-based access control. Define which users, roles, or API keys can access specific endpoints.

## API Resource Concept

API Resources are protected endpoints that require specific permissions. Combined with AlgorithmShift's deterministic permission UUID system, you get lightning-fast authorization checks.

### Why Protect API Resources?

While RLS controls data access, API resource protection controls feature access. Example: RLS ensures users only see their customers, but API resource protection determines if they can use the "Export to CSV" API at all.

## sys_api_resources Schema
Copy
```
CREATE TABLE sys_api_resources (
  resource_id UUID PRIMARY KEY,
  workspace_id UUID NOT NULL,
  
  -- Resource identification
  resource_name VARCHAR NOT NULL,        -- e.g., "workflows.execute"
  resource_path VARCHAR NOT NULL,        -- e.g., "/api/v1/workflows/:id/execute"
  http_method VARCHAR,                   -- "GET", "POST", "PUT", "DELETE", "*"
  
  -- Permission requirement
  required_permission_set VARCHAR,       -- e.g., "ps_workflows_execute"
  
  -- Description
  display_name VARCHAR,
  description TEXT,
  category VARCHAR,                      -- "workflows", "ai_agents", "reports"
  
  -- Configuration
  is_active BOOLEAN DEFAULT true,
  rate_limit_per_minute INTEGER,
  
  -- Metadata
  created_by UUID,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  
  UNIQUE(workspace_id, resource_path, http_method)
);
```

## How API Protection Works
Copy
```
// 1. User/API Key makes request
POST /api/v1/workflows/wf-123/execute

// 2. Server checks API resource protection
const resource = await getAPIResource('/api/v1/workflows/:id/execute', 'POST');
// Returns: { required_permission_set: 'ps_workflows_execute' }

// 3. Check if requester has permission (in-memory, instant)
const permissionUUID = getPermissionUUID('ps_workflows_execute');
const hasPermission = user.permissions.includes(permissionUUID);

if (!hasPermission) {
  return 403 Forbidden;
}

// 4. Permission granted, proceed with request
// (RLS still applies to the actual workflow data)
```

## Common API Resources

### Workflow Execution
Copy
```
INSERT INTO sys_api_resources (
  resource_id,
  workspace_id,
  resource_name,
  resource_path,
  http_method,
  required_permission_set,
  display_name,
  category
) VALUES (
  gen_random_uuid(),
  'workspace-123',
  'workflows.execute',
  '/api/v1/workflows/:id/execute',
  'POST',
  'ps_workflows_execute',
  'Execute Workflow',
  'workflows'
);

-- Now only users with ps_workflows_execute can trigger workflows
```

### Data Export
Copy
```
INSERT INTO sys_api_resources (
  resource_id,
  workspace_id,
  resource_name,
  resource_path,
  http_method,
  required_permission_set,
  display_name
) VALUES (
  gen_random_uuid(),
  'workspace-123',
  'data.export',
  '/api/v1/tables/:table/export',
  'POST',
  'ps_data_export',
  'Export Data to CSV/Excel'
);

-- Requires ps_data_export permission to use export API
```

### AI Agent Management
Copy
```
INSERT INTO sys_api_resources VALUES
  (gen_random_uuid(), 'workspace-123', 'agents.create',
   '/api/v1/agents', 'POST', 'ps_ai_agents_create', 'Create AI Agent', 'ai_agents'),
  
  (gen_random_uuid(), 'workspace-123', 'agents.update',
   '/api/v1/agents/:id', 'PUT', 'ps_ai_agents_manage', 'Update AI Agent', 'ai_agents'),
  
  (gen_random_uuid(), 'workspace-123', 'agents.delete',
   '/api/v1/agents/:id', 'DELETE', 'ps_ai_agents_manage', 'Delete AI Agent', 'ai_agents');

-- Different permissions for create vs manage
```

## API Keys with Permission Sets

API keys can be created with specific permission sets, allowing external systems to access protected resources:
Copy
```
-- Create API key with specific permissions
INSERT INTO sys_api_keys (
  api_key_id,
  workspace_id,
  key_name,
  key_hash,
  permission_sets,  -- Array of permission set names
  user_id,
  expires_at
) VALUES (
  gen_random_uuid(),
  'workspace-123',
  'Zapier Integration Key',
  hash('ask_live_...'),
  ARRAY[
    'ps_workflows_execute',
    'ps_tbl_customers_r',
    'ps_tbl_customers_w',
    'ps_webhooks_receive'
  ],
  'user-alice',
  NOW() + INTERVAL '90 days'
);

-- When API key is used:
-- 1. Convert permission set names → UUIDs
-- 2. Check if required permission UUID is in key's permission UUIDs
-- 3. Grant or deny access
```

## Permission Checking Middleware
Copy
```
// Express middleware example
async function requirePermission(permissionName: string) {
  return async (req, res, next) => {
    // Get user or API key from request
    const principal = req.user || req.apiKey;
    
    if (!principal) {
      return res.status(401).json({ error: 'Unauthorized' });
    }
    
    // Check permission (in-memory, instant)
    const permissionUUID = getPermissionUUID(permissionName);
    const hasPermission = principal.permissions.includes(permissionUUID);
    
    if (!hasPermission) {
      return res.status(403).json({ 
        error: 'Forbidden',
        required_permission: permissionName 
      });
    }
    
    next();
  };
}

// Usage
app.post('/api/v1/workflows/:id/execute',
  requirePermission('ps_workflows_execute'),
  async (req, res) => {
    // Execute workflow
  }
);
```

## Resource Categories
CategoryExample ResourcesPermission SetsWorkflowsExecute, Create, Delete`ps_workflows_*`AI AgentsCreate, Manage, Chat`ps_ai_agents_*`DataExport, Import, Bulk Edit`ps_data_*`ReportsCreate, Run, Export`ps_reports_*`PortalsCreate, Configure, Deploy`ps_portals_*`FunctionsDeploy, Execute, Monitor`ps_functions_*`StorageUpload, Download, Delete`ps_storage_*`
## Rate Limiting by Resource
Copy
```
-- Set rate limits per resource
UPDATE sys_api_resources
SET rate_limit_per_minute = 10
WHERE resource_name = 'workflows.execute';

UPDATE sys_api_resources
SET rate_limit_per_minute = 100
WHERE resource_name = 'data.query';

-- Expensive operations: Lower limits
-- Read operations: Higher limits
```

## Managing API Resources

### API Resources Interface

Navigate to: /{workspaceId}/access-control/api-security/api-resources

Browse Resources

View all protected API endpoints

Create Protection

Add permission requirements to endpoints

Test Access

Verify which users can access resources

Usage Analytics

Monitor API resource usage

## Learn More
[### Permission Sets

Deterministic UUID-based permissions](https://www.algorithmshift.ai/docs/data-authorization/permission-sets)[### Roles & Permissions

Assign permissions to users](https://www.algorithmshift.ai/docs/data-authorization/roles)[### API Authentication

API key authentication methods](https://www.algorithmshift.ai/docs/api/auth)
