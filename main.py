
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from agents import AGENTS  

# Load Gemini API key from .env
load_dotenv()
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

# Initialize FastAPI
app = FastAPI(title="Multi-Agent AI System")

# Pydantic model for requests
class TaskRequest(BaseModel):
    agents: List[str]
    prompt: str

@app.get("/")
async def root():
    return {"message": "Welcome to Multi-Agent AI System! Use POST /agent to submit tasks."}

@app.post("/agent")
async def run_agents(task: TaskRequest):
    results = {}
    for agent_name in task.agents:
        if agent_name not in AGENTS:
            raise HTTPException(status_code=400, detail=f"Agent '{agent_name}' not found")
        try:
            # Calling the agent function
            results[agent_name] = AGENTS[agent_name](task.prompt)
        except Exception as e:
            results[agent_name] = f"Error: {str(e)}"
    return {"prompt": task.prompt, "results": results}
