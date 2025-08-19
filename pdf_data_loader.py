from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Step 1: Loading all the PDFs which contain repair manuals and sample data 
# generated through generative AI. PyPDFLoader from Langchain is used to load
# the PDF files. Each page of every PDF is treated as a separate document and is 
# returned through the following function.

DATA_PATH="data/"
def load_pdf_files(data):
    loader = DirectoryLoader(data,
                             glob='*.pdf',
                             loader_cls=PyPDFLoader)
    
    documents=loader.load()
    return documents

documents=load_pdf_files(data=DATA_PATH)
print("Length of PDF pages: ", len(documents))


# Step 2: Creating chunks of text from all documents to reduce the number of tokens being processed
# by our embeddings model. This will reduce the processing cost , save time and will not 
# compromise on the quality of embeddings. Chunk overlap is kept to induce some context as 
# some data of chunks will be shared with each other.

def create_chunks(extracted_data):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,
                                                 chunk_overlap=50)
    text_chunks=text_splitter.split_documents(extracted_data)
    return text_chunks

text_chunks=create_chunks(extracted_data=documents)
print("Length of Text Chunks: ", len(text_chunks))

# Step 3: Creating a function to load the Vector Embeddings model 

def get_embedding_model():
    embedding_model=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embedding_model

embedding_model=get_embedding_model()

# Step 4: Store vector embeddings in Facebook AI Similarity Search (FAISS) vector store.
# FAISS is a library for efficient similarity search and clustering of dense vectors.

DB_FAISS_PATH="vectorstore/db_faiss"
db=FAISS.from_documents(text_chunks, embedding_model)
db.save_local(DB_FAISS_PATH)