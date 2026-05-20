from typing_extensions import TypedDict, Literal
from typing import Optional
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    user_query: str
    llm_output: Optional[str]
    is_good: Optional[bool]
    
graph_builder = StateGraph(State)

def evaluate_response(state: State) -> Literal["chatbot_gemini", "end"]:
    # Placeholder for evaluation logic
    print("Print evaluate_response", state)
    if False:
        return "end"
    return "chatbot_gemini"

def chatbot_gemini(state: State) -> State:
    # Placeholder for chatbot response generation logic
    print("Print chatbot_gemini", state)
    return {
        "user_query": state["user_query"],
        "llm_output": "Generated response from Gemini",
        "is_good": None
    }

def end(state: State) -> None:
    print("Print end", state)
    
graph_builder.add_node(START, evaluate_response)
graph_builder.add_node("evaluate_response", evaluate_response)
graph_builder.add_node("chatbot_gemini", chatbot_gemini)
graph_builder.add_conditional_edges("chatbot", evaluate_response)
graph_builder.add_node("end", end)