import os
from chromadb import Client
from chromadb.config import Settings
import chromadb

# Path where KB text files are stored
KB_PATH = "data/kb"

# Create Chroma client with persistence
client = chromadb.PersistentClient(path="chroma_db")#creates a local database
collection = client.get_or_create_collection(name = "support_kb")

KB_PATH = "data/kb"

documents = []
ids = []

for idx,filename in enumerate(os.listdir(KB_PATH)):
    if filename.endswith(".txt"):
        file_path = os.path.join(KB_PATH,filename)

    with open(file_path,"r",encoding="utf-8") as f:
        text = f.read()
        documents.append(text)
        ids.append(f"doc_{idx}")

collection.add(documents=documents,ids = ids)#Converts docs to embeddings

print("Knowledge Base ingestion successful!")
print("Total documents stored:", len(documents))
