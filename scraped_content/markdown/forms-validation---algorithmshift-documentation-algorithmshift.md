# Forms & Validation - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/forms  
**Scraped:** 2025-12-10 14:03:19

**Description:** Build forms with validation, submission handling, and data binding. Connect to APIs and databases seamlessly.

---

Forms & Validation - AlgorithmShift Documentation | AlgorithmShiftDocumentationApp Builder
# Forms & Validation

Build powerful forms with built-in validation, error handling, and data submission. Connect directly to your database or APIs with zero configuration.

### Text Input

### Select
Choose option...
### Checkbox
I agree
### Textarea

## Creating a Form
1
### Add Form Components

Drag form components onto your canvas:

Text Input

Name, email, etc.

Select

Dropdowns

Checkbox

Boolean options

Date Picker

Date selection

File Upload

File attachments

Submit Button

Form submission
2
### Configure Validation

#### Built-in Validators

Required

Field must have value

Email

Valid email format

Min/Max Length

Character limits

Pattern (Regex)

Custom validation

#### Validation Example
Copy
```
// Email input validation
{
  "type": "email",
  "required": true,
  "validation": {
    "pattern": "^[^@]+@[^@]+\.[^@]+$",
    "message": "Please enter a valid email"
  }
}

// Password validation
{
  "type": "password",
  "required": true,
  "validation": {
    "minLength": 8,
    "pattern": "^(?=.*[A-Z])(?=.*[0-9]).*$",
    "message": "Min 8 chars, 1 uppercase, 1 number"
  }
}
```
3
### Handle Form Submission

Configure what happens when the form is submitted:
Copy
```
// Submit button configuration
{
  "onClick": {
    "type": "form_submit",
    "action": "create_record",
    "table": "contacts",
    "onSuccess": {
      "message": "Contact created successfully!",
      "redirect": "/contacts",
      "resetForm": true
    },
    "onError": {
      "message": "Failed to create contact",
      "showErrors": true
    }
  }
}
```

## Form Actions

Multiple ways to handle form data:

### Save to Database

Directly insert form data into a table
Copy
```
// Form submit action
{
  "type": "create_record",
  "table": "tasks",
  "data": {
    "title": "{{ form.title }}",
    "description": "{{ form.description }}",
    "status": "{{ form.status }}",
    "priority": "{{ form.priority }}",
    "assigned_to": "{{ currentUser.id }}"
  }
}

// Or use the simplified syntax
{
  "type": "create_record",
  "table": "tasks",
  "data": "{{ formData }}"  // Auto-maps all fields
}
```

### Call API

Submit to custom API endpoint
Copy
```
{
  "type": "api_call",
  "method": "POST",
  "url": "https://api.example.com/contacts",
  "headers": {
    "Authorization": "Bearer {{ secrets.API_KEY }}",
    "Content-Type": "application/json"
  },
  "body": {
    "name": "{{ form.name }}",
    "email": "{{ form.email }}",
    "message": "{{ form.message }}"
  },
  "onSuccess": {
    "message": "Message sent!",
    "resetForm": true
  }
}
```

### Trigger Workflow

Start a workflow with form data
Copy
```
{
  "type": "trigger_workflow",
  "workflowId": "process-lead",
  "data": {
    "name": "{{ form.name }}",
    "email": "{{ form.email }}",
    "company": "{{ form.company }}",
    "phone": "{{ form.phone }}"
  }
}
```

## Validation Patterns

Common validation scenarios:

### Email Validation
Copy
```
{
  "type": "email",
  "required": true,
  "validation": {
    "pattern": "^[^@]+@[^@]+\.[^@]+$",
    "message": "Invalid email address"
  }
}
```

### Phone Number
Copy
```
{
  "type": "tel",
  "required": true,
  "validation": {
    "pattern": "^\+?[1-9]\d{1,14}$",
    "message": "Invalid phone number"
  }
}
```

### URL Validation
Copy
```
{
  "type": "url",
  "required": true,
  "validation": {
    "pattern": "^https?://.*",
    "message": "Must be valid URL"
  }
}
```

### Custom Validation
Copy
```
{
  "validation": {
    "custom": "{{ value.length >= 10 }}",
    "message": "Min 10 characters"
  }
}
```

## Complete Form Example

