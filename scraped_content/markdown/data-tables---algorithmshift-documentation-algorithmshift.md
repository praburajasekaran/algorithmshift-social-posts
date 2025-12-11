# Data Tables - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/tables  
**Scraped:** 2025-12-10 14:03:20

**Description:** Display and manage data with powerful table components. Sorting, filtering, pagination, and inline editing.

---

Data Tables - AlgorithmShift Documentation | AlgorithmShiftDocumentationApp Builder
# Data Tables

Display and manage tabular data with powerful table components. Built-in sorting, filtering, pagination, and actions.

### Rich Data Display

Customizable columns

### Sorting

Multi-column sorting

### Filtering

Advanced filter UI

### Export

CSV, Excel, JSON

## Basic Table Configuration
Copy
```
<Table
  dataSource="tasks"
  columns={[
    {
      key: 'id',
      label: 'ID',
      type: 'text',
      width: 80,
      sortable: false
    },
    {
      key: 'title',
      label: 'Task Title',
      type: 'text',
      sortable: true,
      searchable: true
    },
    {
      key: 'status',
      label: 'Status',
      type: 'badge',
      sortable: true,
      filterable: true,
      filterOptions: ['pending', 'active', 'completed'],
      badgeColors: {
        pending: 'yellow',
        active: 'blue',
        completed: 'green'
      }
    },
    {
      key: 'priority',
      label: 'Priority',
      type: 'select',
      sortable: true,
      filterable: true,
      options: [
        { value: 'low', label: 'Low' },
        { value: 'medium', label: 'Medium' },
        { value: 'high', label: 'High' }
      ]
    },
    {
      key: 'assigned_to',
      label: 'Assigned To',
      type: 'relation',
      relatedTable: 'users',
      displayField: 'name',
      expandable: true
    },
    {
      key: 'created_at',
      label: 'Created',
      type: 'datetime',
      format: 'MMM DD, YYYY',
      sortable: true
    }
  ]}
  pagination={true}
  pageSize={20}
  actions={['view', 'edit', 'delete']}
  onRowClick={(row) => {
    // Navigate to detail page
    navigateTo(`/tasks/${row.id}`);
  }}
/>
```

## Column Types

### text

Plain text display

Example: "Hello World"

### number

Formatted numbers

Example: 1,234.56

### currency

Currency formatting

Example: $1,234.56

### date

Date formatting

Example: Jan 15, 2024

### datetime

Date and time

Example: Jan 15, 2024 10:30 AM

### boolean

True/false checkbox

Example: ✓ or ✗

### badge

Colored status badge

Example: 🟢 Active

### image

Thumbnail preview

Example: [img]

### link

Clickable link

Example: 🔗 View

### relation

Foreign key display

Example: John Doe

### array

List of values

Example: Tag1, Tag2

### custom

Custom renderer

Example: Custom JSX

## Row Actions
Copy
```
// Table with row actions
{
  "actions": [
    {
      "type": "view",
      "label": "View Details",
      "icon": "eye",
      "onClick": "navigateTo('/tasks/{{ row.id }}')"
    },
    {
      "type": "edit",
      "label": "Edit",
      "icon": "pencil",
      "onClick": "openEditModal({{ row }})"
    },
    {
      "type": "delete",
      "label": "Delete",
      "icon": "trash",
      "confirm": true,
      "confirmMessage": "Delete this task?",
      "onClick": "deleteRecord('tasks', {{ row.id }})"
    },
    {
      "type": "custom",
      "label": "Assign",
      "icon": "user-plus",
      "visible": "{{ currentUser.role === 'admin' }}",
      "onClick": "openAssignModal({{ row }})"
    }
  ]
}
```

## Advanced Features

### Inline Editing
Copy
```
{
  "editable": true,
  "editableColumns": ["title", "status", "priority"],
  "onCellEdit": {
    "type": "update_record",
    "table": "tasks",
    "autoSave": true
  }
}
```

### Bulk Actions
Copy
```
{
  "selectable": true,
  "bulkActions": [
    {
      "label": "Delete Selected",
      "action": "deleteRecords"
    },
    {
      "label": "Update Status",
      "action": "bulkUpdate",
      "field": "status"
    },
    {
      "label": "Export Selected",
      "action": "exportToCsv"
    }
  ]
}
```

### Server-Side Processing
Copy
```
{
  "serverSide": true,
  "apiEndpoint": "/api/v1/tables/tasks",
  "totalRecords": 10000,
  // Sorting, filtering, pagination
  // handled by server
}
```

### Export Data
Copy
```
{
  "exportFormats": ["csv", "excel", "json"],
  "exportAll": true,
  "exportFiltered": true
}
```

## Learn More
[### Database Integration

Connect tables to your database](https://www.algorithmshift.ai/docs/database)[### All Components

Explore other data display components](https://www.algorithmshift.ai/docs/components)
