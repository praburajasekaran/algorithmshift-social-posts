# REST API Reference - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/api  
**Scraped:** 2025-12-10 14:02:21

**Description:** Complete REST API documentation. Auto-generated endpoints for every table with filtering, sorting, and pagination.

---

REST API Reference - AlgorithmShift Documentation | AlgorithmShiftDocumentationAPI Reference
# REST API Reference

Auto-generated REST APIs for every table in your workspace. Powerful querying, filtering, sorting, and pagination out of the box.

### Auto-Generated

APIs created with your tables

### CRUD Operations

Create, read, update, delete

### Secure by Default

RLS policies enforced

## Base URL
Copy
```
# Production
https://api.algorithmshift.ai/api/v1

# Your workspace API base
https://api.algorithmshift.ai/api/v1/ws/{workspaceSlug}
```

## Authentication

All API requests require authentication using API keys:

### API Key Authentication

#### Authorization Header
Copy
```
Authorization: Bearer YOUR_API_KEY
```

#### Example Request
Copy
```
curl -X GET \
  https://api.algorithmshift.ai/api/v1/tables/tasks \
  -H "Authorization: Bearer as_..." \
  -H "Content-Type: application/json"
```

### API Key Security

- • Never commit API keys to version control
- • Store keys in environment variables
- • Use different keys for development and production
- • Rotate keys regularly

## Standard Endpoints

Every table in your workspace automatically gets these endpoints:

### List Records

Get all records from a table
GETCopy
```
GET /api/v1/tables/{table_name}

# Example
GET /api/v1/tables/tasks

# Response
{
  "success": true,
  "data": [
    {
      "id": "task-1",
      "title": "Complete documentation",
      "status": "pending",
      "created_at": "2024-01-15T10:30:00Z"
    },
    {
      "id": "task-2",
      "title": "Review PR",
      "status": "completed",
      "created_at": "2024-01-14T15:20:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "pageSize": 20,
    "total": 2
  }
}
```

### Get Single Record

Retrieve a specific record by ID
GETCopy
```
GET /api/v1/tables/{table_name}/{id}

# Example
GET /api/v1/tables/tasks/task-1

# Response
{
  "success": true,
  "data": {
    "id": "task-1",
    "title": "Complete documentation",
    "description": "Write comprehensive API docs",
    "status": "pending",
    "priority": "high",
    "assigned_to": "user-123",
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2024-01-15T10:30:00Z"
  }
}
```

### Create Record

Insert a new record
POSTCopy
```
POST /api/v1/tables/{table_name}
Content-Type: application/json

# Request Body
{
  "title": "New task",
  "description": "Task description",
  "status": "pending",
  "priority": "medium"
}

# Response
{
  "success": true,
  "data": {
    "id": "task-3",
    "title": "New task",
    "description": "Task description",
    "status": "pending",
    "priority": "medium",
    "created_at": "2024-01-15T11:00:00Z"
  }
}
```

### Update Record

Modify an existing record
PUTCopy
```
PUT /api/v1/tables/{table_name}/{id}
Content-Type: application/json

# Request Body
{
  "status": "completed",
  "completed_at": "2024-01-15T12:00:00Z"
}

# Response
{
  "success": true,
  "data": {
    "id": "task-3",
    "title": "New task",
    "status": "completed",
    "completed_at": "2024-01-15T12:00:00Z",
    "updated_at": "2024-01-15T12:00:00Z"
  }
}
```

### Delete Record

Remove a record
DELETECopy
```
DELETE /api/v1/tables/{table_name}/{id}

# Example
DELETE /api/v1/tables/tasks/task-3

# Response
{
  "success": true,
  "message": "Record deleted successfully"
}
```

## Query Parameters

Powerful querying capabilities built into every endpoint:

### Filtering

#### Exact Match
Copy
```
# Filter by status
GET /api/v1/tables/tasks?status=pending

# Multiple conditions (AND)
GET /api/v1/tables/tasks?status=pending&priority=high
```

