from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ai_core.gemini_generator import GeminiDocumentGenerator

router = APIRouter()

try:
    gemini_generator = GeminiDocumentGenerator()
except Exception:
    gemini_generator = None

class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    dates: str

@router.post("/generate")
def generate_legal_document(request: DocumentRequest):
    """Generates legal document content via Gemini AI."""
    if not gemini_generator:
        raise HTTPException(
            status_code=500, 
            detail="Gemini Generator is not configured. Please supply a valid GEMINI_API_KEY."
        )
    
    try:
        response_text = gemini_generator.generate_document(
            document_type=request.document_type,
            parties=request.parties,
            terms=request.terms,
            dates=request.dates
        )
        return {"document": response_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Document Generation Failed: {str(e)}")