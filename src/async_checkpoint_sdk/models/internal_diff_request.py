from pydantic import BaseModel, Field


class InternalDiffRequest(BaseModel):
    from_date: str = Field(
        alias="from-date",
        description="""The date from which tracking changes is to be performed. ISO 8601. If timezone isn't specified in the input, the Management server's timezone is used.""",
    )
    from_session: str = Field(
        alias="from-session",
        description="""The session UID from which tracking changes is to be performed.""",
    )
    limit: int = Field(alias="limit", description="""Maximum number of sessions to analyze.""")
    offset: int = Field(
        alias="offset", description="""Number of sessions to skip (beginning with from-session)."""
    )
    to_date: str = Field(
        alias="to-date",
        description="""The date until which tracking changes is to be performed. ISO 8601. If timezone isn't specified in the input, the Management server's timezone is used.""",
    )
    to_session: str = Field(
        alias="to-session",
        description="""The session UID until which tracking changes is to be performed.""",
    )
    dereference_group_members: bool = Field(
        alias="dereference-group-members",
        description="""Indicates whether to dereference members field by details level for every object in reply.""",
    )
    show_membership: bool = Field(
        alias="show-membership",
        description="""Indicates whether to calculate and show groups field for every object in reply.""",
    )
    dereference_max_depth: int = Field(
        alias="dereference-max-depth",
        description="""When details level is full you can choose the number of levels in the API reply.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
