from .add import add
from .api_doc_rule_base_position_object_builder import (
    ApiDocRuleBasePositionObjectBuilder,
)
from .pydantic import BaseModel, Field
from .remove import remove


class ThreatExceptionRequestEdit(BaseModel):
    action: str = Field(alias="action", description="""Action-the enforced profile.""")
    destination: add | remove | str | list[str] = Field(
        alias="destination",
        description="""Collection of Network objects identified by the name or UID.""",
    )
    destination_negate: bool = Field(
        alias="destination-negate",
        description="""True if negate is set for destination.""",
    )
    enabled: bool = Field(alias="enabled", description="""Enable/Disable the rule.""")
    exception_number: int = Field(alias="exception-number", description="""N/A""")
    install_on: add | remove | str | list[str] = Field(
        alias="install-on",
        description="""Which Gateways identified by the name or UID to install the policy on.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    new_position: int | str | ApiDocRuleBasePositionObjectBuilder = Field(
        alias="new-position", description="""New position in the rulebase."""
    )
    protected_scope: add | remove | str | list[str] = Field(
        alias="protected-scope",
        description="""Collection of objects defining Protected Scope identified by the name or UID.""",
    )
    protected_scope_negate: bool = Field(
        alias="protected-scope-negate",
        description="""True if negate is set for Protected Scope.""",
    )
    protection_or_site: add | remove | str | list[str] = Field(
        alias="protection-or-site",
        description="""Collection of protection or site identified by the name or UID.""",
    )
    service: add | remove | str | list[str] = Field(
        alias="service",
        description="""Collection of Network objects identified by the name or UID.""",
    )
    service_negate: bool = Field(
        alias="service-negate", description="""True if negate is set for Service."""
    )
    source: add | remove | str | list[str] = Field(
        alias="source",
        description="""Collection of Network objects identified by the name or UID.""",
    )
    source_negate: bool = Field(
        alias="source-negate", description="""True if negate is set for source."""
    )
    tags: add | remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    track: str = Field(alias="track", description="""Packet tracking.""")
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
