# Database Views - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/database/views  
**Scraped:** 2025-12-10 14:03:43

**Description:** Create database views for complex queries. Reusable virtual tables with SQL.

---

Database Views - AlgorithmShift Documentation | AlgorithmShiftDocumentationDatabase & APIs
# Database Views

Create reusable virtual tables with SQL queries. Views get their own auto-generated REST APIs.

## What are Views?

Database views are saved SQL queries that act like virtual tables. They're perfect for:

### Use Cases

- Complex JOIN queries
- Aggregated data
- Computed columns
- Simplified data access

### Example View
Copy
```
CREATE VIEW v_customer_orders AS
SELECT 
  c.id as customer_id,
  c.name as customer_name,
  c.email,
  COUNT(o.id) as total_orders,
  SUM(o.total) as lifetime_value,
  MAX(o.created_at) as last_order_date
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
GROUP BY c.id, c.name, c.email;
```

## Creating Views

Navigate to Access Control → Data Management → Views, click "Create View"
Copy
```
{
  "name": "v_active_projects",
  "description": "Active projects with team member count",
  "sql": `
    SELECT 
      p.id,
      p.name,
      p.status,
      COUNT(DISTINCT pm.user_id) as team_size,
      COUNT(t.id) as total_tasks,
      SUM(CASE WHEN t.status = 'completed' THEN 1 ELSE 0 END) as completed_tasks
    FROM projects p
    LEFT JOIN project_members pm ON p.id = pm.project_id
    LEFT JOIN tasks t ON p.id = t.project_id
    WHERE p.status = 'active'
    GROUP BY p.id, p.name, p.status
  `
}

// Auto-generated API endpoint
GET /api/v1/views/v_active_projects
```
