from cluster_profile_topology_reply import ClusterProfileTopologyReply
from pydantic import BaseModel, Field


class LsmClusterProfileInterfaceReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    network_address: str = Field(alias="network-address", description="""N/A""")
    network_mask: str = Field(alias="network-mask", description="""N/A""")
    network_type: str = Field(alias="network-type", description="""N/A""")
    topology: ClusterProfileTopologyReply = Field(
        alias="topology", description="""N/A"""
    )
