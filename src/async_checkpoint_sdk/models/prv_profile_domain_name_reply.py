from pydantic import BaseModel, Field


class PrvProfileDomainNameReply(BaseModel):
    manage_settings: str = Field(
        alias="manage-settings",
        description="""Manage settings mode: locally on the device or centrally from this application.""",
    )
    override_settings: str = Field(
        alias="override-settings",
        description="""Override settings mode: allowed, mandatory or denied. Relevant only when settings are managed centrally.""",
    )
    name: str = Field(alias="name", description="""Domain Name.""")
