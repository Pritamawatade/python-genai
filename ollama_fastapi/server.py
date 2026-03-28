from fastapi import FastAPI, Body
from ollama import ChatResponse, chat, Client
app = FastAPI()
client = Client(
    host="http://localhost:11434"
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/chat")
def chat(
    message: str = Body(..., description="The message to send to the model")
):
    response: ChatResponse  = client.chat(model="phi3:3.8b", messages=[{"role": "user", "content": message}])
    print(response.message.content)
    return {"response": response.message.content}