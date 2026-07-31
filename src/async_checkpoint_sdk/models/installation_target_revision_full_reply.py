from api_object_standard_identifier import ApiObjectStandardIdentifier
from pydantic import BaseModel, Field


class InstallationTargetRevisionFullReply(BaseModel):
    target_name: str = Field(
        alias="target-name", description="""The name of the installation target."""
    )
    target_uid: str = Field(
        alias="target-uid", description="""Installation target unique identifier."""
    )
    cluster_members_revision: list[dict] = Field(
        alias="cluster-members-revision",
        description="""If this target is a cluster, this list shows a revision which was installed on each cluster member.""",
    )
    revision: ApiObjectStandardIdentifier = Field(
        alias="revision",
        description="""The revision installed on this target. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
