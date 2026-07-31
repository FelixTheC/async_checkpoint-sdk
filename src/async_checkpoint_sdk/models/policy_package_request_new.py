from .pydantic import BaseModel, Field


class PolicyPackageRequestNew(BaseModel):
    access: bool = Field(
        alias="access",
        description="""True - enables, False - disables access & NAT policies, empty - nothing is changed.""",
    )
    desktop_security: bool = Field(
        alias="desktop-security",
        description="""True - enables, False - disables Desktop security policy, empty - nothing is changed.""",
    )
    installation_targets: str | list[str] = Field(
        alias="installation-targets",
        description="""Which Gateways identified by the name or UID to install the policy on. <br>All - Install the policy on all Gateways.<br>[] - Empty the list of specified Gateways on which to install the policy.""",
    )
    qos: bool = Field(
        alias="qos",
        description="""True - enables, False - disables QoS policy, empty - nothing is changed.""",
    )
    qos_policy_type: str = Field(alias="qos-policy-type", description="""QoS policy type.""")
    threat_prevention: bool = Field(
        alias="threat-prevention",
        description="""True - enables, False - disables Threat policy, empty - nothing is changed.""",
    )
    vpn_traditional_mode: bool = Field(
        alias="vpn-traditional-mode",
        description="""True - enables, False - disables VPN traditional mode, empty - nothing is changed.""",
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
