# Agent Tools - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/ai/tools  
**Scraped:** 2025-12-10 14:03:39

**Description:** Give AI agents capabilities with tools: database access, API calls, workflows, and file operations.

---

Agent Tools - AlgorithmShift Documentation | AlgorithmShiftDocumentationAI Agents
# Agent Tools & Capabilities

Give your AI agents the ability to take actions. Connect to databases, APIs, workflows, and files.

### Database Access

Query and manipulate data
Copy
```
{
  "type": "database",
  "tables": ["customers", "orders"],
  "permissions": {
    "customers": ["read"],
    "orders": ["read", "update"]
  }
}
```

### HTTP API Calls

Call external APIs
Copy
```
{
  "type": "http_api",
  "name": "CRM API",
  "baseUrl": "https://api.crm.com",
  "auth": {
    "type": "bearer",
    "token": "{{ secrets.CRM_KEY }}"
  }
}
```

### Workflow Execution

Trigger workflows
Copy
```
{
  "type": "workflow",
  "workflows": [
    {
      "id": "create-ticket",
      "name": "Create Support Ticket"
    }
  ]
}
```

### File Operations

Read and write files
Copy
```
{
  "type": "files",
  "permissions": ["read", "write"],
  "allowedPaths": [
    "documents/*",
    "reports/*"
  ]
}
```

### RAG (Knowledge Base)

Search knowledge base
Copy
```
{
  "type": "rag",
  "collection": "support-docs",
  "maxResults": 5
}
```
