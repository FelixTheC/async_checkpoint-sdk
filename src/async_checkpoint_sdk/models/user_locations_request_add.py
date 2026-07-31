from .pydantic import BaseModel, Field


class UserLocationsRequestAdd(BaseModel):
    destinations: str | list[str] = Field(
        alias="destinations",
        description="""Collection of allowed destination locations name or uid.""",
    )
    sources: str | list[str] = Field(
        alias="sources",
        description="""Collection of allowed source locations name or uid.""",
    )
