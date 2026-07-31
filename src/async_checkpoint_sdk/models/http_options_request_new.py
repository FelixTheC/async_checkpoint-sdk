from pydantic import BaseModel, Field


class HttpOptionsRequestNew(BaseModel):
    destination: str = Field(alias="destination", description="""The destination URL.""")
