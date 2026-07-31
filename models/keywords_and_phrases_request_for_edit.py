from pydantic import BaseModel, Field


class KeywordsAndPhrasesRequestForEdit(BaseModel):
    weight: int = Field(alias="weight", description="""Weight of the expression.""")
    max_weight: int = Field(
        alias="max-weight", description="""Max weight of the expression."""
    )
    regex: bool = Field(
        alias="regex",
        description="""Determine whether to consider the expression as a regular expression.""",
    )
