# Workflows - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/workflows  
**Scraped:** 2025-12-10 14:02:36

**Description:** Automate business processes with visual workflows. Connect triggers, actions, and conditional logic.

---

Workflows - AlgorithmShift Documentation | AlgorithmShiftDocumentationWorkflows
# Workflow Automation

Automate business logic and processes with visual workflows. React to events, call APIs, manipulate data, and orchestrate complex operations without code.

### Visual Builder

Drag-and-drop workflow designer

### 20+ Triggers

Webhooks, schedules, database events

### 50+ Actions

APIs, emails, database operations

### Conditional Logic

Branches, loops, and dynamic routing

### Error Handling

Retries, fallbacks, notifications

### Real-time Monitoring

Logs, metrics, and debugging

## What are Workflows?

Workflows automate repetitive tasks and complex business logic. They consist of:

### Triggers

Events that start the workflow

### Actions

Operations to perform

### Logic

Conditional flow control

## Available Triggers

Workflows can be triggered by various events:

### Webhook

HTTP POST request to trigger the workflow
Copy
```
// Webhook URL (auto-generated)
POST https://api.algorithmshift.ai/webhooks/{workflow_id}

// Payload is available in workflow as {{ trigger.body }}
{
  "event": "order.created",
  "order_id": "12345",
  "customer": {
    "name": "John Doe",
    "email": "john@example.com"
  }
}
```

### Schedule (CRON)

Run workflows on a schedule

Common Schedules
`0 * * * *`
Every hour
`0 9 * * *`
Daily at 9 AM
`0 0 * * 0`
Weekly on Sunday
`0 0 1 * *`
Monthly on 1st

Configuration
Copy
```
{
  "type": "cron",
  "schedule": "0 9 * * *",
  "timezone": "America/New_York"
}
```

### Database Events

Triggered when data changes
Copy
```
// Configuration
{
  "type": "database.insert",
  "table": "orders",
  "conditions": {
    "status": "pending",
    "total[gt]": 100
  }
}

// Available events:
- database.insert   // New record created
- database.update   // Record updated
- database.delete   // Record deleted

// Trigger data available as {{ trigger.record }}
{
  "id": "123",
  "status": "pending",
  "total": 150,
  "customer_id": "456"
}
```

### Email (Mailhook)

Triggered by incoming emails
Copy
```
// Email address (auto-generated)
support-{workflow_id}@mail.algorithmshift.ai

// Email data available as:
{
  "from": "customer@example.com",
  "to": "support@yourapp.com",
  "subject": "Help with order",
  "body": "I need assistance...",
  "attachments": [...]
}
```

## Workflow Actions

Perform operations within your workflows:

### Database Operations

#### Query Records
Copy
```
{
  "type": "database.query",
  "table": "users",
  "filters": {
    "email": "{{ trigger.body.email }}"
  },
  "assign": "user"
}
```

#### Create Record
Copy
```
{
  "type": "database.insert",
  "table": "tasks",
  "data": {
    "title": "Follow up",
    "user_id": "{{ user.id }}",
    "status": "pending"
  }
}
```

#### Update Record
Copy
```
{
  "type": "database.update",
  "table": "orders",
  "where": { "id": "{{ order.id }}" },
  "data": {
    "status": "processing"
  }
}
```

#### Delete Record
Copy
```
{
  "type": "database.delete",
  "table": "temp_data",
  "where": {
    "created_at[lt]": "{{ now() - 86400 }}"
  }
}
```

### API Calls
Copy
```
{
  "type": "http",
  "method": "POST",
  "url": "https://api.stripe.com/v1/charges",
  "headers": {
    "Authorization": "Bearer {{ secrets.STRIPE_KEY }}",
    "Content-Type": "application/json"
  },
  "body": {
    "amount": "{{ order.total * 100 }}",
    "currency": "usd",
    "customer": "{{ order.customer_id }}"
  },
  "assign": "payment"
}
```

### Send Email
Copy
```
{
  "type": "sendEmail",
  "to": "{{ order.customer.email }}",
  "subject": "Order Confirmation #{{ order.id }}",
  "template": "order-confirmation",
  "data": {
    "order": "{{ order }}",
    "customer": "{{ order.customer }}",
    "items": "{{ order.items }}"
  }
}

// Or send plain email
{
  "type": "sendEmail",
  "to": "{{ user.email }}",
  "subject": "Welcome!",
  "body": "Thank you for signing up..."
}
```

## Conditional Logic

Control workflow execution with conditions and branches:

