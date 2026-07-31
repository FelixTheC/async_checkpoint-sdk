from pydantic import BaseModel, Field


class ComplianceShowBestPracticeQueryRequest(BaseModel):
    blade: str | list[str] = Field(
        alias="blade",
        description="""Returns all the relevant Best Practices of the selected Software Blades. When empty will return all the Best Practices.""",
    )
    limit: int = Field(alias="limit", description="""The maximal number of returned results.""")
    offset: int = Field(alias="offset", description="""Number of the results to initially skip.""")
    show_regulations: bool = Field(
        alias="show-regulations",
        description="""Show the applicable regulations of the Best Practice.""",
    )
    status: str | list[str] = Field(
        alias="status",
        description="""Returns all the relevant best practices with the selected statuses. When empty will return all best practices.""",
    )
    gateway_name: str = Field(
        alias="gateway-name",
        description="""Returns all the relevant Best Practices of the selected Security Gateway object.""",
    )
    defined_by: str = Field(
        alias="defined-by",
        description="""Returns all the relevant Best Practices of the selected type.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    show_only_local_domain: bool = Field(
        alias="show-only-local-domain",
        description="""Indicates whether the query should return only objects from the current local domain. This parameter is only valid for local domain.""",
    )
