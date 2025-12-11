# Organization-Wide Defaults (OWD) - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/data-authorization/owd  
**Scraped:** 2025-12-10 14:04:09

**Description:** Configure table-level default access modes: Public Read/Write, Public Read Only, Private, and Controlled by Parent.

---

Organization-Wide Defaults (OWD) - AlgorithmShift Documentation | AlgorithmShiftDocumentationData Authorization & Security
# Organization-Wide Defaults (OWD)

Set the baseline access level for each table. OWD is the first layer of security evaluation after workspace admin bypass, defining what users can see by default.

## The Four OWD Modes

Each table in your database has one of four default access levels:

### Public Read/Write

Most open access

All users can see AND edit all records in the table.
**Read:** Everyone sees all records**Write:** Everyone can edit all records**Delete:** Everyone can delete all recordsCopy
```
SELECT * FROM countries
-- Returns ALL records (no filtering)
```

### Public Read Only

View all, edit only yours

All users can see all records, but can only edit/delete their own (or those shared with them).
**Read:** Everyone sees all records**Write:** Only your records (layers 2-4 apply)**Delete:** Only your records (layers 2-4 apply)Copy
```
-- READ: All records visible
SELECT * FROM products
-- Returns ALL records

-- WRITE: Only filtered records
UPDATE products SET price = 100
WHERE (owner_id = current_user OR ...)
```

### Private

Most restrictive

Users can only see and edit records they own or that are shared with them.
**Read:** Only your records (layers 2-4 apply)**Write:** Only your records (layers 2-4 apply)**Delete:** Only your records (layers 2-4 apply)Copy
```
SELECT * FROM orders
WHERE (
  owner_id = current_user
  OR primary_group_id IN (user_groups)
  OR EXISTS (explicit shares)
)
-- Only returns YOUR records
```

### Controlled by Parent

Inherit from parent table

Access is determined by the parent record. If you can see the parent, you can see the child.
**Parent Access:** Requires parent_table_name field**Automatic:** Child records inherit parent access**Common Use:** Order Line Items → OrdersCopy
```
-- If parent_table_name = 'orders'
SELECT * FROM order_line_items
WHERE order_id IN (
  SELECT id FROM orders
  WHERE (... parent access rules ...)
)
-- Inherits Orders access
```

## OWD Configuration

Set OWD for each table in the table settings:

### Table Settings Location
Copy
```
Admin Interface Path:
/{workspaceId}/access-control/data-management/tables

1. Select your table from the list
2. Click "Settings" or "Edit"
3. Find "Default Access" field
4. Choose one of four modes:
   - public_read_write
   - public_read_only
   - private
   - controlled_by_parent

5. Save changes
```

## Database Schema

OWD settings are stored in the sys_table_settings table:
Copy
```
CREATE TABLE sys_table_settings (
  id UUID PRIMARY KEY,
  workspace_id UUID NOT NULL,
  table_name VARCHAR NOT NULL,
  
  -- OWD Configuration
  default_access VARCHAR DEFAULT 'private',
    -- 'public_read_write'
    -- 'public_read_only'
    -- 'private'
    -- 'controlled_by_parent'
  
  -- Parent Table (for controlled_by_parent mode)
  parent_table_name VARCHAR,
  parent_id_column VARCHAR DEFAULT 'parent_id',
  
  -- RLS Configuration
  rls_enabled BOOLEAN DEFAULT true,
  
  -- Audit Configuration
  track_created_by BOOLEAN DEFAULT true,
  track_updated_by BOOLEAN DEFAULT true,
  
  UNIQUE(workspace_id, table_name)
);
```

## Choosing the Right OWD Mode

Public Read/Write

Use For:

- • Reference data (countries, states, categories)
- • Shared configuration tables
- • Lookup tables
- • Public announcements

⚠️ Be careful: Everyone can modify data!

Public Read Only

Use For:

- • Product catalogs (view all, edit yours)
- • Knowledge bases (read all, create yours)
- • Company directory (see everyone, edit yourself)
- • Shared resources with ownership

✓ Good balance: Visibility + ownership

Private

Use For:

- • Customer data (accounts, contacts)
- • Financial records (invoices, payments)
- • Sensitive information (medical records)
- • Personal user data

✓ Most secure: Explicit sharing required

Controlled by Parent

Use For:

- • Child records (order → line items)
- • Nested data (account → contacts → notes)
- • Related records that follow parent
- • Hierarchical data structures

→ Simplifies complex hierarchies

## Real-World Examples

### CRM System
TableOWD ModeReason`accounts`PrivateSensitive customer data`contacts`PrivatePersonal information`opportunities`PrivateSales data is confidential`products`Public Read OnlyEveryone views, product managers edit`price_books`Public Read OnlyEveryone sees prices, admins edit`opportunity_line_items`Controlled by ParentFollow opportunity access`countries`Public Read/WriteReference data
## How OWD Interacts with Other Layers

OWD is evaluated early in the security chain, but other layers can grant additional access:
Copy
```
Example: Table with OWD = "private"

1. OWD says: "You can only see your own records"
2. But other layers can EXPAND access:
   - Ownership (Layer 2): + Records you own
   - Groups (Layer 3): + Records from your groups
   - Shares (Layer 4): + Records explicitly shared with you
   - RLS Policies (Layer 5): + Records matching custom rules

Result: Private OWD + Group sharing = You see your records AND your team's records

Important: OWD sets the BASELINE. Other layers can only ADD more access, 
never remove it (except Layer 5 RLS policies, which use AND logic).
```

## Learn More
[### Table Settings

Configure OWD and other table settings](https://www.algorithmshift.ai/docs/data-authorization/table-settings)[### Ownership & Groups

How ownership expands on OWD](https://www.algorithmshift.ai/docs/data-authorization/ownership)[### How Access Works

Complete access evaluation flow](https://www.algorithmshift.ai/docs/data-authorization/access-flow)
