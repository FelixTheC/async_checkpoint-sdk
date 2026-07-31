from pydantic import BaseModel, Field


class InterfaceStandardReply_ClusterMemberInterfaceOverview(BaseModel):
    member_ip_addresses: str = Field(
        alias="member-ip-addresses",
        description="""IPv4 and IPv6 network address and network mask length.""",
    )
    member_uid: str = Field(alias="member-uid", description="""Cluster member uid.""")
