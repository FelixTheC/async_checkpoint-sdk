from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from http_options_reply import HttpOptionsReply
from icmp_options_reply import IcmpOptionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class NetworkProbeReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    http_options: HttpOptionsReply = Field(
        alias="http-options",
        description="""Additional options when [protocol] is set to http.""",
    )
    icmp_options: IcmpOptionsReply = Field(
        alias="icmp-options",
        description="""Additional options when [protocol] is set to icmp.""",
    )
    install_on: list[dict] = Field(
        alias="install-on",
        description="""Collection of Check Point Security Gateways that generate the probe. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    protocol: str = Field(
        alias="protocol", description="""The probing protocol to use."""
    )
    type: str = Field(alias="type", description="""Object type.""")
    interval: int = Field(
        alias="interval",
        description="""The time interval (in seconds) between each probe request.<br>Best Practice - The interval value should be lower than the timeout value.""",
    )
    timeout: int = Field(
        alias="timeout",
        description="""The probe expiration timeout (in seconds). If there is not a single reply within this time, the status of the probe changes to Down.""",
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
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
