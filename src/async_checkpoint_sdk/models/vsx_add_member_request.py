from pydantic import BaseModel, Field


class VsxAddMemberRequest(BaseModel):
    ipv4_address: str = Field(
        alias="ipv4-address",
        description="""The IPv4 address of the management interface of the VSX Cluster member.""",
    )
    ipv4_sync_address: str = Field(
        alias="ipv4-sync-address",
        description="""The IPv4 address of the sync interface of the VSX Cluster member.""",
    )
    member_name: str = Field(
        alias="member-name", description="""Name of the new VSX Cluster member object."""
    )
    vsx_name: str = Field(alias="vsx-name", description="""Name of the VSX Cluster object.""")
