from fastapi import FastAPI, Query
from rag_queue.client.rq_client import q
from rag_queue.client.worker import process_query

app  = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/chat")
def chat(message: str = Query(..., description="The message to send to the model")):
    job =q.enqueue(process_query, message)

    return {"status": "queued", "job_id": job.id}