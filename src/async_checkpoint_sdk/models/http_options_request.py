from pydantic import BaseModel, Field


class HttpOptionsRequest(BaseModel):
    destination: str = Field(alias="destination", description="""The destination URL.""")
