from .api_object_standard_identifier import ApiObjectStandardIdentifier
from .pydantic import BaseModel, Field


class ShowRuleCandidateReply(BaseModel):
    default_object: ApiObjectStandardIdentifier = Field(
        alias="default-object", description="""Default object of the field."""
    )
    source: int = Field(
        alias="from", description="""from .which element number the query was done."""
    )
    objects: list[dict] = Field(
        alias="objects",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    to: int = Field(alias="to", description="""To which element number the query was done.""")
    total: int = Field(
        alias="total", description="""Total number of elements returned by the query."""
    )
