import os
import json
from google import genai
from google.genai import types
from fastapi import HTTPException
from app.models import NIDResponse

# Ensure API key is loaded from environment variables
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def extract_nid_data(front_bytes: bytes, back_bytes: bytes) -> NIDResponse:
    prompt = """
    You are a highly accurate data extraction system.
    Read the provided front and back images of a Bangladesh National ID (NID).
    Translate all Bengali fields into meaning-preserving English.
    Return ONLY a JSON object matching this exact structure. Do not invent data. 
    If a field is unreadable or missing, return null for that field.
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[
                prompt,
                types.Part.from_bytes(data=front_bytes, mime_type='image/jpeg'),
                types.Part.from_bytes(data=back_bytes, mime_type='image/jpeg')
            ],
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=NIDResponse,
                temperature=0.1
            )
        )
        
        # Parse the structured JSON response
        extracted_data = json.loads(response.text)
        return NIDResponse(**extracted_data)
        
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to process NID images via LLM: {str(e)}"
        )