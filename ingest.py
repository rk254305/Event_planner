from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

# Load documents
loader = TextLoader("data/events_docs.txt")
docs = loader.load()

# Split text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(docs)

# Embeddings
embeddings = OllamaEmbeddings(model="llama2")

# Vector store
vectorstore = FAISS.from_documents(chunks, embeddings)

# Save locally
vectorstore.save_local("vectorstore")

print("✅ Vector DB created successfully")
