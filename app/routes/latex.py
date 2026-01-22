from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.latex_extractor import extract_latex_from_image
from app.schemas.response import LatexResponse
from app.utils.image_prep import validate_and_prepare_image

router = APIRouter()

MAX_IMAGE_SIZE = 5 * 1024 * 1024  # 5 MB


@router.post("/image-to-latex", response_model=LatexResponse)
async def image_to_latex(file: UploadFile = File(...)):
    # ✅ Check file size before reading
    if file.size is not None and file.size > MAX_IMAGE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="Image too large (max 5MB)"
        )

    try:
        image_bytes = await file.read()

        image = validate_and_prepare_image(image_bytes)

        latex = extract_latex_from_image(image)

        if not latex.strip():
            raise ValueError("No LaTeX detected")

        return LatexResponse(
            success=True,
            latex=latex
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )
