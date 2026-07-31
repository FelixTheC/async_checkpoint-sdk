from pydantic import BaseModel, Field


class CmeApiCmdRequest(BaseModel):
    payload: str = Field(
        alias="payload", description="""The payload of CME API request body."""
    )
