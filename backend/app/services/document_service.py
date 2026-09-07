from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.document import Document
from app.schemas.document import DocumentCreate


def create_document(
    database: Session,
    document_data: DocumentCreate,
) -> Document:
    document = Document(
        **document_data.model_dump(),
        status="pending",
    )

    database.add(document)
    database.commit()
    database.refresh(document)

    return document

def list_documents(
    database: Session,
) -> list[Document]:
    query = select(Document).order_by(
        Document.created_at.desc()
    )

    result = database.execute(query)

    return list(result.scalars().all())