from add import add
from machines_source_and_selection_request import MachinesSourceAndSelectionRequest
from pydantic import BaseModel, Field
from remove import remove
from users_source_and_selection_request import UsersSourceAndSelectionRequest


class AccessRoleRequestEdit(BaseModel):
    machines: str | add | remove | MachinesSourceAndSelectionRequest | list[dict] = (
        Field(alias="machines", description="""Machines that can access the system.""")
    )
    networks: add | remove | str | list[str] = Field(
        alias="networks",
        description="""Collection of Network objects identified by the name or UID that can access the system.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    remote_access_clients: str = Field(
        alias="remote-access-clients",
        description="""Remote access clients identified by name or UID.""",
    )
    users: str | add | remove | UsersSourceAndSelectionRequest | list[dict] = Field(
        alias="users", description="""Users that can access the system."""
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
        alias="tags", description="""Collection of tag identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
