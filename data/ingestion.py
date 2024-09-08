# Autor: Estela Madariaga

import os
from langchain_community.document_loaders import UnstructuredExcelLoader
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain_cohere.llms import Cohere
from langchain_cohere.embeddings import CohereEmbeddings
from dotenv import load_dotenv,find_dotenv
from uuid import uuid4
import logging


# Configurar el logging
logging.basicConfig(
    level=logging.DEBUG,  # Nivel de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Formato del log
    datefmt='%Y-%m-%d %H:%M:%S',  # Formato de la fecha
    filename="app.log",  # Archivo de log.
    filemode='a'  # Modo de apertura del archivo (a: append, w: write)
)


# Obtener un logger
logger = logging.getLogger(__name__)

# Cargar variables de entorno desde el archivo .env
load_dotenv(".env")


def load_excels_files():
    """
    Loads Excel files from the current directory and its subdirectories.

    Returns:
    list: A list of documents loaded from the Excel files.
    """
    loader = DirectoryLoader('.'  , glob="**/*.xlsx", loader_cls=UnstructuredExcelLoader, show_progress=True)
    docs = loader.load_and_split()
    logger.info(f"Loaded {len(docs)} documents")
    return docs


def ingestion():
    """
    Ingests data into a vector database.

    Creates a vector database using Cohere embeddings and Chroma, loads data from a directory,
    generates a unique ID for each document, and adds the documents to the database.
    """
    # Cargar los datos desde un directorio
    docs = load_excels_files()

    # Crear base de datos vectorial 
    embeddings = CohereEmbeddings( model="embed-multilingual-v3.0",cohere_api_key=os.getenv("COHERE_API_KEY"))

    vectorstore = FAISS.from_documents(docs, embeddings)
    # Guardar la base de datos vectorial en local
    vectorstore.save_local("./data/faiss_index")

   

if __name__ == "__main__":
    ingestion()
    