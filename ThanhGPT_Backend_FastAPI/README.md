# ThanhGPT Backend (FastAPI)

## 🚀 Hướng dẫn chạy server

### 1. Cài thư viện
```bash
pip install -r requirements.txt
```

### 2. Cài đặt Tesseract OCR (nếu chưa có)
- Windows: https://github.com/tesseract-ocr/tesseract/wiki
- Ubuntu/Debian:
```bash
sudo apt install tesseract-ocr -y
```

### 3. Chạy server FastAPI
```bash
uvicorn main:app --reload
```

Sau đó truy cập: http://localhost:8000/docs để test API.

### 4. Ghi đè OpenAI API Key trong `main.py`
```python
openai.api_key = "YOUR_OPENAI_API_KEY"
```

## ✅ API
- POST `/api/solve` → giải bài văn bản
- POST `/api/image` → trích xuất đề từ ảnh

Sử dụng kèm với giao diện HTML ThanhGPT.