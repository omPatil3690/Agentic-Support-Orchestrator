import chromadb 

class ChromaRetriever:
    def __init__(self,path="chroma_db",collection_name="support_kb"):
        self.client = chromadb.PersistentClient(path="chroma_db")
        self.collection = self.client.get_collection(collection_name)

    def retrieve(self,query:str,k:int = 2) -> list[str]:
        results = self.collection.query(query_texts=[query],n_results=k)
        return results["documents"][0]