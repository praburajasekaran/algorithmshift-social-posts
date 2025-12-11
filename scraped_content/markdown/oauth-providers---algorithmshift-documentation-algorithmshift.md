# OAuth Providers - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/auth/oauth  
**Scraped:** 2025-12-10 14:03:57

**Description:** Configure social login with Google, Microsoft, GitHub, and other OAuth providers.

---

OAuth Providers - AlgorithmShift Documentation | AlgorithmShiftDocumentationAuthentication
# OAuth Providers

Enable social login with Google, Microsoft, GitHub, and other OAuth 2.0 providers.

## Supported Providers

### Google

### Microsoft

### GitHub

### LinkedIn

## Configuring Google OAuth
1
### Get Google Credentials

1. 1. Go to Google Cloud Console
1. 2. Create new project or select existing
1. 3. Enable Google+ API
1. 4. Create OAuth 2.0 credentials
1. 5. Add authorized redirect URI
2
### Configure in AlgorithmShift
Copy
```
{
  "provider": "google",
  "clientId": "123456789.apps.googleusercontent.com",
  "clientSecret": "{{ secrets.GOOGLE_CLIENT_SECRET }}",
  "scope": ["email", "profile"],
  "callbackUrl": "https://app.algorithmshift.ai/auth/callback/google"
}
```
