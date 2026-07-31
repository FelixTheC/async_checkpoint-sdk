from cluster_member_request import ClusterMemberRequest
from pydantic import BaseModel, Field


class update(BaseModel):
    update: ClusterMemberRequest = Field(
        alias="update", description="""Updates a value from a collection"""
    )
