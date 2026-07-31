from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from prv_profile_configuration_script_reply import PrvProfileConfigurationScriptReply
from prv_profile_dns_reply import PrvProfileDnsReply
from prv_profile_domain_name_reply import PrvProfileDomainNameReply
from prv_profile_hosts_reply import PrvProfileHostsReply
from prv_profile_hotspot_reply import PrvProfileHotspotReply
from prv_profile_radius_reply import PrvProfileRadiusReply
from pydantic import BaseModel, Field


class PrvProfileReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    configuration_script: PrvProfileConfigurationScriptReply = Field(
        alias="configuration-script",
        description="""Configuration Script Settings. Relevant only for Gaia Embedded (SMB) profile.""",
    )
    dns: PrvProfileDnsReply = Field(alias="dns", description="""DNS Settings.""")
    domain_name: PrvProfileDomainNameReply = Field(
        alias="domain-name", description="""Domain Name Settings."""
    )
    groups: list[dict] = Field(
        alias="groups",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    hosts: PrvProfileHostsReply = Field(alias="hosts", description="""Hosts Settings.""")
    hotspot: PrvProfileHotspotReply = Field(
        alias="hotspot",
        description="""Hotspot Settings. Relevant only for Gaia Embedded (SMB) profile.""",
    )
    radius: PrvProfileRadiusReply = Field(
        alias="radius",
        description="""RADIUS Servers Settings. Relevant only for Gaia Embedded (SMB) profile.""",
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain", description="""Information about the domain that holds the Object."""
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
        alias="available-actions", description="""Actions that are available on the object."""
    )
