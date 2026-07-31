from folder_permissions_role_pair_request import FolderPermissionsRolePairRequest
from pydantic import BaseModel, Field


class IdpGroupRequestNew(BaseModel):
    multi_domain_profile: str = Field(
        alias="multi-domain-profile",
        description="""Administrator multi-domain profile.""",
    )
    permissions_profile: FolderPermissionsRolePairRequest | list[dict] = Field(
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
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
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