#### Comparison Operators
OperatorSyntaxExampleGreater than`[gt]``priority[gt]=3`Greater or equal`[gte]``created_at[gte]=2024-01-01`Less than`[lt]``price[lt]=100`Less or equal`[lte]``quantity[lte]=10`Not equal`[ne]``status[ne]=archived`IN list`[in]``status[in]=pending,active`LIKE pattern`[like]``title[like]=%urgent%`
#### Examples
Copy
```
# Tasks created after a date
GET /api/v1/tables/tasks?created_at[gte]=2024-01-01

# Price between range
GET /api/v1/tables/products?price[gte]=50&price[lte]=200

# Status is either pending or active
GET /api/v1/tables/tasks?status[in]=pending,active

# Title contains "urgent"
GET /api/v1/tables/tasks?title[like]=%urgent%
```

### Sorting
Copy
```
# Sort by created_at (ascending)
GET /api/v1/tables/tasks?sort=created_at

# Sort by created_at (descending)
GET /api/v1/tables/tasks?sort=-created_at

# Multiple sort fields
GET /api/v1/tables/tasks?sort=priority,-created_at

# Sorts by priority (asc), then by created_at (desc)
```

### Pagination
Copy
```
# Page-based pagination
GET /api/v1/tables/tasks?page=1&pageSize=20

# Offset-based pagination
GET /api/v1/tables/tasks?limit=20&offset=0

# Response includes pagination info
{
  "success": true,
  "data": [...],
  "pagination": {
    "page": 1,
    "pageSize": 20,
    "total": 150,
    "totalPages": 8
  }
}
```

### Field Selection
Copy
```
# Select specific fields only
GET /api/v1/tables/tasks?fields=id,title,status

# Response contains only requested fields
{
  "success": true,
  "data": [
    {
      "id": "task-1",
      "title": "Complete documentation",
      "status": "pending"
    }
  ]
}

# Exclude specific fields
GET /api/v1/tables/tasks?exclude=description,metadata
```

### Foreign Key Expansion
Copy
```
# Expand foreign key relationships
GET /api/v1/tables/tasks?expand=assigned_user,project

# Response includes full related objects
{
  "success": true,
  "data": [
    {
      "id": "task-1",
      "title": "Complete documentation",
      "assigned_user": {
        "id": "user-123",
        "name": "John Doe",
        "email": "john@example.com"
      },
      "project": {
        "id": "proj-456",
        "name": "Platform Development",
        "status": "active"
      }
    }
  ]
}
```

## Batch Operations

Perform operations on multiple records at once:

### Batch Create
Copy
```
POST /api/v1/tables/tasks/batch
Content-Type: application/json

{
  "records": [
    { "title": "Task 1", "status": "pending" },
    { "title": "Task 2", "status": "pending" },
    { "title": "Task 3", "status": "pending" }
  ]
}

# Response
{
  "success": true,
  "data": [
    { "id": "task-10", "title": "Task 1", ... },
    { "id": "task-11", "title": "Task 2", ... },
    { "id": "task-12", "title": "Task 3", ... }
  ]
}
```

### Batch Update
Copy
```
PUT /api/v1/tables/tasks/batch
Content-Type: application/json

{
  "ids": ["task-1", "task-2", "task-3"],
  "data": {
    "status": "completed"
  }
}

# Response
{
  "success": true,
  "updated": 3
}
```

## Error Responses

Standard error response format:

#### Error Format
Copy
```
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": {
      "field": "email",
      "issue": "Invalid email format"
    }
  }
}
```

#### HTTP Status Codes
CodeMeaningDescription`200`OKRequest successful`201`CreatedResource created successfully`400`Bad RequestInvalid request data`401`UnauthorizedMissing or invalid API key`403`ForbiddenInsufficient permissions`404`Not FoundResource does not exist`429`Too Many RequestsRate limit exceeded`500`Internal Server ErrorServer error occurred
## Rate Limiting

### Rate Limits

- Standard Tier: 1,000 requests per minute
- Pro Tier: 5,000 requests per minute
- Enterprise: Custom limits

Rate limit headers are included in every response:
Copy
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 987
X-RateLimit-Reset: 1642345678
```

## Learn More
[### GraphQL API

Query your data with GraphQL](https://www.algorithmshift.ai/docs/api/graphql)[### API Authentication

Learn about API key management](https://www.algorithmshift.ai/docs/api/auth)[### Webhooks

Receive real-time event notifications](https://www.algorithmshift.ai/docs/api/webhooks)[### SDKs & Libraries

Client libraries for popular languages](https://www.algorithmshift.ai/docs/sdks)
