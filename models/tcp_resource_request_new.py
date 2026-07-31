from pydantic import BaseModel, Field
from tcp_resource_cvp_request_new import TcpResourceCvpRequestNew
from tcp_resource_ufp_request_new import TcpResourceUfpRequestNew


class TcpResourceRequestNew(BaseModel):
    resource_type: str = Field(
        alias="resource-type", description="""The type of the TCP resource."""
    )
    exception_track: str = Field(
        alias="exception-track",
        description="""Configures how to track connections that match this rule but fail the content security checks. An example of an exception is a connection with an unsupported scheme or method.""",
    )
    ufp_settings: TcpResourceUfpRequestNew = Field(
        alias="ufp-settings", description="""UFP settings."""
    )
    cvp_settings: TcpResourceCvpRequestNew = Field(
        alias="cvp-settings", description="""CVP settings."""
    )
    set_if_exists: bool = Field(
        alias="set-if-exists",
        description="""If another object with the same identifier already exists, it will be updated. The command behaviour will be the same as if originally a set command was called. Pay attention that original object's fields will be overwritten by the fields provided in the request payload!""",
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
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
    tags: str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
