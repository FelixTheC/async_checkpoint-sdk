from .pydantic import BaseModel, Field


class MultiValueAccessLayer(BaseModel):
    add: list[dict] = Field(
        alias="add",
        description="""Collection of Access layer objects to be added identified by the name or UID.""",
    )
    remove: list[str] = Field(
        alias="remove",
        description="""Collection of Access layer objects to be removed identified by the name or UID.""",
    )
    value: list[str] = Field(
        alias="value",
        description="""Collection of Access layer objects to be set identified by the name or UID. Replaces existing Access layers.""",
    )
