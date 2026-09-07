from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.session import get_db


router = APIRouter(tags=["health"])


@router.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "rag-api",
    }


@router.get("/health/database")
def database_health_check(
    database: Session = Depends(get_db),
) -> dict[str, str]:
    database.execute(text("SELECT 1"))

    return {
        "status": "ok",
        "database": "connected",
    }