# Audit & Compliance - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/data-authorization/audit  
**Scraped:** 2025-12-10 14:04:29

**Description:** Comprehensive audit logging, access tracking, and compliance features for enterprise security requirements.

---

Audit & Compliance - AlgorithmShift Documentation | AlgorithmShiftDocumentationData Authorization & Security
# Audit & Compliance

Track every data access, modification, and security change. Meet enterprise compliance requirements with comprehensive audit trails.

## Audit Features

### Access Logging

Track every data access with who, what, when details

### Change Tracking

Record all CREATE, UPDATE, DELETE operations with before/after values

### Security Events

Log permission changes, role assignments, policy updates

### Retention Policies

Configurable audit log retention (90 days, 1 year, indefinite)

### Anomaly Detection

Alert on unusual access patterns or bulk exports

### Compliance Reports

Pre-built reports for SOC 2, HIPAA, GDPR compliance

## sys_audit_logs Schema
Copy
```
CREATE TABLE sys_audit_logs (
  log_id UUID PRIMARY KEY,
  workspace_id UUID NOT NULL,
  
  -- Event Details
  event_type VARCHAR NOT NULL,
    -- 'data_access', 'data_create', 'data_update', 'data_delete',
    -- 'permission_grant', 'permission_revoke', 'role_assign',
    -- 'rls_policy_create', 'share_create', 'login', 'api_key_use'
  
  event_category VARCHAR NOT NULL,
    -- 'data', 'security', 'auth', 'admin'
  
  -- Actor (Who)
  actor_id UUID,                    -- User or API key
  actor_type VARCHAR,                -- 'user', 'api_key', 'system'
  actor_email VARCHAR,
  actor_ip_address INET,
  
  -- Target (What)
  target_type VARCHAR,               -- 'record', 'table', 'user', 'role'
  target_id VARCHAR,
  target_table VARCHAR,
  
  -- Action Details
  action VARCHAR NOT NULL,           -- 'read', 'create', 'update', 'delete'
  affected_records INTEGER,
  
  -- Change Tracking
  old_values JSONB,
  new_values JSONB,
  changed_fields TEXT[],
  
  -- Context
  request_id UUID,
  session_id UUID,
  user_agent TEXT,
  
  -- Metadata
  timestamp TIMESTAMP DEFAULT NOW(),
  success BOOLEAN DEFAULT true,
  error_message TEXT,
  
  -- Indexing
  INDEX idx_audit_workspace_time (workspace_id, timestamp DESC),
  INDEX idx_audit_actor (actor_id, timestamp DESC),
  INDEX idx_audit_target (target_table, target_id),
  INDEX idx_audit_event (event_type, timestamp DESC)
);
```

## Automatic Audit Logging

### Data Access Logging
Copy
```
-- Every SELECT query is logged
SELECT * FROM customers WHERE id = '123';

-- Creates audit log:
INSERT INTO sys_audit_logs (
  log_id, workspace_id, event_type, event_category,
  actor_id, actor_email, actor_ip_address,
  target_type, target_id, target_table,
  action, affected_records, timestamp
) VALUES (
  gen_random_uuid(),
  'workspace-123',
  'data_access',
  'data',
  'user-alice',
  'alice@company.com',
  '192.168.1.100',
  'record',
  '123',
  'customers',
  'read',
  1,
  NOW()
);
```

### Data Modification Logging
Copy
```
-- UPDATE with before/after tracking
UPDATE customers 
SET status = 'active', priority = 'high'
WHERE id = '123';

-- Creates audit log with change tracking:
INSERT INTO sys_audit_logs (
  log_id, event_type, actor_id, target_table, target_id,
  action, changed_fields, old_values, new_values
) VALUES (
  gen_random_uuid(),
  'data_update',
  'user-alice',
  'customers',
  '123',
  'update',
  ARRAY['status', 'priority'],
  '{"status": "pending", "priority": "normal"}'::jsonb,
  '{"status": "active", "priority": "high"}'::jsonb
);
```

