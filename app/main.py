from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.latex import router as latex_router

app = FastAPI(
    title="Image to LaTeX API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change later if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(latex_router, prefix="/api")

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Image → LaTeX backend running"}