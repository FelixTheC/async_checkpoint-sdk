from pydantic import BaseModel, Field


class KeywordsAndPhrasesReply(BaseModel):
    keyword: str = Field(
        alias="keyword", description="""keyword or regular expression to be weighted."""
    )
    weight: int = Field(alias="weight", description="""weight of the expression.""")
    max_weight: int = Field(
        alias="max-weight", description="""max weight of the expression."""
    )
    regex: bool = Field(
        alias="regex",
        description="""Determine weather to consider the expression as a regular expression.""",
    )
