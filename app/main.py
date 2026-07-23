from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from app.utils import validate_image
from app.models import NIDResponse
from app.services import extract_nid_data
import os

app = FastAPI(
    title = "NID Parser API",
    description= "AI-powered application to extract and translate NID information.",
    version="1.0.0"
)

@app.get("/", response_class=FileResponse)
async def serve_ui():
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "index.html")
    return FileResponse(file_path)

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
    
    extracted_data = extract_nid_data(front_bytes, back_bytes)

    return extracted_data
