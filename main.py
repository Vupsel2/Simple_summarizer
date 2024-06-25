from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from langchain import PromptTemplate
from langchain.llms import AI21
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

class TextRequest(BaseModel):
    text: str

template = """Summarize the following text:
{text}
"""

prompt = PromptTemplate(input_variables=["text"], template=template)

llm = AI21(ai21_api_key=os.getenv("API_KEY"))

summarization_chain = prompt| llm

@app.post("/summarize")
async def summarize_text(request: TextRequest):
    try:
        input_text = request.text
        summary = summarization_chain.invoke({"text": input_text})
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Запуск приложения
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
