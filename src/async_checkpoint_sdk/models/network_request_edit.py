from add import Add
from nat_settings_request import NatSettingsRequest
from pydantic import BaseModel, Field
from remove import Remove


class NetworkRequestEdit(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    subnet: str = Field(
        alias="subnet",
        description="""IPv4 or IPv6 network address. If both addresses are required use subnet4 and subnet6 fields explicitly.""",
    )
    mask_length: int = Field(
        alias="mask-length",
        description="""IPv4 or IPv6 network mask length. If both masks are required use mask-length4 and mask-length6 fields explicitly. Instead of IPv4 mask length it is possible to specify IPv4 mask itself in subnet-mask field.""",
    )
    nat_settings: NatSettingsRequest = Field(alias="nat-settings", description="""NAT settings.""")
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    broadcast: str = Field(alias="broadcast", description="""Allow broadcast address inclusion.""")
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    groups: Add | Remove | str | list[str] = Field(
        alias="groups", description="""Collection of group identifiers."""
    )
    tags: Add | Remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
