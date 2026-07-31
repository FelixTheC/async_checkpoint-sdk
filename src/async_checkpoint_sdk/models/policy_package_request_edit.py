from add import Add
from https_layers_request_edit import HttpsLayersRequestEdit
from multi_value_access_layer import MultiValueAccessLayer
from multi_value_threat_layer import MultiValueThreatLayer
from pydantic import BaseModel, Field
from remove import Remove


class PolicyPackageRequestEdit(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    access: bool = Field(
        alias="access",
        description="""True - enables, False - disables access & NAT policies, empty - nothing is changed.""",
    )
    access_layers: MultiValueAccessLayer = Field(
        alias="access-layers", description="""Access policy layers."""
    )
    desktop_security: bool = Field(
        alias="desktop-security",
        description="""True - enables, False - disables Desktop security policy, empty - nothing is changed.""",
    )
    https_inspection_layers: HttpsLayersRequestEdit = Field(
        alias="https-inspection-layers", description="""HTTPS inspection policy layers."""
    )
    installation_targets: Add | Remove | str | list[str] = Field(
        alias="installation-targets",
        description="""Which Gateways identified by the name or UID to install the policy on. <br>All - Install the policy on all Gateways.<br>[] - Empty the list of specified Gateways on which to install the policy.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    qos: bool = Field(
        alias="qos",
        description="""True - enables, False - disables QoS policy, empty - nothing is changed.""",
    )
    qos_policy_type: str = Field(alias="qos-policy-type", description="""QoS policy type.""")
    threat_layers: MultiValueThreatLayer = Field(
        alias="threat-layers", description="""Threat policy layers."""
    )
    threat_prevention: bool = Field(
        alias="threat-prevention",
        description="""True - enables, False - disables Threat policy, empty - nothing is changed.""",
    )
    vpn_traditional_mode: bool = Field(
        alias="vpn-traditional-mode",
        description="""True - enables, False - disables VPN traditional mode, empty - nothing is changed.""",
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
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
