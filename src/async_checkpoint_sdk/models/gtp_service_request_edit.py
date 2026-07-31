from access_point_name_request import AccessPointNameRequest
from add import Add
from apply_a_p_on_traffic_request import ApplyAPOnTrafficRequest
from imsi_prefix_request import ImsiPrefixRequest
from interface_profile_request import InterfaceProfileRequest
from ldap_group_request import LdapGroupRequest
from ms_isdn_request import MsIsdnRequest
from pydantic import BaseModel, Field
from ra_tech_request import RaTechRequest
from remove import Remove
from selection_mode_request import SelectionModeRequest


class GtpServiceRequestEdit(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    version: str = Field(alias="version", description="""GTP version.""")
    access_point_name: AccessPointNameRequest = Field(
        alias="access-point-name", description="""Match by Access Point Name."""
    )
    allow_usage_of_static_ip: bool = Field(
        alias="allow-usage-of-static-ip", description="""Allow usage of static IP addresses."""
    )
    apply_access_policy_on_user_traffic: ApplyAPOnTrafficRequest = Field(
        alias="apply-access-policy-on-user-traffic",
        description="""Apply Access Policy on user traffic.""",
    )
    cs_fallback_and_srvcc: bool = Field(
        alias="cs-fallback-and-srvcc",
        description="""CS Fallback and SRVCC (Relevant for V2 only).""",
    )
    imsi_prefix: ImsiPrefixRequest = Field(
        alias="imsi-prefix", description="""Match by IMSI prefix."""
    )
    interface_profile: InterfaceProfileRequest = Field(
        alias="interface-profile",
        description="""Match only message types relevant to the given GTP interface. Relevant only for GTP V1 or V2.""",
    )
    ldap_group: LdapGroupRequest = Field(
        alias="ldap-group", description="""Match by an LDAP Group."""
    )
    ms_isdn: MsIsdnRequest = Field(alias="ms-isdn", description="""Match by an MS-ISDN.""")
    radio_access_technology: RaTechRequest = Field(
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
    selection_mode: SelectionModeRequest = Field(
        alias="selection-mode", description="""Match by a selection mode."""
    )
    trace_management: bool = Field(
        alias="trace-management", description="""Trace Management (Relevant for V2 only)."""
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    groups: Add | Remove | str | list[str] = Field(
        alias="groups", description="""Collection of group identifiers."""
    )
    tags: Add | Remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
