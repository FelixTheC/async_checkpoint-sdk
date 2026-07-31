from pydantic import BaseModel, Field


class ShowRuleCandidateRequest(BaseModel):
    layer_type: str | str = Field(alias="layer-type", description="""N/A""")
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
    sub_field: str = Field(
        alias="sub-field",
        description="""Optional sub-field to the policy field.<br>For vpn field in access layer: all-gw-to-gw, specific<br>For service field in access layer: services, application-and-sites, categories, mobile-application<br>For content field in access layer: file-types<br>For protection-or-site field in exception: whitelist-files, ips-protections, anti-protection, user-applicatoin, blades.""",
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
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
    )
    show_only_local_domain: bool = Field(
        alias="show-only-local-domain",
        description="""Indicates whether the query should return only objects from the current local domain. This parameter is only valid for local domain.""",
    )
