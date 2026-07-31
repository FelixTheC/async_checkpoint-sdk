from pydantic import BaseModel, Field


class VptAddVsxMemberRequest(BaseModel):
    ipv4_address: str = Field(
        alias="ipv4-address",
        description="""Main IPv4 Address of the VSX Cluster member.<br/>Mandatory if the VSX Cluster has an IPv4 Address.""",
    )
    ipv6_address: str = Field(
        alias="ipv6-address",
        description="""Main IPv6 Address of the VSX Cluster member.<br/>Mandatory if the VSX Cluster has an IPv6 Address.""",
    )
    name: str = Field(alias="name", description="""Name of the new VSX Cluster member.""")
    sic_otp: str = Field(
        alias="sic-otp",
        description="""SIC one-time-password of the VSX Gateway or Cluster member.<br/>Password must be between 4-127 characters in length.""",
    )
    sync_ip: str = Field(
        alias="sync-ip", description="""Sync IP address for the VSX Cluster member."""
    )
