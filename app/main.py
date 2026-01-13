from fastapi import FastAPI
from langchain_ollama import OllamaLLM
app = FastAPI()

llm = OllamaLLM(model="llama3", base_url="http://localhost:11434")

@app.get("/")
def chat(query: str):
     response = llm.invoke(query) 
     return {"response": response}  