from .api_object_standard_identifier import ApiObjectStandardIdentifier
from .pydantic import BaseModel, Field


class InstallationTargetRevisionReply(BaseModel):
    target_name: str = Field(
        alias="target-name", description="""The name of the installation target."""
    )
    target_uid: str = Field(
        alias="target-uid", description="""Installation target unique identifier."""
    )
    revision: ApiObjectStandardIdentifier = Field(
        alias="revision",
        description="""The revision installed on this target. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
