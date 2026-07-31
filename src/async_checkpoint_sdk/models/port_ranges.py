from .pydantic import BaseModel, Field


class PortRanges(BaseModel):
    tcp: list[dict] = Field(
        alias="tcp", description="""Range of TCP ports that match in the given rule."""
    )
    udp: list[dict] = Field(
        alias="udp", description="""Range of UDP ports that match in the given rule."""
    )
    others: list[dict] = Field(
        alias="others",
        description="""Objects which are not represented as port numbers and match the given rule. The details-level parameter of the request determines whether they are displayed as UID's or objects.""",
    )
    excluded_others: list[dict] = Field(
        alias="excluded-others",
        description="""Objects which are not represented as port numbers and are negated in the given rule - for example if negate is set for the service of this rule. The details-level parameter of the request determines whether they are displayed as UID's or objects.""",
    )
