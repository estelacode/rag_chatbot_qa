PLACE_HOLDER = "¡Hola! ¿En qué puedo ayudarte?"
BOT_ICON = "src/assets/chatbot.png"
USER_ICON = "src/assets/user.png"
UI_PORT =8051

RAG_PROMPT="""You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. Use only the context provided to response. If you don't know the answer,just say that you don't know. Use three sentences maximum and keep the answer concise.

Question: {query} 

Context: {context} 

Answer:"""