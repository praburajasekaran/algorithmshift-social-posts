# Error Handling - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/workflows/errors  
**Scraped:** 2025-12-10 14:03:33

**Description:** Handle errors in workflows with retries, fallbacks, and notifications.

---

Error Handling - AlgorithmShift Documentation | AlgorithmShiftDocumentationWorkflows
# Error Handling

Build resilient workflows with automatic retries, fallback paths, and error notifications.

### Automatic Retries

Retry failed actions

### Fallback Paths

Alternative execution paths

### Notifications

Alert on failures

## Error Handling Configuration
Copy
```
{
  "name": "Process Payment",
  "actions": [
    {
      "type": "http",
      "url": "https://api.stripe.com/v1/charges",
      "method": "POST",
      "body": { "amount": "{{ order.total }}" }
    }
  ],
  "onError": {
    "retry": {
      "enabled": true,
      "attempts": 3,
      "delay": 5000,        // 5 seconds
      "backoff": "exponential"  // 5s, 10s, 20s
    },
    "notifications": [
      {
        "type": "email",
        "to": ["admin@company.com"],
        "subject": "Workflow Failed: {{ workflow.name }}",
        "body": "Error: {{ error.message }}"
      },
      {
        "type": "slack",
        "channel": "#alerts",
        "message": "⚠️ Workflow failed: {{ error.message }}"
      }
    ],
    "fallback": [
      {
        "type": "database.update",
        "table": "orders",
        "where": { "id": "{{ order.id }}" },
        "data": { "status": "payment_failed" }
      }
    ],
    "rollback": true  // Undo previous actions in transaction
  }
}
```

## Retry Strategies

### Fixed Delay
Copy
```
{
  "retry": {
    "attempts": 3,
    "delay": 5000,
    "backoff": "fixed"
  }
}

// Retries at:
// 5s, 5s, 5s
```

### Exponential Backoff
Copy
```
{
  "retry": {
    "attempts": 4,
    "delay": 1000,
    "backoff": "exponential"
  }
}

// Retries at:
// 1s, 2s, 4s, 8s
```
