from pydantic import BaseModel, Field


class CifsResourceRequestNew(BaseModel):
    log_mapped_shares: bool = Field(
        alias="log-mapped-shares", description="""Logs each share map attempt."""
    )
    log_access_violation: bool = Field(
        alias="log-access-violation",
        description="""Logs any attempt to violate the restrictions imposed by the Resource.""",
    )
    block_remote_registry_access: bool = Field(
        alias="block-remote-registry-access",
        description="""Blocks the ability to remotely manipulate a the window's registry.""",
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
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
    tags: str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
