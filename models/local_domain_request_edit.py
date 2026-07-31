from add import add
from pydantic import BaseModel, Field
from remove import remove
from update import update


class LocalDomainRequestEdit(BaseModel):
    servers: add | remove | update = Field(
        alias="servers",
        description="""Domain servers. When this field is provided, 'set-domain' command is executed asynchronously.""",
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
    tags: add | remove | str | list[str] = Field(
        alias="tags",
        description="""Collection of tag identifiers. Note: The list of tags can not be modified in a single command together with the domain servers. To modify tags, please use the separate 'set-domain' command, without providing the list of domain servers.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
