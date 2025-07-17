from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import openai
import pytesseract
from PIL import Image
import io

openai.api_key = "YOUR_OPENAI_API_KEY"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class SolveRequest(BaseModel):
    question: str
    grade: str
    type: str

@app.post("/api/solve")
async def solve(req: SolveRequest):
    prompt = f"Giải bài toán lớp {req.grade}, loại {req.type}:
{req.question}"
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Bạn là trợ lý AI Toán học chuyên giải đề bài chi tiết."},
            {"role": "user", "content": prompt}
        ]
    )
    return {"answer": response.choices[0].message.content}

@app.post("/api/image")
async def solve_from_image(file: UploadFile = File(...)):
    content = await file.read()
    image = Image.open(io.BytesIO(content))
    extracted_text = pytesseract.image_to_string(image, lang='eng+vie')
    return {"extracted_text": extracted_text.strip()}