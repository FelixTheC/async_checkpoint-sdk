from access_point_name_reply import AccessPointNameReply
from api_domain_identifier import ApiDomainIdentifier
from apply_a_p_on_traffic_reply import ApplyAPOnTrafficReply
from available_actions_reply import AvailableActionsReply
from imsi_prefix_reply import ImsiPrefixReply
from interface_profile_reply import InterfaceProfileReply
from ldap_group_reply import LdapGroupReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from ms_isdn_reply import MsIsdnReply
from pydantic import BaseModel, Field
from ra_tech_reply import RaTechReply
from selection_mode_reply import SelectionModeReply


class GtpServiceReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    version: str = Field(alias="version", description="""GTP version.""")
    access_point_name: AccessPointNameReply = Field(
        alias="access-point-name", description="""Match by Access Point Name."""
    )
    allow_usage_of_static_ip: bool = Field(
        alias="allow-usage-of-static-ip", description="""Allow usage of static IP addresses."""
    )
    apply_access_policy_on_user_traffic: ApplyAPOnTrafficReply = Field(
        alias="apply-access-policy-on-user-traffic",
        description="""Apply Access Policy on user traffic.""",
    )
    cs_fallback_and_srvcc: bool = Field(
        alias="cs-fallback-and-srvcc",
        description="""CS Fallback and SRVCC (Relevant for V2 only).""",
    )
    imsi_prefix: ImsiPrefixReply = Field(
        alias="imsi-prefix", description="""Match by IMSI prefix."""
    )
    interface_profile: InterfaceProfileReply = Field(
        alias="interface-profile",
        description="""Match only message types relevant to the given GTP interface. Relevant only for GTP V1 or V2.""",
    )
    ldap_group: LdapGroupReply = Field(
        alias="ldap-group", description="""Match by an LDAP Group."""
    )
    ms_isdn: MsIsdnReply = Field(alias="ms-isdn", description="""Match by an MS-ISDN.""")
    radio_access_technology: RaTechReply = Field(
        alias="radio-access-technology", description="""Match by Radio Access Technology."""
    )
    restoration_and_recovery: bool = Field(
        alias="restoration-and-recovery",
        description="""Restoration and Recovery (Relevant for V2 only).""",
    )
    reverse_service: bool = Field(
        alias="reverse-service",
        description="""Accept PDUs from the GGSN/PGW to the SGSN/SGW on a previously established PDP context, even if different ports are used.""",
    )
    selection_mode: SelectionModeReply = Field(
        alias="selection-mode", description="""Match by a selection mode."""
    )
    trace_management: bool = Field(
        alias="trace-management", description="""Trace Management (Relevant for V2 only)."""
    )
    type: str = Field(alias="type", description="""Object type.""")
    groups: list[dict] = Field(
        alias="groups",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
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
