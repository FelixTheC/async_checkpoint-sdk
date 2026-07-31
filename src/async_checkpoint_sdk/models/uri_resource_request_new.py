from pydantic import BaseModel, Field
from ufp_object_request import UfpObjectRequest
from uri_resource_action_request import UriResourceActionRequest
from uri_resource_connection_methods_request import UriResourceConnectionMethodsRequest
from uri_resource_cvp_request import UriResourceCvpRequest
from uri_resource_soap_request import UriResourceSoapRequest
from uri_resource_wildcards_request import UriResourceWildcardsRequest


class UriResourceRequestNew(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    use_this_resource_to: str = Field(
        alias="use-this-resource-to", description="""Select the use of the URI resource."""
    )
    connection_methods: UriResourceConnectionMethodsRequest = Field(
        alias="connection-methods", description="""Connection methods."""
    )
    uri_match_specification_type: str = Field(
        alias="uri-match-specification-type",
        description="""The type can be Wild Cards or UFP, where a UFP server holds categories of forbidden web sites.""",
    )
    exception_track: str = Field(
        alias="exception-track",
        description="""Configures how to track connections that match this rule but fail the content security checks. An example of an exception is a connection with an unsupported scheme or method.""",
    )
    match_ufp: UfpObjectRequest = Field(alias="match-ufp", description="""Match - UFP settings.""")
    match_wildcards: UriResourceWildcardsRequest = Field(
        alias="match-wildcards", description="""Match - Wildcards settings."""
    )
    action: UriResourceActionRequest = Field(alias="action", description="""Action settings.""")
    cvp: UriResourceCvpRequest = Field(alias="cvp", description="""CVP settings.""")
    soap: UriResourceSoapRequest = Field(alias="soap", description="""SOAP settings.""")
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
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
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
