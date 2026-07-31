from .api_object_standard_identifier import ApiObjectStandardIdentifier
from .pydantic import BaseModel, Field


class GatewayServerPolicyReply_ClusterMemberReply(BaseModel):
    name: str = Field(alias="name", description="""Cluster member name.""")
    uid: str = Field(alias="uid", description="""Cluster member unique identifier.""")
    policy_name: str = Field(
        alias="policy-name", description="""The name of the installed policy."""
    )
    revision: ApiObjectStandardIdentifier = Field(
        alias="revision", description="""Cluster member revision."""
    )
