# GraphQL API - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/api/graphql  
**Scraped:** 2025-12-10 14:03:02

**Description:** Query your data with GraphQL. Flexible queries and precise data fetching.

---

GraphQL API - AlgorithmShift Documentation | AlgorithmShiftDocumentationAPI Reference
# GraphQL API

Query your workspace data with GraphQL. Request exactly what you need with a single query.

### GraphQL Support

GraphQL support is coming soon to AlgorithmShift. Currently, we recommend using our powerful REST API with field selection and foreign key expansion for similar capabilities.

## GraphQL Endpoint (Coming Soon)
Copy
```
# GraphQL endpoint (planned)
https://api.algorithmshift.ai/graphql/{workspace}

# Example query
query GetTasks {
  tasks(where: { status: "active" }, limit: 10) {
    id
    title
    status
    assignedUser {
      name
      email
    }
    project {
      name
    }
  }
}
```

## Current Alternative: REST API with Expansion

You can achieve similar results with our REST API:
Copy
```
GET /api/v1/tables/tasks?status=active&limit=10&expand=assignedUser,project&fields=id,title,status

// Returns
{
  "data": [
    {
      "id": "task-1",
      "title": "Complete feature",
      "status": "active",
      "assignedUser": {
        "name": "John Doe",
        "email": "john@example.com"
      },
      "project": {
        "name": "Platform Development"
      }
    }
  ]
}
```
