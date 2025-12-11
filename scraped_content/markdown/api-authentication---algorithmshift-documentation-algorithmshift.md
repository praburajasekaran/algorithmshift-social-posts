# API Authentication - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/api/auth  
**Scraped:** 2025-12-10 14:03:03

**Description:** Authenticate API requests with API keys. Generate, manage, and secure your keys.

---

API Authentication - AlgorithmShift Documentation | AlgorithmShiftDocumentationAPI Reference
# API Authentication

Authenticate API requests using API keys. Secure, manageable, and traceable access to your workspace.

## Authentication Methods

### API Keys (Recommended)
Copy
```
Authorization: Bearer as_1234567890abcdef...

# Example request
curl -X GET \
  https://api.algorithmshift.ai/api/v1/tables/tasks \
  -H "Authorization: Bearer as_..." \
  -H "Content-Type: application/json"
```

### Session-Based

For browser-based apps, use session cookies (automatically handled by NextAuth).
Copy
```
// Cookies set automatically
Cookie: next-auth.session-token=...
```

## Generating API Keys
1
### Navigate to API Keys

Go to Access Control → API Security → API Keys
2
### Create API Key

Key Name

Production API Key

User

Select workspace_admin user

Expiration

90 days (recommended)
3
### Copy and Store Securely

Important!

API keys are only shown once. Store them securely in environment variables or secrets manager.

## Security Best Practices

Store API keys in environment variables, never in code

Use different keys for development and production

Set expiration dates on all API keys

Rotate keys every 90 days

Revoke unused or compromised keys immediately

Monitor API key usage for suspicious activity

Never commit keys to version control

Use secrets manager for production keys
