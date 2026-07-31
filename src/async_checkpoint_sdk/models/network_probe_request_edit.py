from .add import add
from .http_options_request import HttpOptionsRequest
from .icmp_options_request import IcmpOptionsRequest
from .pydantic import BaseModel, Field
from .remove import remove


class NetworkProbeRequestEdit(BaseModel):
    http_options: HttpOptionsRequest = Field(
        alias="http-options",
        description="""Additional options when [protocol] is set to http.""",
    )
    icmp_options: IcmpOptionsRequest = Field(
        alias="icmp-options",
        description="""Additional options when [protocol] is set to icmp.""",
    )
    install_on: add | remove | str | list[str] = Field(
        alias="install-on",
        description="""Collection of Check Point Security Gateways that generate the probe, identified by name or UID.""",
    )
    protocol: str = Field(alias="protocol", description="""The probing protocol to use.""")
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    interval: int = Field(
        alias="interval",
        description="""The time interval (in seconds) between each probe request.<br>Best Practice - The interval value should be lower than the timeout value.""",
    )
    timeout: int = Field(
        alias="timeout",
        description="""The probe expiration timeout (in seconds). If there is not a single reply within this time, the status of the probe changes to Down.""",
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from .the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
    )
    tags: add | remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