### If/Else Branches
Copy
```
{
  "type": "condition",
  "condition": "{{ order.total > 100 }}",
  "true": [
    {
      "type": "sendEmail",
      "to": "{{ order.customer.email }}",
      "subject": "Free shipping applied!"
    },
    {
      "type": "database.update",
      "table": "orders",
      "where": { "id": "{{ order.id }}" },
      "data": { "shipping_cost": 0 }
    }
  ],
  "false": [
    {
      "type": "database.update",
      "table": "orders",
      "where": { "id": "{{ order.id }}" },
      "data": { "shipping_cost": 9.99 }
    }
  ]
}
```

### Loops
Copy
```
// For each item in array
{
  "type": "loop",
  "items": "{{ order.items }}",
  "itemName": "item",
  "actions": [
    {
      "type": "database.update",
      "table": "inventory",
      "where": { "product_id": "{{ item.product_id }}" },
      "data": {
        "quantity": "{{ inventory.quantity - item.quantity }}"
      }
    },
    {
      "type": "sendEmail",
      "to": "warehouse@company.com",
      "subject": "Ship: {{ item.name }}",
      "body": "Quantity: {{ item.quantity }}"
    }
  ]
}
```

## Example Workflow

Here's a complete workflow that processes new orders:

### Order Processing Workflow

Triggered when a new order is created
Copy
```
{
  "name": "Process New Order",
  "trigger": {
    "type": "database.insert",
    "table": "orders"
  },
  "actions": [
    // 1. Check inventory
    {
      "type": "database.query",
      "table": "inventory",
      "filters": { "product_id": "{{ trigger.record.product_id }}" },
      "assign": "inventory"
    },
    
    // 2. Branch based on inventory
    {
      "type": "condition",
      "condition": "{{ inventory.quantity >= trigger.record.quantity }}",
      "true": [
        // Process payment
        {
          "type": "http",
          "method": "POST",
          "url": "https://api.stripe.com/v1/charges",
          "headers": {
            "Authorization": "Bearer {{ secrets.STRIPE_KEY }}"
          },
          "body": {
            "amount": "{{ trigger.record.total * 100 }}",
            "customer": "{{ trigger.record.customer_id }}"
          },
          "assign": "payment"
        },
        
        // Update inventory
        {
          "type": "database.update",
          "table": "inventory",
          "where": { "product_id": "{{ trigger.record.product_id }}" },
          "data": {
            "quantity": "{{ inventory.quantity - trigger.record.quantity }}"
          }
        },
        
        // Send confirmation email
        {
          "type": "sendEmail",
          "to": "{{ trigger.record.customer.email }}",
          "subject": "Order Confirmed #{{ trigger.record.id }}",
          "template": "order-confirmation",
          "data": {
            "order": "{{ trigger.record }}",
            "payment": "{{ payment }}"
          }
        },
        
        // Update order status
        {
          "type": "database.update",
          "table": "orders",
          "where": { "id": "{{ trigger.record.id }}" },
          "data": { "status": "confirmed" }
        }
      ],
      "false": [
        // Notify out of stock
        {
          "type": "sendEmail",
          "to": "{{ trigger.record.customer.email }}",
          "subject": "Out of Stock",
          "template": "out-of-stock"
        },
        
        // Alert inventory team
        {
          "type": "sendEmail",
          "to": "inventory@company.com",
          "subject": "Low Stock Alert",
          "body": "Product {{ trigger.record.product.name }} is out of stock"
        }
      ]
    }
  ],
  
  // Error handling
  "onError": {
    "retry": {
      "attempts": 3,
      "delay": 5000
    },
    "notify": ["admin@company.com"],
    "actions": [
      {
        "type": "database.update",
        "table": "orders",
        "where": { "id": "{{ trigger.record.id }}" },
        "data": { "status": "error" }
      }
    ]
  }
}
```

## Monitoring & Debugging

Track workflow executions and debug issues:

### Execution Logs

- View every workflow run
- See input/output for each step
- Execution duration and timing
- Error messages and stack traces

### Performance Metrics

- Success/failure rates
- Average execution time
- Trigger frequency
- Resource usage

## Learn More
[### Visual Builder

Learn the workflow builder interface](https://www.algorithmshift.ai/docs/workflows/builder)[### Triggers

Complete trigger reference](https://www.algorithmshift.ai/docs/workflows/triggers)[### Actions

All available workflow actions](https://www.algorithmshift.ai/docs/workflows/actions)[### Error Handling

Retries, fallbacks, and error recovery](https://www.algorithmshift.ai/docs/workflows/errors)
