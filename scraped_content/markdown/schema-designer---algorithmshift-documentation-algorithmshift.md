# Schema Designer - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/database/schema  
**Scraped:** 2025-12-10 14:03:40

**Description:** Design your database schema visually. Create tables, define relationships, and manage constraints.

---

Schema Designer - AlgorithmShift Documentation | AlgorithmShiftDocumentationDatabase & APIs
# Visual Schema Designer

Design your database schema with an intuitive visual interface. Define tables, columns, relationships, and constraints without writing SQL.
1
### Create Table

#### Table Properties

Table Name

customers (lowercase, plural)

Description

Customer information and contacts

RLS Enabled

Yes (recommended for multi-user apps)

#### Generated SQL
Copy
```
CREATE TABLE customers (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Enable RLS
ALTER TABLE customers ENABLE ROW LEVEL SECURITY;
```
2
### Add Columns
ColumnTypeConstraints`id`UUIDPRIMARY KEY, DEFAULT uuid_generate_v4()`name`VARCHAR(255)NOT NULL`email`VARCHAR(255)UNIQUE, NOT NULL`company`VARCHAR(255)-`status`VARCHAR(50)DEFAULT 'active'`created_at`TIMESTAMPDEFAULT NOW()3
### Define Relationships
Copy
```
// Add foreign key to orders table
{
  "column": "customer_id",
  "type": "UUID",
  "foreignKey": {
    "table": "customers",
    "column": "id",
    "onDelete": "CASCADE",
    "onUpdate": "CASCADE"
  }
}

-- Generated SQL
ALTER TABLE orders
ADD CONSTRAINT fk_orders_customer
FOREIGN KEY (customer_id)
REFERENCES customers(id)
ON DELETE CASCADE;
```

## Learn More
[### Database Overview

Learn about database features](https://www.algorithmshift.ai/docs/database)[### REST APIs

Auto-generated APIs for your tables](https://www.algorithmshift.ai/docs/database/rest)
