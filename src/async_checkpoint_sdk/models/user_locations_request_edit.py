from .add import add
from .pydantic import BaseModel, Field
from .remove import remove


class UserLocationsRequestEdit(BaseModel):
    destinations: add | remove | str | list[str] = Field(
        alias="destinations",
        description="""Collection of allowed destination locations name or uid.""",
    )
    sources: add | remove | str | list[str] = Field(
        alias="sources",
        description="""Collection of allowed source locations name or uid.""",
    )
