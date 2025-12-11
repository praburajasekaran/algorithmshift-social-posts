# REST APIs - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/database/rest  
**Scraped:** 2025-12-10 14:03:41

**Description:** Auto-generated REST APIs for every database table. Complete CRUD operations with advanced querying.

---

REST APIs - AlgorithmShift Documentation | AlgorithmShiftDocumentationDatabase & APIs
# REST APIs

Every table in your workspace automatically gets a full REST API with CRUD operations, filtering, sorting, pagination, and more.
`GET`
### List/Read
`POST`
### Create
`PUT`
### Update
`PATCH`
### Partial Update
`DELETE`
### Delete

## Endpoint Structure
Copy
```
# Base URL
https://api.algorithmshift.ai/api/v1

# Table endpoints
/tables/{table_name}           # Collection endpoint
/tables/{table_name}/{id}      # Single resource endpoint

# Entity endpoints (advanced)
/entities/{table_name}         # With complex filtering

# Examples
GET    /api/v1/tables/tasks
POST   /api/v1/tables/tasks
GET    /api/v1/tables/tasks/123
PUT    /api/v1/tables/tasks/123
DELETE /api/v1/tables/tasks/123
```

## Shorthand Filter Operators

AlgorithmShift supports bracket notation for advanced filtering directly in the URL query string. Perfect for REST clients, webhooks, and dynamic filtering.

### Why Shorthand Operators?

Instead of sending a JSON body with complex filter objects, you can use simple URL parameters with bracket notation for common query patterns.
**Standard (verbose):**`POST with {"filter": {"price": {"gte": 100}}}`**Shorthand (simple):**`GET ?price[gte]=100`
### Available Shorthand Operators
OperatorMeaningExample[gte]Greater than or equalprice[gte]=100[lte]Less than or equalprice[lte]=500[gt]Greater thanstock[gt]=0[lt]Less thanpriority[lt]=5[ne]Not equalstatus[ne]=deleted[like]Pattern match (case-insensitive)name[like]=%john%[in]In array (comma-separated)status[in]=active,pending[nin]Not in arrayrole[nin]=admin,superadmin[null]Is null or not nulldeleted_at[null]=true
### Real-World Examples

Date Range (last 30 days):
Copy
```
GET /api/v1/tables/orders?created_at[gte]=2024-01-01&created_at[lte]=2024-01-31
```

Price Range:
Copy
```
GET /api/v1/tables/products?price[gte]=100&price[lte]=500
```

Multiple Statuses:
Copy
```
GET /api/v1/tables/tasks?status[in]=pending,in-progress,review
```

Search by Name:
Copy
```
GET /api/v1/tables/customers?name[like]=%smith%
```

Exclude Deleted Records:
Copy
```
GET /api/v1/tables/users?deleted_at[null]=true
```

Combining Multiple Filters:
Copy
```
GET /api/v1/tables/leads?
  status[in]=qualified,contacted&
  score[gte]=70&
  created_at[gte]=2024-01-01&
  source[ne]=spam
```
[Complete Filtering Guide →](https://www.algorithmshift.ai/docs/api/filtering)
## Foreign Key Expansion

Use the expand parameter to fetch related records in a single request, reducing the number of API calls needed.
Copy
```
# Without expansion (2 requests needed)
GET /api/v1/tables/orders/123
{
  "order_id": "123",
  "customer_id": "customer-456",
  "product_id": "product-789"
}

# Then fetch customer separately
GET /api/v1/tables/customers/customer-456

# With expansion (1 request)
GET /api/v1/tables/orders/123?expand=customer_id,product_id
{
  "order_id": "123",
  "customer_id": "customer-456",
  "product_id": "product-789",
  "_expanded": {
    "customer_id": {
      "customer_id": "customer-456",
      "name": "Acme Corp",
      "email": "contact@acme.com"
    },
    "product_id": {
      "product_id": "product-789",
      "name": "Premium Subscription",
      "price": 99.00
    }
  }
}
```

## Complex Filters (JSON Body)

For advanced filtering beyond shorthand operators, use the /entities endpoint with JSON filter objects.

### OR Conditions
Copy
```
POST /api/v1/entities/tasks
{
  "filter": {
    "or": [
      { "status": "urgent" },
      { "priority": { "gte": 8 } }
    ]
  }
}
```

### AND + OR Combination
Copy
```
POST /api/v1/entities/tasks
{
  "filter": {
    "and": [
      { "status": "active" },
      {
        "or": [
          { "assigned_to": "user-123" },
          { "created_by": "user-123" }
        ]
      }
    ]
  }
}
```

## Aggregations

Perform SQL aggregations (COUNT, SUM, AVG, MIN, MAX) with grouping and filtering.
Copy
```
POST /api/v1/entities/tasks/aggregate
{
  "groupBy": ["status"],
  "aggregations": {
    "count": "*",
    "avg_priority": { "avg": "priority" },
    "total_hours": { "sum": "estimated_hours" }
  }
}

// Response
{
  "data": [
    {
      "status": "pending",
      "count": 45,
      "avg_priority": 6.2,
      "total_hours": 120
    },
    {
      "status": "completed",
      "count": 78,
      "avg_priority": 5.8,
      "total_hours": 234
    }
  ]
}
```

## Pagination & Sorting

### Pagination
Copy
```
# Limit and offset
GET /api/v1/tables/tasks?limit=50&offset=100

# Page-based
GET /api/v1/tables/tasks?page=3&pageSize=25
```

### Sorting
Copy
```
# Ascending
GET /api/v1/tables/tasks?sort=created_at

# Descending
GET /api/v1/tables/tasks?sort=-created_at

# Multiple fields
GET /api/v1/tables/tasks?sort=-priority,created_at
```
