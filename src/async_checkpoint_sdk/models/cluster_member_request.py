from cluster_member_interface_request import ClusterMemberInterfaceRequest
from object import Object
from pydantic import BaseModel, Field


class ClusterMemberRequest(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    auto_generate_ip: bool = Field(
        alias="auto-generate-ip",
        description="""Use an automatically generated IP address for the Gateway object (applies only to Smart-1 Cloud).""",
    )
    interfaces: ClusterMemberInterfaceRequest | list[dict] = Field(
        alias="interfaces", description="""Cluster Member network interfaces."""
    )
    ip_address: str = Field(
        alias="ip-address",
        description="""IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    one_time_password: str = Field(alias="one-time-password", description="""N/A""")
    trust_method: str = Field(
        alias="trust-method", description="""Trust method to use for establishing communication."""
    )
    priority: int = Field(
        alias="priority",
        description="""In a High Availability New mode cluster each machine is given a priority. The highest priority machine serves as the gateway in normal circumstances. If this machine fails, control is passed to the next highest priority machine. If that machine fails, control is passed to the next machine, and so on.
In Load Sharing Unicast mode cluster, the highest priority is the pivot machine.
The values must be in a range from 1 to N, where N is number of cluster members.""",
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    tags: Object = Field(alias="tags", description="""Collection of tag identifiers.""")
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
