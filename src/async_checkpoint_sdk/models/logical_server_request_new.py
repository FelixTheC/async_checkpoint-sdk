from .pydantic import BaseModel, Field


class LogicalServerRequestNew(BaseModel):
    server_type: str = Field(
        alias="server-type", description="""Type of server for the logical server."""
    )
    persistence_mode: bool = Field(
        alias="persistence-mode",
        description="""Indicates if persistence mode is enabled for the logical server.""",
    )
    persistency_type: str = Field(
        alias="persistency-type",
        description="""Persistency type for the logical server.""",
    )
    balance_method: str = Field(
        alias="balance-method",
        description="""Load balancing method for the logical server.""",
    )
    set_if_exists: bool = Field(
        alias="set-if-exists",
        description="""If another object with the same identifier already exists, it will be updated. The command behaviour will be the same as if originally a set command was called. Pay attention that original object's fields will be overwritten by the fields provided in the request payload!""",
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
