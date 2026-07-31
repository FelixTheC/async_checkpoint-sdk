from add import Add
from api_doc_rule_base_position_object_builder import ApiDocRuleBasePositionObjectBuilder
from pydantic import BaseModel, Field
from remove import Remove


class NatRuleRequestEdit(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    package: str = Field(alias="package", description="""Name of the package.""")
    enabled: bool = Field(alias="enabled", description="""Enable/Disable the rule.""")
    install_on: Add | Remove | str | list[str] = Field(
        alias="install-on",
        description="""Which Gateways identified by the name or UID to install the policy on.""",
    )
    method: str = Field(alias="method", description="""Nat method.""")
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    new_position: int | str | ApiDocRuleBasePositionObjectBuilder = Field(
        alias="new-position", description="""New position in the rulebase."""
    )
    original_destination: str = Field(
        alias="original-destination", description="""Original destination."""
    )
    original_service: str = Field(alias="original-service", description="""Original service.""")
    original_source: str = Field(alias="original-source", description="""Original source.""")
    tags: Add | Remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    translated_destination: str = Field(
        alias="translated-destination", description="""Translated  destination."""
    )
    translated_service: str = Field(
        alias="translated-service", description="""Translated  service."""
    )
    translated_source: str = Field(alias="translated-source", description="""Translated  source.""")
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
