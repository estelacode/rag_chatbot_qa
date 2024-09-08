# RAG Chatbot -  Question and Answer Chatbot

Chatbot implementado con LangChain y Gradio basico que responde a preguntas sobre ciencia de datos.

![Demo-Rag Chatbot QA](https://github.com/estelacode/data_science_interview_chatbot/blob/main/src/assets/chatbot_qa_demo.jpg)

### Built With

* Python
* LangChain
* Cohere
* Faiss
* Gradio

## Getting Started

### Prerequisites
To get a local copy up and running follow these simple example steps.
* python
```sh
  python --version
```
* pip
```sh
  pip --version
  python.exe -m pip install --upgrade pip
```

### Installation

0.  Deactivate enviroment
```sh
   deactivate
```

1. Clone the repo
```sh
   git clone https://github.com/estelacode/data_science_interview_chatbot.git
```
2.  Create enviroment
```sh
   python -m venv .venv
```
3.  Activate enviroment
```sh
   .venv\Scripts\activate
```

4.  Install dependencies manually
```sh
   pip install gradio
   pip install langchain
   pip install langchain_community
   pip install langchain_cohere
   pip install unstructured
   pip install networkx
   pip install openpyxl
   pip install faiss-cpu

```
4.  Install dependencies from the requirements file
```sh
   pip install -r requirements.txt
```

5. Generate requirements file
```sh
   pip freeze > requirements.txt
```
### More commands

6. show package version
```sh
   pip show pymilvus
```

7. uninstall package
```sh
   pip uninstall langchain
```
🚀 Usage
To create the vector store
```sh
   python data/ingestion.py
```

To lauch the chatbot
```sh
   pip install -e .
   app
```

# Resources
* Document loader https://python.langchain.com/v0.2/docs/integrations/document_loaders/microsoft_excel/

# Preguntas de Ejemplo
* ¿Qué es python?
* ¿Qué es el aprendizaje supervisado?
