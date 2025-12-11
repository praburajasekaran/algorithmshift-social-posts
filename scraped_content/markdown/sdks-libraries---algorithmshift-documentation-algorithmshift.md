# SDKs & Libraries - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/sdks  
**Scraped:** 2025-12-10 14:03:06

**Description:** Client libraries and SDKs for popular programming languages.

---

SDKs & Libraries - AlgorithmShift Documentation | AlgorithmShiftDocumentationAPI Reference
# SDKs & Client Libraries

Official client libraries for popular programming languages.

### JavaScript / TypeScript
Copy
```
npm install @algorithmshift/js

import { AlgorithmShift } from '@algorithmshift/js';

const as = new AlgorithmShift({
  apiKey: process.env.AS_API_KEY
});

const tasks = await as.tables.tasks.list();
```

### Python
Copy
```
pip install algorithmshift

from algorithmshift import Client

client = Client(api_key=os.getenv('AS_API_KEY'))

tasks = client.tables.tasks.list()
```

### React Hooks
Copy
```
npm install @algorithmshift/react

import { useTable } from '@algorithmshift/react';

function TaskList() {
  const { data, loading } = useTable('tasks');
  
  return <div>{/* Render tasks */}</div>;
}
```
