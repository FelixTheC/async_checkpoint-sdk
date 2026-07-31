from api_rulebase_filter_settings_request import ApiRulebaseFilterSettingsRequest
from hits_settings_request import HitsSettingsRequest
from pydantic import BaseModel, Field


class QueryNatRulebaseRequest(BaseModel):
    package: str = Field(alias="package", description="""Name of the package.""")
    filter: str = Field(
        alias="filter",
        description="""Search expression to filter the rulebase. The provided text should be exactly the same as it would be given in Smart Console. The logical operators in the expression ('AND', 'OR') should be provided in capital letters. If an operator is not used, the default OR operator applies.""",
    )
    filter_settings: ApiRulebaseFilterSettingsRequest = Field(
        alias="filter-settings", description="""Sets filter preferences."""
    )
    limit: int = Field(alias="limit", description="""The maximal number of returned results.""")
    offset: int = Field(alias="offset", description="""Number of the results to initially skip.""")
    order: list[dict] = Field(
        alias="order",
        description="""Sorts the results by search criteria. Automatically sorts the results by Name, in the ascending order.""",
    )
    show_hits: bool = Field(alias="show-hits", description="""Show hitcount data.""")
    use_object_dictionary: bool = Field(alias="use-object-dictionary", description="""N/A""")
    hits_settings: HitsSettingsRequest = Field(
        alias="hits-settings",
        description="""Hitcount settings, define the range if hits to show.""",
    )
    dereference_group_members: bool = Field(
        alias="dereference-group-members",
        description="""Indicates whether to dereference members field by details level for every object in reply.""",
    )
    show_membership: bool = Field(
        alias="show-membership",
        description="""Indicates whether to calculate and show groups field for every object in reply.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
