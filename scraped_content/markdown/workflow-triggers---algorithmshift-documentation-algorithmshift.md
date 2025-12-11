# Workflow Triggers - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/workflows/triggers  
**Scraped:** 2025-12-10 14:03:30

**Description:** Complete reference of all available workflow triggers. Webhooks, schedules, database events, and more.

---

Workflow Triggers - AlgorithmShift Documentation | AlgorithmShiftDocumentationWorkflows
# Workflow Triggers

Triggers start workflow execution. Choose from webhooks, schedules, database events, emails, RSS feeds, and application events.

### Webhook

HTTP POST requests

### Schedule (CRON)

Time-based execution

### Database Events

Table insert/update/delete

### Email (Mailhook)

Incoming emails

### RSS Feed

New RSS items

### App Event

Application-specific events

## Trigger Configurations

### Webhook Trigger

#### Configuration
Copy
```
{
  "type": "webhook",
  "authentication": {
    "type": "api_key",
    "headerName": "X-Webhook-Secret",
    "secret": "{{ secrets.WEBHOOK_SECRET }}"
  },
  "ipWhitelist": [
    "52.1.2.3",
    "52.1.2.4"
  ]
}
```

#### Webhook URL
`https://api.algorithmshift.ai/webhooks/wf_abc123`
#### Trigger Data
Copy
```
// Access webhook payload
{{ trigger.body }}
{{ trigger.headers }}
{{ trigger.query }}
```

### Schedule (CRON) Trigger

#### Common Patterns
`*/5 * * * *`
Every 5 minutes
`0 * * * *`
Every hour
`0 9 * * MON-FRI`
9 AM weekdays
`0 0 1 * *`
1st of month

#### Configuration
Copy
```
{
  "type": "cron",
  "schedule": "0 9 * * *",
  "timezone": "America/New_York",
  "enabled": true
}
```

### Database Event Trigger
Copy
```
{
  "type": "database.insert",
  "table": "orders",
  "conditions": {
    "status": "pending",
    "total[gt]": 100
  }
}

// Trigger data
{
  "trigger": {
    "event": "insert",
    "table": "orders",
    "record": {
      "id": "order-123",
      "status": "pending",
      "total": 150,
      "customer_id": "cust-456"
    },
    "old": null  // null for insert
  }
}
```

### Email (Mailhook) Trigger

#### Email Address
`support-wf_abc@mail.algorithmshift.ai`
#### Email Data
Copy
```
{
  "from": "customer@example.com",
  "to": "support@...",
  "subject": "Help needed",
  "body": "Message text...",
  "attachments": [...]
}
```
