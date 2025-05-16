# CentralDogmaHub API

**Version:** 1.0.0  
**Description:** A FastAPI-based bioinformatics backend API implementing core molecular biology sequence operations — reverse complement, transcription, and translation

---

## Project Overview

CentralDogmaHub API provides a modular FastAPI backend for essential biological sequence transformations. It enables clients to:

- Obtain the reverse complement of DNA sequences  
- Transcribe DNA sequences into RNA  
- Translate RNA sequences into proteins  

---

## Project Structure

```plaintext
app/
├── main.py                       # Main FastAPI app and router inclusion
├── routes/
│   └── full_pipeline.py          # Router with API endpoints
├── utils/
│   ├── reverse_complement.py     # Reverse complement logic
│   ├── transcriptio.py           # Transcription logic
│   └── translation.py            # Translation logic
├── tests/
│   └── test_full_pipeline.py     # Unit tests for API endpoints
└── frontend/
    └── index.py                  # Optional frontend integration or placeholder'''

##Installation
pip install -r requirements.txt

## Running the application 
uvicorn app.main:app --reload
Then go to : http://localhost:8000 

## For Testing
pytest CentralDogmaHub/tests/

