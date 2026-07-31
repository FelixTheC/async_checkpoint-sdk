from pydantic import BaseModel, Field


class AddWithPosition(BaseModel):
    name: str = Field(alias="name", description="""Layer name or UID.""")
    position: int = Field(alias="position", description="""Layer position.""")
