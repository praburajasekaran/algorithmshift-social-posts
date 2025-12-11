# Advanced Filtering - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/api/filtering  
**Scraped:** 2025-12-10 14:04:06

**Description:** Powerful query filtering with shorthand operators. Date ranges, pattern matching, multiple conditions, and more.

---

Advanced Filtering - AlgorithmShift Documentation | AlgorithmShiftDocumentationAPI Reference
# Advanced Filtering

Filter your data with powerful shorthand operators. Build complex queries with date ranges, pattern matching, multiple conditions, and logical operators—all via simple URL parameters.

## Shorthand Operators

Use bracket notation in query parameters to apply different comparison operators:
ShorthandSQL OperatorDescriptionExample`gte``>=`Greater than or equal`amount[gte]=1000``lte``<=`Less than or equal`amount[lte]=5000``gt``>`Greater than`price[gt]=100``lt``<`Less than`price[lt]=500``eq``=`Equals (explicit)`status[eq]=active``ne``!=`Not equals`status[ne]=cancelled``like``LIKE`Pattern match (case-sensitive)`email[like]=@example.com``ilike``ILIKE`Pattern match (case-insensitive)`name[ilike]=john``in``IN`Value in list`category[in]=A,B,C``isnull``IS NULL`Is null`deleted_at[isnull]=true``isnotnull``IS NOT NULL`Is not null`email[isnotnull]=true`
## Common Use Cases

### Date Range Filtering

Find records within a date range
Copy
```
GET /api/v1/entities/lead?
  assigned_on[gte]=2025-01-18&
  assigned_on[lte]=2025-11-18
```

SQL Output:
Copy
```
WHERE (assigned_on >= '2025-01-18' AND assigned_on <= '2025-11-18')
```

Auto-conversion: Date/timestamp fields automatically convert string values to Date objects.

### Numeric Range

Filter by numeric ranges
Copy
```
GET /api/v1/entities/opportunity?
  amount[gt]=1000&
  amount[lt]=5000
```

SQL Output:
Copy
```
WHERE (amount > 1000 AND amount < 5000)
```

### Multiple Exclusions

Exclude multiple values
Copy
```
GET /api/v1/entities/lead?
  status[ne]=cancelled&
  status[ne]=deleted
```

SQL Output:
Copy
```
WHERE (status != 'cancelled' AND status != 'deleted')
```

### Pattern Matching

Search with wildcards
Copy
```
GET /api/v1/entities/contact?
  name[ilike]=john&
  email[like]=@example.com
```

SQL Output:
Copy
```
WHERE name ILIKE '%john%' AND email LIKE '%@example.com%'
```

Difference:

- like - Case-sensitive (PostgreSQL LIKE)
- ilike - Case-insensitive (PostgreSQL ILIKE)

### IN Operator (Multiple Values)

Match any value in a list
Copy
```
GET /api/v1/entities/lead?
  category[in]=electronics,furniture,clothing
```

SQL Output:
Copy
```
WHERE category IN ('electronics', 'furniture', 'clothing')
```

Tip: Separate values with commas. No spaces needed.

### NULL Checks

Filter by null/non-null values
Copy
```
# Find records with null email
GET /api/v1/entities/contact?email[isnull]=true

# Find records with non-null phone
GET /api/v1/entities/contact?phone[isnotnull]=true
```

SQL Output:
Copy
```
WHERE email IS NULL

WHERE phone IS NOT NULL
```

## Combining Multiple Conditions

### Multiple Conditions on Same Field (AND)

Use multiple operators on the same field—they're combined with AND:
Copy
```
GET /api/v1/entities/opportunity?
  amount[gte]=1000&
  amount[lte]=10000&
  amount[ne]=5000
```

SQL Output:
Copy
```
WHERE (
  amount >= 1000 
  AND amount <= 10000 
  AND amount != 5000
)
```

### Multiple Fields (AND by default)

Different fields are combined with AND:
Copy
```
GET /api/v1/entities/lead?
  status=active&
  assigned_on[gte]=2025-01-01&
  amount[gt]=1000
```

SQL Output:
Copy
```
WHERE 
  status = 'active' 
  AND assigned_on >= '2025-01-01' 
  AND amount > 1000
```

### OR Logic (Use logic parameter)

Change global logic to OR with the logic parameter:
Copy
```
GET /api/v1/entities/lead?
  logic=or&
  status=active&
  status=pending&
  priority=high
```

SQL Output:
Copy
```
WHERE (
  status = 'active' 
  OR status = 'pending' 
  OR priority = 'high'
)
```

## Real-World Examples

### Find High-Value Active Opportunities This Quarter
Copy
```
GET /api/v1/entities/opportunity?
  status=active&
  amount[gte]=10000&
  close_date[gte]=2025-01-01&
  close_date[lte]=2025-03-31&
  stage[ne]=lost
```

### Find Unassigned Leads from Specific Sources
Copy
```
GET /api/v1/entities/lead?
  assigned_to[isnull]=true&
  source[in]=website,referral,email_campaign&
  created_at[gte]=2025-11-01
```

### Find Contacts with Gmail Addresses Named John
Copy
```
GET /api/v1/entities/contact?
  name[ilike]=john&
  email[like]=@gmail.com&
  email[isnotnull]=true
```

### Find Cancelled or Refunded Orders Over $500
Copy
```
GET /api/v1/entities/order?
  logic=or&
  status[in]=cancelled,refunded&
  total[gt]=500&
  created_at[gte]=2025-01-01
```

## Simple Equality (No Brackets)

Fields without brackets default to equality operator:
Copy
```
# These are equivalent:
GET /api/v1/entities/lead?status=active
GET /api/v1/entities/lead?status[eq]=active

# Both produce:
WHERE status = 'active'
```

## Performance Tips

### Do

- • Use indexed columns in filters (status, created_at, etc.)
- • Combine with pagination (limit, offset)
- • Use specific date ranges instead of open-ended
- • Use in operator for multiple values (more efficient than multiple OR)

### Avoid

- • Leading wildcards in LIKE (%text) - can't use indexes
- • Filtering on non-indexed columns with large datasets
- • Too many OR conditions (consider restructuring query)
- • Open-ended date queries without upper bound

## Learn More
[### REST APIs

Complete REST API reference](https://www.algorithmshift.ai/docs/database/rest)[### API Reference

Full API documentation](https://www.algorithmshift.ai/docs/api)[### Data Authorization

How security filters work with queries](https://www.algorithmshift.ai/docs/data-authorization)[### Database Setup

Schema design and optimization](https://www.algorithmshift.ai/docs/database)
