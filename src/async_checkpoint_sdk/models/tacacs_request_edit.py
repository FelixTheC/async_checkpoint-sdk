from add import Add
from pydantic import BaseModel, Field
from remove import Remove


class TacacsRequestEdit(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    secret_key: str = Field(
        alias="secret-key",
        description="""The server's secret key.<br><font color=red>Required only when</font> server-type was selected to be TACACS+.""",
    )
    server: str = Field(
        alias="server", description="""The UID or Name of the host that is the TACACS Server."""
    )
    encryption: bool = Field(
        alias="encryption",
        description="""Is there a secret key defined on the server. Must be set true when server-type was selected to be TACACS+.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    priority: int = Field(
        alias="priority",
        description="""The priority of the TACACS Server in case it is a member of a TACACS Group.""",
    )
    server_type: str = Field(alias="server-type", description="""Server type, TACACS or TACACS+.""")
    service: str = Field(
        alias="service", description="""Server service, only relevant when server-type is TACACS."""
    )
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
