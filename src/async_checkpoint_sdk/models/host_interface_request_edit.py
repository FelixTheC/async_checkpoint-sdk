from pydantic import BaseModel, Field


class HostInterfaceRequestEdit(BaseModel):
    name: str = Field(alias="name", description="""Interface name.""")
    subnet: str = Field(
        alias="subnet",
        description="""IPv4 or IPv6 network address. If both addresses are required use subnet4 and subnet6 fields explicitly.""",
    )
    mask_length: int = Field(
        alias="mask-length",
        description="""IPv4 or IPv6 network mask length. If both masks are required use mask-length4 and mask-length6 fields explicitly. Instead of IPv4 mask length it is possible to specify IPv4 mask itself in subnet-mask field.""",
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