Here's a complete contact form with validation and submission:
Copy
```
// Contact Form Configuration
{
  "formId": "contact-form",
  "fields": [
    {
      "id": "name",
      "type": "text",
      "label": "Full Name",
      "placeholder": "John Doe",
      "required": true,
      "validation": {
        "minLength": 2,
        "message": "Name must be at least 2 characters"
      }
    },
    {
      "id": "email",
      "type": "email",
      "label": "Email Address",
      "placeholder": "john@example.com",
      "required": true,
      "validation": {
        "pattern": "^[^@]+@[^@]+\.[^@]+$",
        "message": "Please enter a valid email"
      }
    },
    {
      "id": "phone",
      "type": "tel",
      "label": "Phone Number",
      "placeholder": "+1 (555) 123-4567",
      "required": false,
      "validation": {
        "pattern": "^\+?[1-9]\d{1,14}$",
        "message": "Invalid phone number"
      }
    },
    {
      "id": "subject",
      "type": "select",
      "label": "Subject",
      "required": true,
      "options": [
        { "value": "sales", "label": "Sales Inquiry" },
        { "value": "support", "label": "Technical Support" },
        { "value": "partnership", "label": "Partnership" },
        { "value": "other", "label": "Other" }
      ]
    },
    {
      "id": "message",
      "type": "textarea",
      "label": "Message",
      "placeholder": "How can we help you?",
      "required": true,
      "validation": {
        "minLength": 10,
        "maxLength": 500,
        "message": "Message must be 10-500 characters"
      }
    },
    {
      "id": "newsletter",
      "type": "checkbox",
      "label": "Subscribe to newsletter",
      "required": false
    }
  ],
  "submitButton": {
    "label": "Send Message",
    "action": {
      "type": "create_record",
      "table": "contact_submissions",
      "data": "{{ formData }}",
      "onSuccess": {
        "message": "Thank you! We'll get back to you soon.",
        "resetForm": true,
        "redirect": "/thank-you"
      },
      "onError": {
        "message": "Something went wrong. Please try again.",
        "showErrors": true
      }
    }
  }
}
```

## Form State Management

Access and manipulate form data:

### Form Data Variables
Copy
```
// Access form field values
{{ form.fieldName }}

// Examples:
{{ form.email }}        // Current email value
{{ form.name }}         // Current name value
{{ form.status }}       // Current status value

// All form data as object
{{ formData }}

// Form state
{{ form.isValid }}      // true if all validations pass
{{ form.isDirty }}      // true if any field changed
{{ form.isSubmitting }} // true during submission
{{ form.errors }}       // Object with validation errors
```

### Conditional Field Display
Copy
```
// Show field based on another field's value
{
  "id": "company_name",
  "type": "text",
  "label": "Company Name",
  "visible": "{{ form.account_type === 'business' }}"
}

// Show field based on checkbox
{
  "id": "shipping_address",
  "type": "textarea",
  "label": "Shipping Address",
  "visible": "{{ form.different_shipping === true }}"
}
```

## File Upload

Handle file uploads in your forms:

#### File Upload Configuration
Copy
```
{
  "id": "avatar",
  "type": "file",
  "label": "Profile Picture",
  "accept": "image/*",
  "maxSize": 5242880,  // 5MB
  "multiple": false,
  "uploadConfig": {
    "bucket": "user-uploads",
    "path": "avatars/{{ currentUser.id }}"
  }
}
```

#### Upload Response
Copy
```
// After upload
{
  "url": "https://cdn.../avatar.jpg",
  "key": "avatars/user-123/avatar.jpg",
  "size": 1024000,
  "type": "image/jpeg"
}

// Access in form
{{ form.avatar.url }}
```

## Error Handling

Display validation errors to users:

### Field-Level Errors
Email Address *
Please enter a valid email address

### Form-Level Errors

Unable to submit form

- • Email is required
- • Password must be at least 8 characters

## Success Messages

Show confirmation when forms are submitted successfully:

Success!

Your message has been sent successfully. We'll get back to you soon!
Copy
```
// Success configuration
{
  "onSuccess": {
    "type": "toast",
    "variant": "success",
    "message": "Form submitted successfully!",
    "duration": 5000,
    "actions": [
      { "type": "resetForm" },
      { "type": "redirect", "url": "/thank-you" }
    ]
  }
}
```

## Learn More
[### Form Components

Complete reference of all form components](https://www.algorithmshift.ai/docs/components)[### Database Integration

Save form data to your database](https://www.algorithmshift.ai/docs/database)
