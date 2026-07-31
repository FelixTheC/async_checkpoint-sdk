from nat_settings_request import NatSettingsRequest
from pydantic import BaseModel, Field


class NetworkRequestNew(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    subnet: str = Field(
        alias="subnet",
        description="""IPv4 or IPv6 network address. If both addresses are required use subnet4 and subnet6 fields explicitly.""",
    )
    mask_length: int = Field(
        alias="mask-length",
        description="""IPv4 or IPv6 network mask length. If both masks are required use mask-length4 and mask-length6 fields explicitly. Instead of IPv4 mask length it is possible to specify IPv4 mask itself in subnet-mask field.""",
    )
    nat_settings: NatSettingsRequest = Field(alias="nat-settings", description="""NAT settings.""")
    broadcast: str = Field(alias="broadcast", description="""Allow broadcast address inclusion.""")
    set_if_exists: bool = Field(
        alias="set-if-exists",
        description="""If another object with the same identifier already exists, it will be updated. The command behaviour will be the same as if originally a set command was called. Pay attention that original object's fields will be overwritten by the fields provided in the request payload!""",
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    groups: str | list[str] = Field(
        alias="groups", description="""Collection of group identifiers."""
    )
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
