# Agent Builder - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/ai/builder  
**Scraped:** 2025-12-10 14:03:34

**Description:** Build AI agents with the visual node-based editor. Configure LLM nodes, tools, and conversation flow.

---

Agent Builder - AlgorithmShift Documentation | AlgorithmShiftDocumentationAI Agents
# Agent Builder

Design AI agents with a visual node-based interface. Connect triggers, LLM nodes, tools, and actions.

### Triggers

Webhook, Email, Chat

### AI Nodes

LLM, Memory, RAG

### Tools

Database, API, Files

### Actions

Email, Webhook, Response

## Agent Flow Example
Copy
```
// Customer support agent flow
{
  "nodes": [
    {
      "id": "trigger",
      "type": "webhook",
      "config": { "channel": "web_chat" }
    },
    {
      "id": "memory",
      "type": "memory",
      "config": { "type": "conversation", "maxTokens": 2000 }
    },
    {
      "id": "rag",
      "type": "rag",
      "config": {
        "collection": "support-docs",
        "maxResults": 3
      }
    },
    {
      "id": "llm",
      "type": "llm",
      "config": {
        "model": "gpt-4",
        "temperature": 0.7,
        "systemPrompt": "You are a helpful support agent..."
      }
    },
    {
      "id": "response",
      "type": "respond",
      "config": {
        "channel": "{{ trigger.channel }}"
      }
    }
  ],
  "connections": [
    { "from": "trigger", "to": "memory" },
    { "from": "memory", "to": "rag" },
    { "from": "rag", "to": "llm" },
    { "from": "llm", "to": "response" }
  ]
}
```
