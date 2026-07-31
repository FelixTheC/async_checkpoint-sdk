from api_doc_rule_base_position_object_builder import ApiDocRuleBasePositionObjectBuilder
from pydantic import BaseModel, Field


class TLSRuleRequestNew(BaseModel):
    position: int | str | ApiDocRuleBasePositionObjectBuilder = Field(
        alias="position", description="""Position in the rulebase."""
    )
    layer: str = Field(
        alias="layer", description="""Layer that holds the Object. Identified by the Name or UID."""
    )
    name: str = Field(alias="name", description="""HTTPS rule name.""")
    destination: str | list[str] = Field(
        alias="destination",
        description="""Collection of Network objects identified by Name or UID that represents connection destination.""",
    )
    service: str | list[str] = Field(
        alias="service",
        description="""Collection of Network objects identified by Name or UID that represents connection service.""",
    )
    source: str | list[str] = Field(
        alias="source",
        description="""Collection of Network objects identified by Name or UID that represents connection source.""",
    )
    action: str = Field(alias="action", description="""Rule inspect level. Bypass or Inspect.""")
    blade: str | list[str] = Field(
        alias="blade",
        description="""Blades for HTTPS Inspection. Identified by Name or UID of the blade.""",
    )
    certificate: str = Field(
        alias="certificate",
        description="""Internal Server Certificate identified by Name or UID,
otherwise, Outbound Certificate is a default value.""",
    )
    destination_negate: bool = Field(
        alias="destination-negate", description="""TRUE if negate value is set for Destination."""
    )
    enabled: bool = Field(alias="enabled", description="""Enable/Disable the rule.""")
    install_on: str | list[str] = Field(
        alias="install-on",
        description="""Which Gateways identified by the name or UID to install the policy on.""",
    )
    service_negate: bool = Field(
        alias="service-negate", description="""TRUE if negate value is set for Service."""
    )
    site_category: str | list[str] = Field(
        alias="site-category",
        description="""Collection of Site Categories objects identified by the name or UID.""",
    )
    site_category_negate: bool = Field(
        alias="site-category-negate",
        description="""TRUE if negate value is set for Site Category.""",
    )
    source_negate: bool = Field(
        alias="source-negate", description="""TRUE if negate value is set for Source."""
    )
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
    track: str = Field(
        alias="track",
        description="""None,Log,Alert,Mail,SNMP trap,Mail,User Alert 1, User Alert 2, User Alert 3.""",
    )
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
