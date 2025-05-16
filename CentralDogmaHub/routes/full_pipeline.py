from fastapi import APIRouter, HTTPException
from pydantic import BaseModel # Validate and parse incoming json data
from app.utils.reverse_complement import get_reverse_complement
from app.utils.transcription import transcribe
from app.utils.translation import translate

router = APIRouter() # For defining the routes 

class DNARequest(BaseModel):
    sequence: str

@router.post("/pipeline")
def process_dna(data: DNARequest):
    try:
        original = data.sequence.upper().replace(" ", "").replace("\n", "")
        reverse_comp = get_reverse_complement(original)
        transcription_original = transcribe(original)
        transcription_reverse = transcribe(reverse_comp)
        translation_original = translate(transcription_original)
        translation_reverse = translate(transcription_reverse)

        return {
            "Input_Sequence": original,
            "Reverse_Complement": reverse_comp,
            "Transcription_Original": transcription_original,
            "Transcription_Reverse": transcription_reverse,
            "Translation_Original": translation_original,
            "Translation_Reverse": translation_reverse,
        } # Sends the output to frontend    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing DNA sequence: {str(e)}")
