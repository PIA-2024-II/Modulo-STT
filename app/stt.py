import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import librosa

# Cargar modelo y tokenizador
model_name = "jonatasgrosman/wav2vec2-large-xlsr-53-spanish"
tokenizer = Wav2Vec2Tokenizer.from_pretrained(model_name)
model = Wav2Vec2ForCTC.from_pretrained(model_name)

def audio_to_text(file_path: str) -> str:
    # Cargar el archivo de audio
    audio, rate = librosa.load(file_path, sr=16000)

    # Tokenizar el audio
    input_values = tokenizer(audio, return_tensors="pt", padding="longest").input_values

    # Realizar inferencia
    with torch.no_grad():
        logits = model(input_values).logits

    # Obtener el índice de las probabilidades más altas
    predicted_ids = torch.argmax(logits, dim=-1)

    # Convertir los ids en texto
    transcription = tokenizer.batch_decode(predicted_ids)[0]

    return transcription.lower()