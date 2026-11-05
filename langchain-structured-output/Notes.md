 Large Language Models (LLMs) natively speak and output **unstructured text** (strings). However, when we want to build software applications, backend systems, or databases that talk to an LLM, a free-flowing paragraph won't work—we need **structured data** (like JSON objects, typed classes, or dictionaries).

To solve this, LangChain splits structured outputs into two core approaches, which match how the repository is structured:

---

### The Two Ways to Get Structured Output

1. **Models with Native Structured Output Support (e.g., OpenAI with `with_structured_output`)**
* **How it works:** Modern models (like GPT-4o or GPT-4o-mini) have built-in API parameters (often powered by JSON mode or tool/function calling under the hood) that guarantee the model will output a response matching a schema you provide (usually defined using **Pydantic**).
* **Why it's great:** It is clean, reliable, handled natively by the model provider, and parses straight into a typed Python object.


2. **Models without Native Structured Output Support (Using Output Parsers)**
* **How it works:** For older models or open-source models that don't natively enforce a strict JSON schema via API parameters, we rely on **LangChain Output Parsers** (e.g., `PydanticOutputParser`, `JsonOutputParser`).
* **Why it's used:** We instruct the LLM via prompt engineering (passing the formatting instructions and schema inside the prompt) and then parse its textual response back into structured code. If it fails or hallucinates extra text, we catch it or use retry mechanisms.

