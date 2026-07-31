from .pydantic import BaseModel, Field


class ProtectionQueryRequest(BaseModel):
    filter: str = Field(
        alias="filter",
        description="""Search expression to filter threat protections by.""",
    )
    limit: int = Field(alias="limit", description="""The maximal number of returned results.""")
    offset: int = Field(alias="offset", description="""Number of the results to initially skip.""")
    order: list[dict] = Field(
        alias="order",
        description="""Sorts the results by search criteria. Automatically sorts the results by Name, in the ascending order.""",
    )
    show_capture_packets_and_track: bool = Field(
        alias="show-capture-packets-and-track",
        description="""Indicates whether to calculate and show Capture Packets And Track field in reply.""",
    )
    show_ips_additional_properties: bool = Field(
        alias="show-ips-additional-properties",
        description="""Indicates whether to calculate and show ips additional properties field in reply when details level is full.""",
    )
    show_profiles: bool = Field(
        alias="show-profiles",
        description="""Indicates whether to calculate and show profiles field in reply when details level is full.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from .the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
    )
    show_only_local_domain: bool = Field(
        alias="show-only-local-domain",
        description="""Indicates whether the query should return only objects from .the current local domain. This parameter is only valid for local domain.""",
    )
