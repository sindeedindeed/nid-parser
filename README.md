# NID Parser

## Project overview
A containerized web application designed to extract and parse structured data from National ID cards. The system accepts images of both sides of an ID card, processes them gracefully to handle missing or unreadable fields (outputting "N/A"), and returns the extracted information to a custom-built UI.

## Technology stack
* Backend: Python 3.14, FastAPI, Uvicorn
* Frontend: HTML5, CSS3, Vanilla JavaScript
* Deployment: Docker, Docker Compose
* Data Validation: Pydantic

## AI/OCR libraries used
* Google GenAI SDK: Serves as the core OCR and intelligence engine. The application utilizes the Gemini Vision and Text APIs for multimodal extraction, bypassing traditional OCR libraries in favor of AI-driven semantic parsing.

## Build instructions
The application is fully containerized. To build the Docker image manually, run the following command in the project root:

    docker build -t nid-parser .

## Run instructions
You do not need to modify any source code to run this application. The required .env file containing the API key is included in the project directory for evaluation purposes.

To build and start the system simultaneously, run:

    docker compose up --build

Once the terminal displays "Application startup complete", open your web browser and navigate to: http://localhost:8000

## API endpoint(s)

### GET /
* Description: Serves the frontend web interface.
* Response: HTML document containing the custom UI.

### POST /extract
* Description: Accepts the front and back images of the NID and returns the extracted data. 
* Content-Type: multipart/form-data
* Parameters:
  * front_image (File): Image of the front of the NID.
  * back_image (File): Image of the back of the NID.
* Response Format: JSON