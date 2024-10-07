from fastapi.testclient import TestClient
from app.main import app
import mimetypes

client = TestClient(app)

def test_home(): #Da la bienvenida de abrirlo en navegador
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Speech-to-Text API"}

def test_transcribe(): #Endpoint importante, es el que devuelve el texto en la terminal
     # Se tiene un diccionario con todas las extensiones posibles para su lectura
    file_extensions = ["wav", "mp3", "x-wav"]

    for ext in file_extensions: # Lee todas las extensione hasta encontrar la primera que posea el nombre sample
        file_path = f"app/tests/sample.{ext}"

        # Determinar el tipo MIME basado en la extensión del archivo
        mime_type, _ = mimetypes.guess_type(file_path)

        # Abrir el archivo y enviarlo al endpoint
        with open(file_path, "rb") as audio_file:
            response = client.post("/transcribe/", files={"file": (file_path, audio_file, mime_type)})

        assert response.status_code == 200
        assert "transcription" in response.json()