from object import Object
from pydantic import BaseModel, Field


class TacacsRequestNew(BaseModel):
    encryption: bool = Field(
        alias="encryption",
        description="""Is there a secret key defined on the server. Must be set true when server-type was selected to be TACACS+.""",
    )
    priority: int = Field(
        alias="priority",
        description="""The priority of the TACACS Server in case it is a member of a TACACS Group.""",
    )
    server_type: str = Field(
        alias="server-type", description="""Server type, TACACS or TACACS+."""
    )
    service: str = Field(
        alias="service",
        description="""Server service, only relevant when server-type is TACACS.""",
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
    groups: Object = Field(
        alias="groups", description="""Collection of group identifiers."""
    )
    tags: str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
