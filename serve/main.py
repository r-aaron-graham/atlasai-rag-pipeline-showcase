import os
import re

from fastapi import FastAPI, HTTPException
from openai import OpenAI, OpenAIError
from pydantic import BaseModel, Field

app = FastAPI()
RETENTION_POLICY = "Synthetic policy: retain review records for 30 days."


class PromptRequest(BaseModel):
    query: str = Field(min_length=1, max_length=2000)


@app.post("/ask")
def ask(prompt: PromptRequest):
    if os.getenv("ATLASAI_PROVIDER") == "openai":
        try:
            response = OpenAI().chat.completions.create(
                model=os.getenv("ATLASAI_MODEL", "gpt-4"),
                messages=[{"role": "user", "content": prompt.query}],
            )
        except OpenAIError as exc:
            raise HTTPException(502, "Model provider request failed") from exc
        return {"response": response.choices[0].message.content, "sources": []}

    if re.search(r"\bretention\b", prompt.query, re.IGNORECASE):
        return {"response": RETENTION_POLICY, "sources": ["fixture-retention"]}
    return {"response": None, "sources": []}
