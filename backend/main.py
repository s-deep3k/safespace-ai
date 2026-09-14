# Setup FastAPI backend
from fastapi import FastAPI, Query
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Receive and validate requests from frontend
class Query(BaseModel):
    message: str

@app.post("/ask")
async def ask(query: Query):
    #AI Agent
    return "This is my response from the backend."

# Send response back to frontend

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)