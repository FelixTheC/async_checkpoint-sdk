from add import Add
from pydantic import BaseModel, Field
from remove import Remove


class UserLocationsRequestEdit(BaseModel):
    destinations: Add | Remove | str | list[str] = Field(
        alias="destinations",
        description="""Collection of allowed destination locations name or uid.""",
    )
    sources: Add | Remove | str | list[str] = Field(
        alias="sources", description="""Collection of allowed source locations name or uid."""
    )
