import streamlit as st

# AIMessage, HumanMessage, SystemMessage = objetos de mensaje tipados de LangChain
# Cada uno envuelve un rol (system/human/ai) + cadena de contenido
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import (
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

# ChatOllama se conecta a un servidor Ollama corriendo localmente
from langchain_ollama import ChatOllama

# Configuracion de pagina — debe ser el primer comando de Streamlit
st.set_page_config(page_title="Basic Chatbot", page_icon="🤖")
st.title("🤖 Basic Chatbot with Langchain")
st.markdown("Chat with a local LLM powered by LangChain and Ollama.")

chat_model = ChatOllama(model="gemma3:27b", temperature=0.3)

# st.session_state persiste datos entre reruns de Streamlit (cada interaccion re-ejecuta el script)
# "not in" verifica si la clave "messages" NO existe aun en session_state
if "messages" not in st.session_state:
    # session_state funciona como un diccionario — aqui creamos la clave "messages" con una lista vacia
    # esta lista almacenara objetos HumanMessage y AIMessage conforme avance la conversacion
    st.session_state.messages = []

# Renderizar historial del chat — omitir SystemMessage ya que es solo para el LLM, no para el usuario
# for recorre cada mensaje almacenado en la lista
for msg in st.session_state.messages:
    # isinstance() verifica si un objeto es de un tipo especifico
    if isinstance(msg, SystemMessage):
        # continue salta a la siguiente iteracion del for, sin ejecutar el codigo de abajo
        continue

    # Operador ternario: variable = valor_si_true if condicion else valor_si_false
    role = "assistant" if isinstance(msg, AIMessage) else "user"

    # "with" abre un bloque de contexto — aqui crea una burbuja de chat con el avatar correspondiente
    # todo lo que este dentro del with se renderiza dentro de esa burbuja
    with st.chat_message(role):
        # .content accede al atributo de texto del objeto mensaje de LangChain
        st.markdown(msg.content)
