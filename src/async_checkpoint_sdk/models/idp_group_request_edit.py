from .add import add
from .folder_permissions_role_pair_request import FolderPermissionsRolePairRequest
from .pydantic import BaseModel, Field
from .remove import remove


class IdpGroupRequestEdit(BaseModel):
    group_id: str = Field(
        alias="group-id",
        description="""Group ID or Name should be set base on the source attribute of 'groups' in the Saml Assertion.""",
    )
    multi_domain_profile: str = Field(
        alias="multi-domain-profile",
        description="""Administrator multi-domain profile.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    permissions_profile: add | remove | FolderPermissionsRolePairRequest | list[dict] = Field(
        alias="permissions-profile",
        description="""Administrator permissions profile. Permissions profile should not be provided when multi-domain-profile is set to Multi-Domain Super User or Domain Super User.""",
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
