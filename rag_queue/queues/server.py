from fastapi import FastAPI, Body

app  = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}