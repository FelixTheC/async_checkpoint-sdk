from .pydantic import BaseModel, Field


class FolderPermissionsRolePairRequest(BaseModel):
    domain: str = Field(alias="domain", description="""N/A""")
    profile: str = Field(alias="profile", description="""Permission profile.""")
