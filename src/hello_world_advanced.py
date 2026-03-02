from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

# Create the LLM instance using Ollama with the gemma3 model
llm = ChatOllama(
    model="gemma3:27b",
    temperature=0.1,
)

# Create a prompt template with {name} as a placeholder
chat_prompt = PromptTemplate.from_template(
    "Say hello to the user with its name.\nUser's name: {name}\nAssistant"
)

# The "|" (pipe) operator connects the prompt and the LLM into a chain.
# It works like a pipeline: prompt fills the template -> sends it to the LLM -> returns the response.
# This is LangChain's LCEL (LangChain Expression Language) syntax.
chain = chat_prompt | llm

# Run the chain passing the value for {name} and print the LLM response
response = chain.invoke({"name": "Roberto"})
print(response.content)
