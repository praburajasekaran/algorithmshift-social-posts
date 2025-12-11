# LLM Models - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/ai/models  
**Scraped:** 2025-12-10 14:03:36

**Description:** Configure AI models from OpenAI, Anthropic, and AWS Bedrock for your agents.

---

LLM Models - AlgorithmShift Documentation | AlgorithmShiftDocumentationAI Agents
# LLM Models

Choose from leading AI models for your agents. OpenAI GPT-4, Anthropic Claude, and AWS Bedrock.

### OpenAI

- GPT-4 Turbo (128K context)
- GPT-4 (8K context)
- GPT-3.5 Turbo (16K)
- Function calling

### Anthropic

- Claude 2 (100K context)
- Claude Instant
- Constitutional AI
- Long context

### AWS Bedrock

- Claude (Anthropic)
- Titan (Amazon)
- Llama 2 (Meta)
- Jurassic (AI21)

## Model Configuration
Copy
```
{
  "model": "gpt-4",
  "temperature": 0.7,        // 0-1 (creativity)
  "maxTokens": 2000,         // Max response length
  "topP": 1.0,               // Nucleus sampling
  "frequencyPenalty": 0,     // Reduce repetition
  "presencePenalty": 0,      // Topic diversity
  "systemPrompt": "You are a helpful assistant..."
}
```
