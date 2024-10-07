from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from app.stt import audio_to_text
from app.tests.test_endpoints_2 import router as file_extension_router
import shutil
from mimetypes import guess_type

app = FastAPI()

# Registrar el router de file_extension.py
app.include_router(file_extension_router)

class TranscriptionResponse(BaseModel):
    transcription: str

@app.get("/")
async def home():
    return {"message": "Welcome to the Speech-to-Text API"}

@app.post("/transcribe/", response_model=TranscriptionResponse)
async def transcribe_audio(file: UploadFile = File(...)):

# Usando mime_type, se saca la extension del archivo para admitir solo audio
    mime_type, _ = guess_type(file.filename)

    if mime_type not in ["audio/wav", "audio/mpeg", "audio/x-wav"]: ##if que realiza la comprobacion, comentar de causar errores
        raise HTTPException(status_code=400, detail="Invalid file type")

    with open(f"temp_audio.{file.filename.split('.')[-1]}", "wb") as buffer: ##extrae la extension del archivo para crear la copia temporal
        shutil.copyfileobj(file.file, buffer)

    # Convertir el archivo de audio a texto
    transcription = audio_to_text(f"temp_audio.{file.filename.split('.')[-1]}")

    return {"transcription": transcription}

