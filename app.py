#Langchain components to import
from langchain_community.vectorstores import Cassandra
from langchain_community.indexes import VectorStoreIndexWrapper
from langchain_community.llms import OpenAI
from langchain_openai import OpenAIEmbeddings

# vector_store = InMemoryVectorStore(embedding=SomeEmbeddingModel())

# Hugging Face support for dataset retrieval
from datasets import load_dataset

#Cassio helps integratrion with AstraDB in Langchain and also intialise the DB
import cassio

from PyPDF2 import PdfFileReader

ASTRA_DB_APPLICATION_TOKEN = "AstraCS:ImecPAlWRFypwfTxcXbvZmGt:7b421b94810e9cafde579adb131d674a5873a4ce143ecfca74095b4c58c7fb30"
ASTRA_DB_ID = "01c8f635-8a18-456f-816e-1bb428a9498a"

OPENAI_API_KEY = "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"

pdfContent = PdfFileReader('harry_potter_7.pdf')

from typing_extensions import Concatenate

#read the pdf text
raw_text=''
for i, page in enumerate(pdfContent.pages):
    content = page.extractText()
    if content:
        raw_text += content

cassio.init(token=ASTRA_DB_APPLICATION_TOKEN, database_id=ASTRA_DB_ID)

llm = OpenAI(openai_api_key = OPENAI_API_KEY)
embedding = OpenAIEmbeddings(openai_api_key = OPENAI_API_KEY)

astra_vector_store = Cassandra(
    embedding = embedding,
    table_name = "embedded_text",
    session = None,
    keyspace = None
)

from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(separators = " ", chunk_size = 800, chunk_overlap = 200)

split_text = text_splitter.split_text(raw_text)

astra_vector_store.add_texts(split_text)

astra_vector_index = VectorStoreIndexWrapper(vectorstore = astra_vector_store)

first_question = True

while True:
    if first_question:
        query = input(f'Please type in your first question (or type quit to exit): ').strip()
    else:
        query = input(f'Please type in your next question').strip()
    
    if query == "quit".lower():
        break

    if query == "":
        continue

    first_question = False

    print(f'\n QUESTION: "{query}"')
    answer = astra_vector_index.query(query, llm = llm).strip
    print(f'\n ANSWER: "{answer}"')
    

