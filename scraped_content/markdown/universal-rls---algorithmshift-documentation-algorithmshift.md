# Universal RLS - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/data-authorization/universal-rls  
**Scraped:** 2025-12-10 14:04:16

**Description:** Automatic security injection for every query. How AlgorithmShift applies all 5 security layers transparently.

---

Universal RLS - AlgorithmShift Documentation | AlgorithmShiftDocumentationData Authorization & Security
# Universal RLS (Row-Level Security)

Automatic security injection for every database query. Write simple SQL, get enterprise-grade security automatically applied.

### What is Universal RLS?

Universal RLS is AlgorithmShift's automatic security system that intercepts every database query and injects all 5 security layers transparently.

You write: SELECT * FROM customersSystem executes: SELECT * FROM customers WHERE (5 layers of security)

## How Universal RLS Works

### 1. Query Interception

Every query passes through middleware that extracts user context

### 2. Security Injection

All 5 security layers are added to the WHERE clause automatically

### 3. Database Execution

PostgreSQL executes the secured query with optimized plan

## Implementation Methods

AlgorithmShift uses multiple techniques to ensure universal security:

### Method 1: PostgreSQL RLS Policies
Copy
```
-- Enable RLS on table
ALTER TABLE customers ENABLE ROW LEVEL SECURITY;

-- Create universal policy
CREATE POLICY universal_rls_policy ON customers
FOR ALL
TO PUBLIC
USING (
  -- Layer 0: Admin bypass
  is_workspace_admin()
  
  OR
  
  (
    -- Layer 1: OWD check
    (
      get_table_owd('customers') IN ('public_read_write', 'public_read_only')
      OR
      -- Layers 2-4: Ownership, Groups, Shares (OR logic)
      (
        owner_id = current_user_id()
        OR primary_group_id IN (current_user_groups())
        OR secondary_group_id IN (current_user_groups())
        OR EXISTS (SELECT 1 FROM sys_record_group_bindings ...)
      )
    )
    -- Layer 5: RLS policies (AND logic)
    AND apply_rls_policies('customers', id)
  )
);
```

Benefit: Database-native enforcement, impossible to bypass

### Method 2: Query Rewriting Middleware
Copy
```
// Middleware intercepts all queries
async function universalRLSMiddleware(query, user) {
  // Parse SQL query
  const ast = parseSQL(query);
  
  // Extract table name
  const tableName = ast.from[0].table;
  
  // Build security WHERE clause
  const securityClause = buildSecurityClause(tableName, user);
  
  // Inject security into query
  ast.where = ast.where 
    ? `(${ast.where}) AND (${securityClause})`
    : securityClause;
  
  // Return modified query
  return generateSQL(ast);
}

// Usage (automatic)
const result = await db.query('SELECT * FROM customers');
// Actually executes: SELECT * FROM customers WHERE (security...)
```

Benefit: Application-level control, flexible and testable

### Method 3: Set Session Context
Copy
```
-- At connection start, set user context
SET LOCAL app.current_user_id = 'user-alice';
SET LOCAL app.current_user_groups = 'grp-1,grp-2,grp-3';
SET LOCAL app.current_user_role = 'workspace_user';

-- Helper functions use session variables
CREATE FUNCTION current_user_id() RETURNS UUID AS $$
  SELECT current_setting('app.current_user_id')::uuid;
$$ LANGUAGE SQL STABLE;

-- RLS policies reference these functions
CREATE POLICY ... USING (owner_id = current_user_id());
```

Benefit: Fast, no parameter passing needed

## Automatic Application

Universal RLS applies to all query types automatically:

#### SELECT Queries
Copy
```
SELECT * FROM customers WHERE name LIKE 'A%';
→ Filters rows based on all 5 layers
```

#### UPDATE Queries
Copy
```
UPDATE customers SET status = 'active' WHERE id = '123';
→ Only updates if user has access to record 123
```

#### DELETE Queries
Copy
```
DELETE FROM customers WHERE id = '123';
→ Only deletes if user has access to record 123
```

#### JOIN Queries
Copy
```
SELECT * FROM customers c
JOIN orders o ON c.id = o.customer_id;
→ Filters both customers AND orders based on their respective security
```

#### Aggregate Queries
Copy
```
SELECT COUNT(*) FROM customers;
→ Only counts records user has access to
```

## Performance Optimization

### Session Caching

- • User's groups cached in session
- • Permission UUIDs cached in JWT
- • Table settings cached in application
- • RLS policies compiled once

### Database Indexes

- • Index on owner_id
- • Index on primary_group_id
- • Index on secondary_group_id
- • Composite indexes for common patterns

### Query Planning

- • PostgreSQL query planner optimizes security WHERE clauses
- • Pushes filters as early as possible
- • Uses optimal join strategies

### Bypass for Admins

- • Admin check is first (Layer 0)
- • If admin, skip all security filters
- • No performance penalty for admins

## Testing Universal RLS
Copy
```
-- Test as different users
-- 1. Connect as admin
SET LOCAL app.current_user_id = 'admin-user';
SET LOCAL app.current_user_role = 'workspace_admin';

SELECT COUNT(*) FROM customers;
-- Returns: 10,000 (all records)

-- 2. Connect as regular user
SET LOCAL app.current_user_id = 'user-alice';
SET LOCAL app.current_user_role = 'workspace_user';
SET LOCAL app.current_user_groups = 'grp-sales';

SELECT COUNT(*) FROM customers;
-- Returns: 45 (only Alice's accessible records)

-- 3. Verify security is applied
EXPLAIN SELECT * FROM customers;
-- Shows: Filter on owner_id, primary_group_id, etc.
```

## Disabling RLS (For System Operations)

### When to Disable RLS

In rare cases (system migrations, admin operations), you may need to bypass RLS:
Copy
```
-- Temporarily disable RLS (requires superuser)
SET LOCAL row_security = OFF;

-- Perform admin operation
UPDATE customers SET migration_flag = true;

-- Re-enable (automatic at transaction end)
COMMIT;
```

⚠️ Only use for trusted system operations

## Learn More
[### How Access Works

Complete access evaluation flow](https://www.algorithmshift.ai/docs/data-authorization/access-flow)[### RLS Policies

Custom security rules (Layer 5)](https://www.algorithmshift.ai/docs/data-authorization/rls-policies)[### Database Setup

Configure database and tables](https://www.algorithmshift.ai/docs/database)
