from .pydantic import BaseModel, Field


class IpRanges(BaseModel):
    ipv4: list[dict] = Field(
        alias="ipv4",
        description="""Range of IPv4 addresses that match in the given rule.""",
    )
    ipv6: list[dict] = Field(
        alias="ipv6",
        description="""Range of IPv6 addresses that match in the given rule.""",
    )
    others: list[dict] = Field(
        alias="others",
        description="""Objects which are not represented as IP addresses and match the given rule. The details-level parameter of the request determines whether they are displayed as UID's or objects.""",
    )
    excluded_others: list[dict] = Field(
        alias="excluded-others",
        description="""Objects which are not represented as IP addresses and are negated in the given rule - for example if negate is set for the source or destination of this rule, or if they appear in the 'exclude' member of a group-with-exclusion object. The details-level parameter of the request determines whether they are displayed as UID's or objects.""",
    )
