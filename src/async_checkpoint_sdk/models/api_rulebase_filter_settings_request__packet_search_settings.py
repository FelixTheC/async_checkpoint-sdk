from .pydantic import BaseModel, Field


class ApiRulebaseFilterSettingsRequest_PacketSearchSettings(BaseModel):
    expand_group_members: bool = Field(
        alias="expand-group-members",
        description="""When true, if the search expression contains a UID or a name of a group object, results will include rules that match on at least one member of the group.""",
    )
    expand_group_with_exclusion_members: bool = Field(
        alias="expand-group-with-exclusion-members",
        description="""When true, if the search expression contains a UID or a name of a group-with-exclusion object, results will include rules that match at least one member of the include part and is not a member of the except part.""",
    )
    intersection_mode_dst: str = Field(
        alias="intersection-mode-dst",
        description="""When set to <b>'any'</b>, the search will match all rules where the destination column could capture the IP with 'dst:' token in the filter. When set to <b>'exact'</b>, the search will match only rules where the destination column has the exact IP/network as the IP/network in the filter with 'dst:'.<b>containing<b>: The search will match only rules where the IP/network address searched for in the filter with 'dst:' is containing thedestination column IP/network address of the rule<b>contained_in<b>: The search will match only rules where the IP/network address searched for in the filter with 'dst:' is contained within thedestination column IP/network address of the rule<br><br>NOTE: not giving any token (src/dst) and using this setting would assume dst.""",
    )
    intersection_mode_src: str = Field(
        alias="intersection-mode-src",
        description="""<b>'any'</b>: The search will match all rules where the source column could capture the IP with 'src:' token in the filter. <br><b>'exact'</b>: The search will match only rules where the source column has the exact IP/network as the IP/network in the filter with 'src:'.<br><b>containing<b>: The search will match only rules where the IP/network address searched for in the filter with 'src:' is containing thesource column IP/network address of the rule<b>contained_in<b>: The search will match only rules where the IP/network address searched for in the filter with 'src:' is contained within thesource column IP/network address of the rule<br><br>NOTE: not giving any token (src/dst) and using this setting would assume src.""",
    )
    match_on_any: bool = Field(
        alias="match-on-any", description="""Whether to match on 'Any' object."""
    )
    match_on_group_with_exclusion: bool = Field(
        alias="match-on-group-with-exclusion",
        description="""Whether to match on a group-with-exclusion.""",
    )
    match_on_negate: bool = Field(
        alias="match-on-negate", description="""Whether to match on a negated cell."""
    )
