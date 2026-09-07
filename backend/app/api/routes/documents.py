from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.document import Document
from app.schemas.document import DocumentCreate, DocumentResponse
from app.services.document_service import (create_document,list_documents,)


router = APIRouter(
    prefix="/documents",
    tags=["documents"],
)


@router.post(
    "",
    response_model=DocumentResponse,
    status_code=status.HTTP_201_CREATED,
)
def store_document(
    document_data: DocumentCreate,
    database: Session = Depends(get_db),
) -> Document:
    return create_document(
        database=database,
        document_data=document_data,
    )

@router.get(
    "",
    response_model=list[DocumentResponse],
)
def index_documents(
    database: Session = Depends(get_db),
) -> list[Document]:
    return list_documents(database)