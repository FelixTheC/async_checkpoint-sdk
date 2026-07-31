from add import Add
from pydantic import BaseModel, Field
from remove import Remove


class IdentityProviderRequestEdit(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    usage: str = Field(alias="usage", description="""Usage of Identity Provider.""")
    gateway: str = Field(
        alias="gateway",
        description="""Gateway for the SAML Identity Provider usage.
Identified by name or UID. <font color=red>Required only when</font> 'usage' is set to 'gateway_policy_and_logs'.""",
    )
    service: str = Field(
        alias="service",
        description="""Service for the selected gateway. <font color=red>Required only when</font> 'usage' is set to 'gateway_policy_and_logs'.""",
    )
    data_receiving: str = Field(
        alias="data-receiving",
        description="""Data receiving method from the SAML Identity Provider.""",
    )
    received_identifier: str = Field(
        alias="received-identifier",
        description="""Received Identifier (Entity ID) based on the provider data. <font color=red>Required only when</font> 'data-receiving' is set to 'manually'.""",
    )
    login_url: str = Field(
        alias="login-url",
        description="""Login URL based on the provider data. <font color=red>Required only when</font> 'data-receiving' is set to 'manually'.""",
    )
    base64_metadata_file: str = Field(
        alias="base64-metadata-file",
        description="""Metadata file encoded in base64 based on the provider data. <font color=red>Required only when</font> 'data-receiving' is set to 'metadata_file'.""",
    )
    base64_certificate: str = Field(
        alias="base64-certificate",
        description="""Certificate file encoded in base64 based on provider data. <font color=red>Required only when</font> 'data-receiving' is set to 'manually'.""",
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
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
