from pydantic import BaseModel, Field


class AzureADContentRequest(BaseModel):
    limit: int = Field(
        alias="limit", description="""The maximal number of returned results."""
    )
    offset: int = Field(
        alias="offset", description="""Number of the results to initially skip."""
    )
    order: list[dict] = Field(
        alias="order",
        description="""Sorts the results by search criteria. Automatically sorts the results by Name, in the ascending order.""",
    )
    uid_in_azure_ad: str = Field(
        alias="uid-in-azure-ad",
        description="""Return result matching the unique identifier of the object on the Azure AD Server.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""Standard and Full description are the same.""",
    )
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
    )
