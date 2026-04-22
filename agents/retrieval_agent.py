from ..retrieval.chroma_retriever import ChromaRetriever

retriever = ChromaRetriever()

def retrieve_documents(state:dict)->dict:

    """
    LangGraph Retrieval Node

    Input state:
        state["ticket"] : str

    Output added to state:
        state["context"] : list[str]
    """
    ticket = state["ticket"]

    docs = retriever.retrieve(ticket)

    state["context"] = docs

    return state