# RAG & Knowledge Base - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/ai/rag  
**Scraped:** 2025-12-10 14:03:37

**Description:** Integrate knowledge bases with AI agents using Retrieval Augmented Generation (RAG).

---

RAG & Knowledge Base - AlgorithmShift Documentation | AlgorithmShiftDocumentationAI Agents
# RAG & Knowledge Base

Enhance AI agents with Retrieval Augmented Generation. Connect to knowledge bases for accurate, context-aware responses.
1
### User Query

User asks: "How do I reset my password?"
2
### Vector Search

System searches knowledge base for relevant documents:
Copy
```
// Top 3 relevant documents found
[
  { "content": "To reset password, go to Settings...", "score": 0.92 },
  { "content": "Forgot password link...", "score": 0.85 },
  { "content": "Password requirements...", "score": 0.78 }
]
```
3
### LLM Response

Agent generates response using retrieved context + LLM

## RAG Configuration
Copy
```
{
  "type": "rag",
  "knowledgeBase": "support-docs",
  "embeddingModel": "text-embedding-ada-002",
  "searchConfig": {
    "maxResults": 5,
    "minScore": 0.7,
    "includeMetadata": true,
    "rerank": true
  },
  "llmConfig": {
    "model": "gpt-4",
    "temperature": 0.3,
    "systemPrompt": "Use the provided context to answer questions accurately..."
  }
}
```
