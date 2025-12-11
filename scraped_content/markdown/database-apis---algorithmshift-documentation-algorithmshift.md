# Database & APIs - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/database  
**Scraped:** 2025-12-10 14:02:39

**Description:** Build and manage PostgreSQL databases with auto-generated REST and GraphQL APIs.

---

Database & APIs - AlgorithmShift Documentation | AlgorithmShiftDocumentationDatabase & APIs
# Database & Data Management

Every workspace includes a PostgreSQL database with auto-generated REST and GraphQL APIs. Design your schema visually, and APIs are created instantly.

### PostgreSQL 15

Full-featured relational database

### Auto APIs

REST & GraphQL generated automatically

### Visual Designer

Design schemas with drag & drop

### Row-Level Security

Built-in data access control

### Relationships

Foreign keys and joins

### Views

Complex queries as virtual tables

## How It Works

When you create a workspace, AlgorithmShift provisions a dedicated PostgreSQL database schema with full isolation.

### Database Provisioning
Copy
```
// Your workspace database schema
Schema: ws_my_company

// Connection details (available in workspace settings)
{
  "host": "db.algorithmshift.ai",
  "port": 5432,
  "database": "algorithmshift",
  "schema": "ws_my_company",
  "ssl": true,
  "maxConnections": 100
}
```

## Creating Tables

Use the visual table designer to create database tables without writing SQL.
1
### Navigate to Tables

Go to Access Control → Data Management → Tables
Copy
```
// URL Pattern
/{workspaceId}/access-control/data-management/tables
```
2
### Define Table Structure

Click "Create Table" and define columns:
ColumnTypeConstraints`id`UUIDPRIMARY KEY, DEFAULT uuid_generate_v4()`name`VARCHAR(255)NOT NULL`email`VARCHAR(255)UNIQUE, NOT NULL`status`VARCHAR(50)DEFAULT 'active'`created_at`TIMESTAMPDEFAULT NOW()3
### APIs Created Automatically

As soon as you create a table, REST APIs are generated:
Copy
```
# List all records
GET /api/v1/tables/customers

# Create a record
POST /api/v1/tables/customers
Body: { "name": "John Doe", "email": "john@example.com" }

# Get single record
GET /api/v1/tables/customers/:id

# Update a record
PUT /api/v1/tables/customers/:id
Body: { "status": "inactive" }

# Delete a record
DELETE /api/v1/tables/customers/:id
```

## Supported Data Types

AlgorithmShift supports all standard PostgreSQL data types:

### Text Types

- VARCHAR(n) - Variable length
- TEXT - Unlimited length
- CHAR(n) - Fixed length

### Numeric Types

- INTEGER - Whole numbers
- BIGINT - Large integers
- DECIMAL(p,s) - Exact decimals
- FLOAT - Floating point

### Date & Time

- TIMESTAMP - Date and time
- DATE - Date only
- TIME - Time only
- INTERVAL - Time span

### Boolean & Binary

- BOOLEAN - True/false
- BYTEA - Binary data
- UUID - Unique identifier

### JSON Types

- JSON - JSON data
- JSONB - Binary JSON (faster)

### Arrays & Special

- ARRAY - Array of values
- ENUM - Enumerated type
- POINT - Geometric point

## Query Your Data

The auto-generated APIs support powerful querying capabilities:

### Filtering
Copy
```
# Exact match
GET /api/v1/tables/tasks?status=active

# Comparison operators
GET /api/v1/tables/tasks?created_at[gte]=2024-01-01

# Multiple conditions (AND)
GET /api/v1/tables/tasks?status=active&priority=high

# IN operator
GET /api/v1/tables/tasks?status[in]=active,pending

# Pattern matching
GET /api/v1/tables/tasks?title[like]=%urgent%
```

### Sorting & Pagination
Copy
```
# Sort by field (ascending)
GET /api/v1/tables/tasks?sort=created_at

# Sort descending
GET /api/v1/tables/tasks?sort=-created_at

# Multiple sort fields
GET /api/v1/tables/tasks?sort=priority,-created_at

# Pagination
GET /api/v1/tables/tasks?page=1&pageSize=20

# Limit results
GET /api/v1/tables/tasks?limit=10&offset=0
```

### Field Selection
Copy
```
# Select specific fields
GET /api/v1/tables/tasks?fields=id,title,status

# Exclude fields
GET /api/v1/tables/tasks?exclude=description,metadata

# Expand foreign keys
GET /api/v1/tables/tasks?expand=assigned_user,project
```

## Relationships

Define relationships between tables with foreign keys:

### One-to-Many Relationship

Example: A project has many tasks
Copy
```
// tasks table
{
  "id": "uuid",
  "title": "varchar(255)",
  "project_id": "uuid",  // Foreign key
  "created_at": "timestamp"
}

// Foreign key constraint
ALTER TABLE tasks
ADD CONSTRAINT fk_tasks_project
FOREIGN KEY (project_id)
REFERENCES projects(id)
ON DELETE CASCADE;
```

Query with expansion:
Copy
```
GET /api/v1/tables/tasks?expand=project

Response:
{
  "data": [{
    "id": "123",
    "title": "Task 1",
    "project": {
      "id": "456",
      "name": "Project Alpha",
      "status": "active"
    }
  }]
}
```

### Many-to-Many Relationship

Example: Users can belong to multiple groups
Copy
```
// Junction table: user_groups
{
  "id": "uuid",
  "user_id": "uuid",
  "group_id": "uuid",
  "created_at": "timestamp"
}

// Query users with their groups
GET /api/v1/tables/users?expand=groups

Response:
{
  "data": [{
    "id": "user-1",
    "name": "John Doe",
    "groups": [
      { "id": "group-1", "name": "Developers" },
      { "id": "group-2", "name": "Admins" }
    ]
  }]
}
```

## Learn More
[### Schema Designer

Visual tool for designing database schemas](https://www.algorithmshift.ai/docs/database/schema)[### REST APIs

Complete REST API reference](https://www.algorithmshift.ai/docs/database/rest)[### Database Views

Create complex queries as views](https://www.algorithmshift.ai/docs/database/views)[### Row-Level Security

Secure your data with RLS policies](https://www.algorithmshift.ai/docs/auth/rls)
