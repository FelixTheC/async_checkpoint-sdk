from .pydantic import BaseModel, Field


class GroupRequestQuery(BaseModel):
    filter: str = Field(
        alias="filter",
        description="""Search expression to filter objects by. The provided text should be exactly the same as it would be given in SmartConsole Object Explorer. The logical operators in the expression ('AND', 'OR') should be provided in capital letters. The search involves both a IP search and a textual search in name, comment, tags etc.""",
    )
    limit: int = Field(alias="limit", description="""The maximal number of returned results.""")
    offset: int = Field(alias="offset", description="""Number of the results to initially skip.""")
    order: list[dict] = Field(
        alias="order",
        description="""Sorts the results by search criteria. Automatically sorts the results by Name, in the ascending order.""",
    )
    show_as_ranges: bool = Field(
        alias="show-as-ranges",
        description="""When true, the group's matched content is displayed as ranges of IP addresses rather than network objects.<br />Objects that are not represented using IP addresses are presented as objects.<br />The 'members' parameter is omitted from .the response and instead the 'ranges' parameter is displayed.""",
    )
    dereference_group_members: bool = Field(
        alias="dereference-group-members",
        description="""Indicates whether to dereference members field by details level for every object in reply.""",
    )
    show_membership: bool = Field(
        alias="show-membership",
        description="""Indicates whether to calculate and show groups field for every object in reply.""",
    )
    async_response: bool = Field(
        alias="async-response",
        description="""Run command in asynchronous mode and return task UID. Use show-task command to check the progress of the task.""",
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
