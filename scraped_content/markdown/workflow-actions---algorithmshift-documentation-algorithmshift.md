# Workflow Actions - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/workflows/actions  
**Scraped:** 2025-12-10 14:03:32

**Description:** Complete catalog of workflow actions. Database operations, API calls, emails, and more.

---

Workflow Actions - AlgorithmShift Documentation | AlgorithmShiftDocumentationWorkflows
# Workflow Actions

50+ actions available for workflow automation. Perform database operations, call APIs, send emails, and integrate with external services.

### Database

12 actions

### HTTP/API

8 actions

### Communication

10 actions

### Logic

6 actions

### Data Transform

8 actions

### Integrations

20+ actions

## Database Actions

### database.query

Query records from a table
Copy
```
{
  "type": "database.query",
  "table": "customers",
  "filters": {
    "email": "{{ trigger.body.email }}"
  },
  "limit": 1,
  "assign": "customer"
}

// Result available as {{ customer }}
```

### database.insert

Create new record
Copy
```
{
  "type": "database.insert",
  "table": "leads",
  "data": {
    "name": "{{ trigger.body.name }}",
    "email": "{{ trigger.body.email }}",
    "source": "website",
    "status": "new"
  },
  "assign": "lead"
}
```

### database.update

Update existing record
Copy
```
{
  "type": "database.update",
  "table": "orders",
  "where": { "id": "{{ order.id }}" },
  "data": {
    "status": "shipped",
    "shipped_at": "{{ now() }}"
  }
}
```

## Communication Actions

### sendEmail
Copy
```
{
  "type": "sendEmail",
  "to": "{{ customer.email }}",
  "subject": "Order Confirmed #{{ order.id }}",
  "template": "order-confirmation",
  "data": {
    "customerName": "{{ customer.name }}",
    "orderTotal": "{{ order.total }}",
    "items": "{{ order.items }}"
  }
}
```

### slack.sendMessage
Copy
```
{
  "type": "slack.sendMessage",
  "channel": "#sales",
  "message": "New lead: {{ lead.name }} ({{ lead.email }})",
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*New Lead*\n{{ lead.company }}"
      }
    }
  ]
}
```
