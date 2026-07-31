from .pydantic import BaseModel, Field


class DateReply(BaseModel):
    iso_8601: str = Field(alias="iso-8601", description="""N/A""")
    posix: int = Field(alias="posix", description="""N/A""")
