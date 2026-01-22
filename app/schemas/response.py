from pydantic import BaseModel

class LatexResponse(BaseModel):
    success: bool
    latex: str
