from add import Add
from authentication_method_request_edit import AuthenticationMethodRequestEdit
from pydantic import BaseModel, Field
from remove import Remove
from user_directories_settings_request_edit import UserDirectoriesSettingsRequestEdit


class ClientLoginOptionRequestEdit(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    display_name: str = Field(
        alias="display-name", description="""Display name for the client login option."""
    )
    authentication_methods: Add | Remove | AuthenticationMethodRequestEdit | list[dict] = Field(
        alias="authentication-methods",
        description="""Array of authentication methods that define the login sequence.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    user_directories: UserDirectoriesSettingsRequestEdit = Field(
        alias="user-directories",
        description="""Select one or more places where the Security Gateway searches to find users when they try to authenticate.""",
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
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
