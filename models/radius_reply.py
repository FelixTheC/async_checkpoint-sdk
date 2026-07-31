from api_domain_identifier import ApiDomainIdentifier
from api_object_standard_identifier import ApiObjectStandardIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field
from radius_accounting_object_reply import RadiusAccountingObjectReply


class RadiusReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    groups: list[dict] = Field(
        alias="groups",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    server: ApiObjectStandardIdentifier = Field(
        alias="server",
        description="""The UID or Name of the host that is the RADIUS Server.""",
    )
    service: ApiObjectStandardIdentifier = Field(
        alias="service",
        description="""The UID or Name of the Service to which the RADIUS server listens.""",
    )
    version: str = Field(
        alias="version",
        description="""The version can be either RADIUS Version 1.0, which is RFC 2138 compliant, and RADIUS Version 2.0 which is RFC 2865 compliant.""",
    )
    protocol: str = Field(
        alias="protocol",
        description="""The type of authentication protocol that will be used when authenticating the user to the RADIUS server.""",
    )
    priority: int = Field(
        alias="priority",
        description="""The priority of the RADIUS Server in case it is a member of a RADIUS Group.""",
    )
    accounting: RadiusAccountingObjectReply = Field(
        alias="accounting", description="""Accounting settings."""
    )
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
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
