from pydantic import BaseModel, Field


class BaseDomainQueryRequest(BaseModel):
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
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
    )
