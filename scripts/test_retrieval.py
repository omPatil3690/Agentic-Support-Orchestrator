from chromadb import Client
from chromadb.config import Settings
import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection("support_kb")

query = "My account is locked and I cannot login"

results = collection.query(
    query_texts=[query],
    n_results=2
)

print("\n")
print(query)

print("\n")
for doc in results["documents"][0]:
    print("-----")
    print(doc)