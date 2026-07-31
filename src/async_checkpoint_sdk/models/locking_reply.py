from .api_object_standard_identifier import ApiObjectStandardIdentifier
from .pydantic import BaseModel, Field


class LockingReply(BaseModel):
    object: ApiObjectStandardIdentifier = Field(
        alias="object",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
