
from pydantic import BaseModel

class TextCorrection(BaseModel):
    text: str

class CorrectedText(BaseModel):
    id: int
    text: str
    corrected_text: str
