from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class DocumentCreate(BaseModel):
    original_name: str = Field(
        min_length=1,
        max_length=255,
    )
    storage_path: str = Field(
        min_length=1,
        max_length=500,
    )
    mime_type: str = Field(
        min_length=1,
        max_length=100,
    )


class DocumentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    original_name: str
    storage_path: str
    mime_type: str
    status: str
    created_at: datetime
    updated_at: datetime