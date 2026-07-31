from pydantic import BaseModel, Field


class InterfaceRequestShow(BaseModel):
    gateway_uid: str = Field(
        alias="gateway-uid",
        description="""Gateway or cluster object uid that the interface belongs to. <font color=red>Required only if</font> name was specified.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
    )
