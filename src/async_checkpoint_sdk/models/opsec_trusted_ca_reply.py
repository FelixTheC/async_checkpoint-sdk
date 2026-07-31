from .api_domain_identifier import ApiDomainIdentifier
from .automatic_enrollment_reply import AutomaticEnrollmentReply
from .available_actions_reply import AvailableActionsReply
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .pydantic import BaseModel, Field


class OpsecTrustedCaReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    base64_certificate: str = Field(
        alias="base64-certificate",
        description="""Certificate file encoded in base64.""",
    )
    automatic_enrollment: AutomaticEnrollmentReply = Field(
        alias="automatic-enrollment",
        description="""Certificate automatic enrollment.""",
    )
    retrieve_crl_from_http_servers: bool = Field(
        alias="retrieve-crl-from-http-servers",
        description="""Whether to retrieve Certificate Revocation List from .http servers.""",
    )
    retrieve_crl_from_ldap_servers: bool = Field(
        alias="retrieve-crl-from-ldap-servers",
        description="""Whether to retrieve Certificate Revocation List from .ldap servers.""",
    )
    cache_crl: bool = Field(
        alias="cache-crl",
        description="""Cache Certificate Revocation List on the Security Gateway.""",
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
        description="""Allow only certificates from .listed branches.""",
    )
    branches: list[str] = Field(
        alias="branches",
        description="""Branches to allow certificates from. Required only if allow-certificates-from-branches set to true.""",
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    icon: str = Field(alias="icon", description="""Object icon.""")
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
    read_only: bool = Field(
        alias="read-only", description="""Indicates whether the object is read-only."""
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
