from fastapi import FastAPI, UploadFile, File, HTTPException
from app.utils import validate_image

app = FastAPI(
    title = "NID Parser API",
    description= "AI-powered application to extract and translate NID information.",
    version="1.0.0"
)

@app.post("/parse-nid")
async def parse_nid(
    front_image: UploadFile = File(..., description="Front side"),
    back_image: UploadFile = File(..., description="Back side")
):
    
    if not front_image or not back_image:
        raise HTTPException(
            status_code=400,
            detail="Both the front and back side of the NID are required"
        )
    
    # using from utils.py file
    front_bytes = await validate_image(front_image, "front")
    back_bytes = await validate_image(back_image, "back")
    
    return {
        "status": "Success",
        "message": "Validation successful. Ready for OCR",
        "front_image_size": len(front_bytes),
        "back_image_size": len(back_bytes)
    }
