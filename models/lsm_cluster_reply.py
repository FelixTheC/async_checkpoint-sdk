from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field
from topology_reply import TopologyReply


class LsmClusterReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    dynamic_objects: list[dict] = Field(
        alias="dynamic-objects", description="""Dynamic Objects."""
    )
    interfaces: list[dict] = Field(alias="interfaces", description="""Interfaces.""")
    main_ip_address: str = Field(
        alias="main-ip-address", description="""Main ip-address."""
    )
    members: list[dict] = Field(alias="members", description="""Cluster members.""")
    os_name: str = Field(
        alias="os-name", description="""Device platform operating system."""
    )
    security_profile: str = Field(
        alias="security-profile", description="""Attached LSM profile."""
    )
    topology: TopologyReply = Field(alias="topology", description="""Topology.""")
    version: str = Field(alias="version", description="""Device platform version.""")
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    icon: str = Field(alias="icon", description="""Object icon.""")
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
    read_only: bool = Field(
        alias="read-only", description="""Indicates whether the object is read-only."""
    )
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
