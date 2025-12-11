# Components - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/components  
**Scraped:** 2025-12-10 14:04:04

**Description:** Complete reference of all UI components available in the AlgorithmShift visual builder.

---

Components - AlgorithmShift Documentation | AlgorithmShiftDocumentationApp Builder
# Component Library

50+ pre-built components for building web and mobile applications. Drag, drop, and configure.

### Layout

12 components

### Basic

8 components

### Form

15 components

### Data Display

7 components

### Navigation

6 components

### Charts

8 components

## Layout Components

Structure your application with flexible layout components.

### Container
Layout
Responsive container with max-width constraints

#### Properties
maxWidth`sm | md | lg | xl | 2xl | full`padding`0-20`centered`boolean`
#### Usage Example
Copy
```
<Container maxWidth="lg" padding={4}>
  <Typography variant="h1">
    Welcome
  </Typography>
  {/* Other components */}
</Container>
```

### Grid
Layout
Responsive grid system with 12 columns

#### Properties
columns`1-12`gap`0-20`responsive`sm, md, lg breakpoints`
#### Usage Example
Copy
```
<Grid columns={3} gap={4}>
  <Card>Item 1</Card>
  <Card>Item 2</Card>
  <Card>Item 3</Card>
</Grid>

// Responsive
<Grid 
  columns={{ sm: 1, md: 2, lg: 3 }}
  gap={4}
/>
```

### Flex
Layout
Flexbox container for alignment and spacing

#### Properties
direction`row | column`justify`start | center | between | end`align`start | center | stretch | end`
#### Usage Example
Copy
```
<Flex 
  direction="row" 
  justify="between" 
  align="center"
>
  <Typography>Left</Typography>
  <Button>Right</Button>
</Flex>
```

## Form Components

Build interactive forms with validation and data binding.

### Text Input
Form
Single-line text input with validation

#### Properties
type`text | email | password | number`placeholder`string`required`boolean`validation`regex | min | max`
#### Usage Example
Copy
```
<TextInput
  label="Email Address"
  type="email"
  placeholder="you@example.com"
  required={true}
  validation={{
    pattern: /^[^@]+@[^@]+$/,
    message: "Invalid email"
  }}
  onChange={(value) => {
    // Handle change
  }}
/>
```

### Select
Form
Dropdown select with search and multi-select

#### Properties
options`array`multiple`boolean`searchable`boolean`dataSource`table | api | static`
#### Usage Example
Copy
```
<Select
  label="Status"
  options={[
    { value: 'pending', label: 'Pending' },
    { value: 'active', label: 'Active' },
    { value: 'completed', label: 'Completed' }
  ]}
  multiple={false}
  searchable={true}
  onChange={(value) => {
    // Handle selection
  }}
/>

// With data binding
<Select
  dataSource="tasks"
  valueField="id"
  labelField="title"
/>
```

## Data Display Components

Display and interact with your data efficiently.

### Table
Data Display
Feature-rich data table with sorting, filtering, and pagination

#### Properties
dataSource`table name or API`columns`array of column configs`pagination`boolean`actions`view | edit | delete`
#### Usage Example
Copy
```
<Table
  dataSource="tasks"
  columns={[
    { key: 'title', label: 'Task', sortable: true },
    { key: 'status', label: 'Status', filterable: true },
    { key: 'created_at', label: 'Created', type: 'date' }
  ]}
  pagination={true}
  pageSize={10}
  actions={['view', 'edit', 'delete']}
  onRowClick={(row) => {
    // Navigate to detail page
  }}
/>
```

## Chart Components

Visualize data with interactive charts.

### Line Chart
Copy
```
<LineChart
  dataSource="sales"
  xAxis="date"
  yAxis="revenue"
  height={300}
/>
```

### Bar Chart
Copy
```
<BarChart
  dataSource="tasks"
  groupBy="status"
  aggregate="count"
  height={300}
/>
```

### Pie Chart
Copy
```
<PieChart
  dataSource="users"
  groupBy="role"
  valueField="count"
  height={300}
/>
```

### Area Chart
Copy
```
<AreaChart
  dataSource="analytics"
  xAxis="timestamp"
  yAxis={['users', 'sessions']}
  height={300}
/>
```

## Component Configuration

All components share common configuration patterns:
Copy
```
// Common properties across all components
{
  // Identification
  "id": "component-123",
  "name": "MyComponent",
  
  // Styling
  "styles": {
    "width": "100%",
    "padding": "16px",
    "backgroundColor": "#ffffff",
    "borderRadius": "8px"
  },
  
  // Responsive styles
  "responsiveStyles": {
    "mobile": { "padding": "8px" },
    "tablet": { "padding": "12px" },
    "desktop": { "padding": "16px" }
  },
  
  // Visibility
  "visible": true,
  "conditionalVisibility": "{{ user.role === 'admin' }}",
  
  // Data binding
  "dataSource": "tasks",
  "filters": { "status": "active" },
  
  // Events
  "events": {
    "onClick": "navigateTo('/detail')",
    "onLoad": "fetchData",
    "onChange": "updateState"
  },
  
  // Permissions
  "requiredPermissions": ["tasks.read"]
}
```

## Next Steps

Explore more about building with components:
[### Styling & Themes

Learn how to style and theme your components](https://www.algorithmshift.ai/docs/styling)[### Forms & Validation

Build forms with validation and submission](https://www.algorithmshift.ai/docs/forms)[### State Management

Manage component state and data flow](https://www.algorithmshift.ai/docs/state)[### Data Binding

Connect components to your database](https://www.algorithmshift.ai/docs/database)
