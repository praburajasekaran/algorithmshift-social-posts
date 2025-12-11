# Installation - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/installation  
**Scraped:** 2025-12-10 14:02:31

**Description:** Complete installation guide for AlgorithmShift platform. Set up your account, workspace, and start building applications.

---

Installation - AlgorithmShift Documentation | AlgorithmShiftDocumentationGetting Started
# Installation & Setup

Get AlgorithmShift set up and ready to use. This guide covers account creation, workspace setup, and initial configuration.

### 5 Minutes

Setup time

### Cloud-Based

No installation required

### Free to Start

No credit card needed

## Step 1: Create Your Account

Sign up for a free AlgorithmShift account to get started.
1
### Visit the Sign-Up Page

Navigate to the registration page to create your account.
Copy
```
https://app.algorithmshift.ai/auth/signup
```
2
### Choose Your Sign-Up Method

Email & Password

Traditional email registration

- • Email verification required
- • Strong password (8+ chars)
- • 2FA available

OAuth Providers

Sign up with existing account

- • Google
- • Microsoft
- • GitHub
3
### Verify Your Email

Check your inbox for a verification email and click the confirmation link.

Note: Check your spam folder if you don't see the email within 5 minutes.

## Step 2: Complete Your Profile

Add some basic information to personalize your account.
Full Name
John Doe
Company (Optional)
Acme Inc.
Role
Developer, Designer, Product Manager...
Use Case
Internal tools, Customer portal...

## Step 3: Create Your First Workspace

A workspace is your isolated development environment where you'll build and manage applications.

### What is a Workspace?

Each workspace provides:

Isolated Database

PostgreSQL schema with full control

REST & GraphQL APIs

Auto-generated endpoints

Storage Bucket

AWS S3 for file uploads

Team Collaboration

Invite team members

Authentication System

Built-in user management

Workflow Engine

Automation and business logic

### Workspace Configuration
Workspace Name
My Company

Displayed in the UI and notifications
Workspace Slug
my-company

Used in URLs: app.algorithmshift.ai/my-company/...
Region (Optional)
us-east-1 (N. Virginia)

Choose the closest region for better performance

### Workspace Provisioning

When you create a workspace, AlgorithmShift automatically provisions:
Copy
```
// Backend infrastructure created
{
  "database": {
    "type": "PostgreSQL 15",
    "schema": "ws_my_company",
    "maxConnections": 100
  },
  "storage": {
    "provider": "AWS S3",
    "bucket": "algorithmshift-ws-my-company",
    "region": "us-east-1"
  },
  "apis": {
    "rest": "https://api.algorithmshift.ai/v1/ws/my-company",
    "graphql": "https://api.algorithmshift.ai/graphql/my-company"
  }
}
```

## Step 4: Get Your API Keys

Generate API keys to interact with your workspace programmatically.

### Generate an API Key

1. 1. Navigate to Access Control → API Security → API Keys
1. 2. Click "Create API Key"
1. 3. Enter a name (e.g., "Development Key")
1. 4. Select your user account
1. 5. Optionally set an expiration date
1. 6. Click "Create"

Important

Copy your API key immediately. It will only be shown once for security reasons.

### Using Your API Key

#### Environment Variable
Copy
```
# .env file
ALGORITHMSHIFT_API_KEY=as_1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
```

#### In API Requests
Copy
```
fetch('https://api.algorithmshift.ai/api/v1/tables/users', {
  headers: {
    'Authorization': 'Bearer as_1234567890abcdef...',
    'Content-Type': 'application/json'
  }
})
```

## Step 5: Configure Environment

Set up your development environment for the best experience.

### Supported Browsers

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

### Optional: CLI Tools

Install CLI for advanced features:
Copy
```
npm install -g @algorithmshift/cli

# Login to CLI
asft login

# Init a new project
asft init my-project
```

## Verification Checklist

Make sure everything is set up correctly before proceeding.

Account created and email verified

Profile completed

Workspace created and provisioned

API key generated and saved

Browser compatibility checked

## Next Steps

Now that you're all set up, here's what to do next:
[### Follow the Quick Start

Build your first application in 5 minutes](https://www.algorithmshift.ai/docs/quick-start)[### Understand Project Structure

Learn how workspaces, apps, and resources are organized](https://www.algorithmshift.ai/docs/project-structure)[### Explore Tutorials

Step-by-step guides for common use cases](https://www.algorithmshift.ai/docs/tutorials)[### API Reference

Complete API documentation](https://www.algorithmshift.ai/docs/api)
### Need Help with Installation?

If you encounter any issues during setup:
[Community Support →](https://www.algorithmshift.ai/docs/community)[Email Support →](mailto:support@algorithmshift.ai)[Troubleshooting →](https://www.algorithmshift.ai/docs/troubleshooting)
