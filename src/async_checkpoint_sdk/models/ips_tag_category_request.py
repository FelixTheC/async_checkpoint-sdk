from pydantic import BaseModel, Field


class IpsTagCategoryRequest(BaseModel):
    uid: str = Field(
        alias="uid",
        description="""IPS tag unique identifier. Alternatively it is possible to address IPS tag by name and category name pair.""",
    )
