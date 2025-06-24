from fastapi import FastAPI, Request
from pydantic import BaseModel
import openai
import os

app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")

class PromptRequest(BaseModel):
    query: str

@app.post("/ask")
def ask(prompt: PromptRequest):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt.query}],
    )
    return {"response": response.choices[0].message["content"]}
