from typing import TypedDict,List

class State(TypedDict,total=False):
    user_id:str
    ticket:str
    category:str
    urgency:int
    context : List[str]
    # user_history:str
    tool_context:str
    plan: List[str]
    confidence: float
    final_answer: str
    escalated: bool
    