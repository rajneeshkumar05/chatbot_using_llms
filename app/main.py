from fastapi import FastAPI
from langchain_community.llms import Ollama

app = FastAPI()

llm = Ollama(model="llama3", base_url="http://localhost:11434")

@app.get("/chat")
def chat(query: str):
     response = llm.invoke(query) 
     return {"response": response}  