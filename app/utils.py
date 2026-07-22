from fastapi import HTTPException, UploadFile
from PIL import Image
import io

ALLOWED_EXTENSIONS = {"image/jpeg", "image/png", "image/jpg"}

async def validate_image(file: UploadFile, label: str) -> bytes:
    if file.content_type not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code = 400,
            detail=f"Unsupported file type for {label}. Please upload JPG, JPEG or PNG"
        )
    
    try:
        content = await file.read()
        img = Image.open(io.BytesIO(content))
        img.verify()
        return content
    except Exception:
        raise HTTPException(
            status_code=400,
            detail=f"The {label} image is corrupted or unreadable"
        )
        