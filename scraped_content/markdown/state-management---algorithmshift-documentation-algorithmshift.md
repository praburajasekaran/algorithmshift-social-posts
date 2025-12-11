# State Management - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/state  
**Scraped:** 2025-12-10 14:03:22

**Description:** Manage application state, global variables, and data flow between components.

---

State Management - AlgorithmShift Documentation | AlgorithmShiftDocumentationApp Builder
# State Management

Manage application state, share data between components, and create reactive user interfaces.

### Component State

Local to single component

### Global State

Shared across all components

### URL State

Stored in URL parameters

## Using State Variables
Copy
```
// Define state variables
{
  "appState": {
    "currentUser": null,
    "isAuthenticated": false,
    "selectedTask": null,
    "filterStatus": "all",
    "darkMode": false
  }
}

// Access state in components
{{ appState.currentUser.name }}
{{ appState.isAuthenticated }}

// Update state
{
  "onClick": {
    "type": "setState",
    "key": "selectedTask",
    "value": "{{ row }}"
  }
}

// Conditional rendering based on state
{
  "visible": "{{ appState.isAuthenticated === true }}"
}
```

## Learn More
[### Components

Use state with components](https://www.algorithmshift.ai/docs/components)[### Data Binding

Connect state to database](https://www.algorithmshift.ai/docs/database)
