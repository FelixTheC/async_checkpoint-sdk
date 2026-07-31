from .pydantic import BaseModel, Field


class WorkSessionObjectIdentifierRequest(BaseModel):
    uid: str = Field(alias="uid", description="""Session unique identifier.""")
