# Webhooks - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/api/webhooks  
**Scraped:** 2025-12-10 14:03:05

**Description:** Receive real-time event notifications via webhooks. Subscribe to database changes and workflow events.

---

Webhooks - AlgorithmShift Documentation | AlgorithmShiftDocumentationAPI Reference
# Webhooks

Receive real-time notifications when events occur. Subscribe to database changes, workflow completions, and custom events.

### Database Events

Table insert/update/delete

### Workflow Events

Workflow started/completed

### Secure Delivery

Signed with HMAC

## Creating a Webhook

#### Webhook Configuration
Copy
```
{
  "name": "Order Notifications",
  "url": "https://yourapp.com/webhooks/orders",
  "events": [
    "database.insert.orders",
    "database.update.orders"
  ],
  "headers": {
    "Authorization": "Bearer your-token"
  },
  "active": true
}
```

#### Webhook Payload
Copy
```
{
  "event": "database.insert.orders",
  "timestamp": "2024-01-15T10:30:00Z",
  "data": {
    "id": "order-123",
    "customer_id": "cust-456",
    "total": 150,
    "status": "pending"
  },
  "signature": "sha256=..."
}
```

## Verifying Webhooks
Copy
```
// Verify webhook signature
const crypto = require('crypto');

function verifyWebhook(payload, signature, secret) {
  const hmac = crypto
    .createHmac('sha256', secret)
    .update(JSON.stringify(payload))
    .digest('hex');
  
  return `sha256=${hmac}` === signature;
}

// In your webhook handler
app.post('/webhooks/orders', (req, res) => {
  const signature = req.headers['x-webhook-signature'];
  
  if (!verifyWebhook(req.body, signature, process.env.WEBHOOK_SECRET)) {
    return res.status(401).send('Invalid signature');
  }
  
  // Process webhook
  const { event, data } = req.body;
  console.log('Received event:', event, data);
  
  res.status(200).send('OK');
});
```
