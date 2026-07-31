from .pydantic import BaseModel, Field


class ConnectSessionRequest(BaseModel):
    uid: str = Field(alias="uid", description="""Session unique identifier.""")
