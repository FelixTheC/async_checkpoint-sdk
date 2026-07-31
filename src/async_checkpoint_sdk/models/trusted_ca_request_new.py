from pydantic import BaseModel, Field


class TrustedCaRequestNew(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    base64_certificate: str = Field(
        alias="base64-certificate", description="""Certificate file encoded in base64."""
    )
    retrieve_crl_from_http_servers: bool = Field(
        alias="retrieve-crl-from-http-servers",
        description="""Whether to retrieve Certificate Revocation List from http servers.""",
    )
    crl_cache_method: str = Field(
        alias="crl-cache-method",
        description="""Weather to retrieve new Certificate Revocation List after the certificate expires or after a fixed period.""",
    )
    crl_cache_timeout: int = Field(
        alias="crl-cache-timeout",
        description="""When to fetch new Certificate Revocation List (in minutes).""",
    )
    allow_certificates_from_branches: bool = Field(
        alias="allow-certificates-from-branches",
        description="""Allow only certificates from listed branches.""",
    )
    branches: str | list[str] = Field(
        alias="branches",
        description="""Branches to allow certificates from. Required only if allow-certificates-from-branches set to true.""",
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
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
