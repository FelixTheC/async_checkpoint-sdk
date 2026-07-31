from pydantic import BaseModel, Field


class LsmClusterInterfaceReply(BaseModel):
    name: str = Field(alias="name", description="""Interface Name.""")
    cluster_ip_address_override: str = Field(
        alias="cluster-ip-address-override",
        description="""Cluster IP address override.""",
    )
    member_network_override: str = Field(
        alias="member-network-override", description="""Member network override."""
    )
