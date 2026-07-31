from .pydantic import BaseModel, Field


class OtherRangeRequest(BaseModel):
    enable: bool = Field(alias="enable", description="""""")
    types: str = Field(
        alias="types",
        description="""Other RAT Types. To specify other RAT ranges, add a hyphen between the lowest and the highest numbers, for example: 11-15. Multiple Ranges can be chosen when separated with comma.""",
    )
