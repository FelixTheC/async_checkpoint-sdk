from .pydantic import BaseModel, Field


class ApiDateReply(BaseModel):
    iso_8601: str = Field(
        alias="iso-8601",
        description="""Date and time represented in international ISO 8601 format.""",
    )
    posix: int = Field(
        alias="posix",
        description="""Number of milliseconds that have elapsed since 00:00:00, 1 January 1970.""",
    )
