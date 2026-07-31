from api_doc_rule_base_position_object_builder import ApiDocRuleBasePositionObjectBuilder
from pydantic import BaseModel, Field


class ThreatExceptionRequestNew(BaseModel):
    name: str = Field(alias="name", description="""The name of the exception.""")
    position: int | str | ApiDocRuleBasePositionObjectBuilder = Field(
        alias="position", description="""Position in the rulebase."""
    )
    exception_group_uid: str = Field(
        alias="exception-group-uid", description="""The UID of the exception-group."""
    )
    layer: str = Field(
        alias="layer",
        description="""Layer that the rule belongs to identified by the name or UID.""",
    )
    rule_uid: str = Field(alias="rule-uid", description="""The UID of the parent rule.""")
    action: str = Field(alias="action", description="""Action-the enforced profile.""")
    destination: str | list[str] = Field(
        alias="destination",
        description="""Collection of Network objects identified by the name or UID.""",
    )
    destination_negate: bool = Field(
        alias="destination-negate", description="""True if negate is set for destination."""
    )
    enabled: bool = Field(alias="enabled", description="""Enable/Disable the rule.""")
    install_on: str | list[str] = Field(
        alias="install-on",
        description="""Which Gateways identified by the name or UID to install the policy on.""",
    )
    protected_scope: str | list[str] = Field(
        alias="protected-scope",
        description="""Collection of objects defining Protected Scope identified by the name or UID.""",
    )
    protected_scope_negate: bool = Field(
        alias="protected-scope-negate", description="""True if negate is set for Protected Scope."""
    )
    protection_or_site: str | list[str] = Field(
        alias="protection-or-site",
        description="""Collection of protection or site identified by the name or UID.""",
    )
    service: str | list[str] = Field(
        alias="service",
        description="""Collection of Network objects identified by the name or UID.""",
    )
    service_negate: bool = Field(
        alias="service-negate", description="""True if negate is set for Service."""
    )
    source: str | list[str] = Field(
        alias="source",
        description="""Collection of Network objects identified by the name or UID.""",
    )
    source_negate: bool = Field(
        alias="source-negate", description="""True if negate is set for source."""
    )
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
    track: str = Field(alias="track", description="""Packet tracking.""")
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
