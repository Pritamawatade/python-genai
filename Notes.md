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