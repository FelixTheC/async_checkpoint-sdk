from http_options_request_new import HttpOptionsRequestNew
from pydantic import BaseModel, Field


class NetworkProbeRequestNew(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    http_options: HttpOptionsRequestNew = Field(
        alias="http-options", description="""Additional options when [protocol] is set to http."""
    )
    install_on: str | list[str] = Field(
        alias="install-on",
        description="""Collection of Check Point Security Gateways that generate the probe, identified by name or UID.""",
    )
    protocol: str = Field(alias="protocol", description="""The probing protocol to use.""")
    interval: int = Field(
        alias="interval",
        description="""The time interval (in seconds) between each probe request.<br>Best Practice - The interval value should be lower than the timeout value.""",
    )
    timeout: int = Field(
        alias="timeout",
        description="""The probe expiration timeout (in seconds). If there is not a single reply within this time, the status of the probe changes to Down.""",
    )
    set_if_exists: bool = Field(
        alias="set-if-exists",
        description="""If another object with the same identifier already exists, it will be updated. The command behaviour will be the same as if originally a set command was called. Pay attention that original object's fields will be overwritten by the fields provided in the request payload!""",
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
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
