from fastapi import FastAPI

from app.api.routes.documents import router as documents_router
from app.api.routes.health import router as health_router


app = FastAPI(
    title="Sistema RAG API",
    description="API principal para el sistema RAG.",
    version="0.1.0",
)

app.include_router(health_router, prefix="/api")
app.include_router(documents_router, prefix="/api")

