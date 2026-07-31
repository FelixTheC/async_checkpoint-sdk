from .pydantic import BaseModel, Field


class WhereUsedObjectRequest(BaseModel):
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
    indirect: bool = Field(alias="indirect", description="""Search for indirect usage.""")
    indirect_max_depth: int = Field(
        alias="indirect-max-depth",
        description="""Maximum nesting level during indirect usage search.""",
    )
