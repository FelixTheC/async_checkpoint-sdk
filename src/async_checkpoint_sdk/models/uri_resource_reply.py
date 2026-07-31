from .api_domain_identifier import ApiDomainIdentifier
from .api_object_standard_identifier import ApiObjectStandardIdentifier
from .available_actions_reply import AvailableActionsReply
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .pydantic import BaseModel, Field
from .ufp_object_reply import UfpObjectReply
from .uri_resource_action_reply import UriResourceActionReply
from .uri_resource_connection_methods_reply import UriResourceConnectionMethodsReply
from .uri_resource_cvp_reply import UriResourceCvpReply
from .uri_resource_soap_reply import UriResourceSoapReply
from .uri_resource_wildcards_reply import UriResourceWildcardsReply


class UriResourceReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    use_this_resource_to: str = Field(
        alias="use-this-resource-to",
        description="""Select the use of the URI resource.""",
    )
    type: str = Field(alias="type", description="""Object type.""")
    connection_methods: UriResourceConnectionMethodsReply = Field(
        alias="connection-methods", description="""Connection methods."""
    )
    uri_match_specification_type: str = Field(
        alias="uri-match-specification-type",
        description="""The type can be Wild Cards or UFP, where a UFP server holds categories of forbidden web sites.""",
    )
    exception_track: ApiObjectStandardIdentifier = Field(
        alias="exception-track",
        description="""Configures how to track connections that match this rule but fail the content security checks. An example of an exception is a connection with an unsupported scheme or method.""",
    )
    match_ufp: UfpObjectReply = Field(alias="match-ufp", description="""Match - UFP settings.""")
    match_wildcards: UriResourceWildcardsReply = Field(
        alias="match-wildcards", description="""Match - Wildcards settings."""
    )
    action: UriResourceActionReply = Field(alias="action", description="""Action settings.""")
    cvp: UriResourceCvpReply = Field(alias="cvp", description="""CVP settings.""")
    soap: UriResourceSoapReply = Field(alias="soap", description="""SOAP settings.""")
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
