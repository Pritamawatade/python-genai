from fastapi import FastAPI, Query
from rag_queue.client.rq_client import q

app  = FastAPI()

# Runnable from `rag_queue/` as cwd (e.g. `rq worker`); not `rag_queue.client...`.
JOB_PROCESS_QUERY = "client.worker.process_query"

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/chat")
def chat(message: str = Query(..., description="The message to send to the model")):
    job = q.enqueue(JOB_PROCESS_QUERY, message)

    return {"status": "queued", "job_id": job.id}

@app.get('/job-status')
def get_result(job_id: str = Query(..., description="The job id to get the result of")):
    job = q.fetch_job(job_id=job_id)
    
    result = job.return_value()
    
    return {"status": "completed", "result": result} 