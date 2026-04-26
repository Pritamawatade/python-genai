from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
class State(TypedDict):
    messages: Annotated[list, add_messages]
    

def chat(state: State):
    print("\n\nChat node called with state:", state)
    return {"messages": ["Hello, how can I help you?"]}    

def sample_node(state: State):
    print("\n\nSample node called with state:", state)
    return {"messages": ["This is a sample node."]}
graph_builder = StateGraph(State)

graph_builder.add_node("chat", chat)

graph_builder.add_node("sample_node", sample_node)


graph_builder.add_edge(START, "chat")
graph_builder.add_edge("chat", "sample_node")
graph_builder.add_edge("sample_node", END)




graph = graph_builder.compile()

updates_state = graph.invoke(State({"messages": ["Hi my name is pritam"]}))
print("\n\nFinal state after invoking the graph:", updates_state)

# (START) -> chat -> sample_node -> (END)



