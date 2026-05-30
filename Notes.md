# Gen AI with python

### Types of propmts 
- Zero shot prompting : System prompt with no examples just instructions
- Few shot prompting : System prompt with few examples and instructions
- Chain of thought prompting : System prompt with examples and detailed explanation of should model/LLM thinking process should be.
- persona based prompting: giving a persona to AI.

### Prompt styles
- Alpeca prompting : system propmt and user input and response in on string
- ChatML schema : {role: "user" | "system" | "developer" | "assistant", content: ""} like this  
- INST prompting: [INST] user instruction [/INST] everything is in the wrap of brackets.

# Steps to create RAG

- Setup vector db. docker-compose.yml 
- setup document loaders with PyPDFLoader
- setup text_spliter
- split the pdf into chunks 
- create openai embeddings out of openaiembedding model
- do the emebedding with QdrantvectorStore.from_document(docs)

# Langgraph 
- Langgraph is the low level agent workflow building tool. 
- State: In Langgraph a state is global shared object between nodes. we can store common knowledge between nodes with state.
- A node is nothing but a function which does a specific work and have access of state object.
- you can add node to graph like this 
```python 

# for adding the node in graph
graph_builder.add_node("chat", chat)
graph_builder.add_node("sample_node", sample_node)

# for adding the edge in the graph

graph_builder.add_edge(START, "chat")
graph_builder.add_edge("chat", "sample_node")
graph_builder.add_edge("sample_node", END)

# for compiling and running the graph

graph = graph_builder.compile()

updates_state = graph.invoke(State({"messages": ["Hi my name is pritam"]}))


```
- You have to pass intial stage of state in the invoke for running the graph




### Types of memory 

- Short term memory
- Long term Memory 
- Episodic term Memory 
- Symentic term Memory 
- Factual term Memory 
