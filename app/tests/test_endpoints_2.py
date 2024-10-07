from fastapi import APIRouter, File, UploadFile
import mimetypes

router = APIRouter()

@router.post("/file-extension/")
async def get_file_extension(file: UploadFile = File(...)):
    extension = file.filename.split('.')[-1]

    # Se saca el mime_type con la extension
    mime_type, _ = mimetypes.guess_type(file.filename)

    return {
        "Nombre del archivo": file.filename,
        "Extension": extension,
        "Mime_type": mime_type
    }