### Security Event Logging
Copy
```
-- Permission granted
INSERT INTO sys_user_permissions (user_id, permission_id)
VALUES ('user-bob', 'ps_workflows_execute');

-- Creates audit log:
INSERT INTO sys_audit_logs (
  event_type, event_category, actor_id, target_type, target_id,
  action, new_values
) VALUES (
  'permission_grant',
  'security',
  'user-alice',  -- Admin who granted
  'user',
  'user-bob',    -- User who received
  'grant',
  '{"permission": "ps_workflows_execute"}'::jsonb
);
```

## Querying Audit Logs
Copy
```
-- Who accessed customer 123 in the last 30 days?
SELECT 
  actor_email,
  actor_ip_address,
  action,
  timestamp
FROM sys_audit_logs
WHERE target_table = 'customers'
  AND target_id = '123'
  AND event_category = 'data'
  AND timestamp > NOW() - INTERVAL '30 days'
ORDER BY timestamp DESC;

-- What did Alice do today?
SELECT 
  event_type,
  target_table,
  target_id,
  action,
  affected_records,
  timestamp
FROM sys_audit_logs
WHERE actor_id = 'user-alice'
  AND timestamp >= CURRENT_DATE
ORDER BY timestamp DESC;

-- Find bulk data exports
SELECT 
  actor_email,
  target_table,
  affected_records,
  timestamp
FROM sys_audit_logs
WHERE event_type = 'data_access'
  AND affected_records > 1000
  AND timestamp > NOW() - INTERVAL '7 days'
ORDER BY affected_records DESC;
```

## Compliance Features

### Built-In Compliance Support

SOC 2 Type II

Complete audit trails, access controls, and change tracking

GDPR

Data access logs, right-to-be-forgotten support, consent tracking

HIPAA

PHI access logging, minimum necessary access, audit reports

ISO 27001

Information security management, access control evidence

## Compliance Reports

### Access Report

- • Who accessed what data
- • Time ranges and frequency
- • Failed access attempts
- • Unusual access patterns

### Change Report

- • All data modifications
- • Before/after values
- • Who made changes
- • Rollback capability

### Security Report

- • Permission changes
- • Role assignments
- • Policy modifications
- • Security events timeline

### User Activity Report

- • Per-user activity summary
- • Login history
- • API key usage
- • Actions performed

## Audit Log Retention
Copy
```
-- Configure retention policy
UPDATE sys_workspace_settings
SET audit_log_retention_days = 365  -- 1 year
WHERE workspace_id = 'workspace-123';

-- Automatic archival (daily job)
INSERT INTO sys_audit_logs_archive
SELECT * FROM sys_audit_logs
WHERE timestamp < NOW() - INTERVAL '365 days';

DELETE FROM sys_audit_logs
WHERE timestamp < NOW() - INTERVAL '365 days';

-- Compliance-driven retention
-- SOC 2: Minimum 90 days
-- HIPAA: Minimum 6 years
-- GDPR: As long as processing occurs
```

## Viewing Audit Logs

### Audit Log Interface

Navigate to: /{workspaceId}/access-control/audit-logs

Real-Time View

Live stream of security events

Advanced Filters

Filter by user, table, action, date range

Export Logs

Download as CSV, JSON for external analysis

Compliance Reports

Pre-built reports for auditors

## Best Practices

Enable audit logging on all tables

Comprehensive logging ensures no blind spots

Review logs regularly

Weekly review of unusual activity patterns

Set appropriate retention

Balance compliance requirements with storage costs

Archive old logs

Move old logs to cold storage (S3 Glacier)

Set up alerts

Notify on bulk exports, failed access, permission changes

## Learn More
[### Field Permissions

Column-level access control](https://www.algorithmshift.ai/docs/data-authorization/field-permissions)[### Best Practices

Security and audit best practices](https://www.algorithmshift.ai/docs/data-authorization/best-practices)[### Monitoring

Application monitoring tools](https://www.algorithmshift.ai/docs/monitoring)
