## 1. LangChain Model Component

### What are Models?

**The Model component in LangChain is a crucial part of the framework, designed to facilitate interactions with various language models and embedding models.**

It **abstracts the complexity** of working directly with different LLMs, chat models, and embedding models, providing a **uniform interface** to communicate with them.

This makes it easier to build applications that rely on:

- AI-generated text
- Text embeddings for similarity search
- Retrieval-Augmented Generation (**RAG**)

### Models in LangChain

```text
                    Models
                   /      \
                  /        \
        Language Models   Embedding Models
             /     \
            /       \
          LLMs    Chat Models
```

So, in LangChain:

**Models**
→ **Language Models**
→ **LLMs / Chat Models**

and separately:

**Models**
→ **Embedding Models**

---

### Important idea

LangChain provides a **common/uniform interface** so that you can work with different model providers without having to completely change your application code.

For example, your application can interact with different language models through LangChain rather than writing completely different code for each provider.


## 1. Language Models

### Language Models
**Language Models are AI systems designed to process, generate, and understand natural language text.**

**Basic idea:**

`Text → Language Model → Text`

Language Models can be broadly divided into:

- **LLMs (Large Language Models)**
- **Chat Models**

### LLMs
LLMs are **general-purpose models** that are used for raw text generation.

- They take a **string (plain text)** as input.
- They return a **string (plain text)** as output.
- These are traditionally older models and are **not used much now**.

**Example:**

`"Tell me a story" → LLM → "Once upon a time..."`

### Chat Models
Chat Models are language models specialized for **conversational tasks**.

- They take a **sequence of messages** as input.
- They return **chat messages** as output.
- Unlike LLMs, they work with structured messages such as:
  - system
  - user
  - assistant
- These are traditionally newer models and are used more compared to traditional LLMs.