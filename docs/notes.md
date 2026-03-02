# LangChain Udemy Course Notes

## 1. Hello World with Ollama (`src/hello_world.py`)

Basic example: send messages directly to an LLM and get a response.

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(model="gemma3:27b", temperature=0)

messages = [
    ("system", "You are a helpful assistant that translates English to French."),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)
```

**Key takeaways:**
- `ChatOllama` connects to a local Ollama instance
- `temperature` controls randomness (0 = deterministic, higher = more creative)
- Messages use tuples with role and content: `("system", "...")`, `("human", "...")`
- `llm.invoke(messages)` sends the messages and returns an AI message object
- Use `.content` to get the actual text from the response

---

## 2. Prompt Templates & LCEL Chains (`src/hello_world_advanced.py`)

Using `PromptTemplate` to create reusable prompts with variables, and LCEL to chain components.

```python
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(model="gemma3:27b", temperature=0.1)

chat_prompt = PromptTemplate.from_template(
    "Say hello to the user with its name.\nUser's name: {name}\nAssistant"
)

chain = chat_prompt | llm

response = chain.invoke({"name": "Roberto"})
print(response.content)
```

**Key takeaways:**
- `PromptTemplate.from_template()` creates a template with `{placeholders}` for variables
- Do NOT use f-strings (`f"...{var}"`) in templates — use plain `{var}` so LangChain fills them at runtime
- `from_template()` infers input variables automatically, no need to pass `input_variables`

### LCEL — LangChain Expression Language

The `|` (pipe) operator connects components into a chain (like Unix pipes):

```
chain = prompt | llm
```

This means: fill the template -> send to LLM -> return response.

You can keep adding steps:

```
chain = prompt | llm | output_parser
```

**Why use LCEL?**
- Readable, declarative syntax
- Built-in support for async, streaming, and batch operations
- Each component is a `Runnable`, and any `Runnable` can be piped

**Docs:**
- [LCEL Concepts](https://python.langchain.com/docs/concepts/lcel/)
- [Runnable API Reference](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html)
