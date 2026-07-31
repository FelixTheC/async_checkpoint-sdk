from .pydantic import BaseModel, Field


class DenyExpiredServerCertRequest(BaseModel):
    override_profile: bool = Field(
        alias="override-profile",
        description="""Override profile of global configuration.""",
    )
    value: bool = Field(
        alias="value",
        description="""Override value.<br><font color=red>Required only for</font> 'override-profile' is True.""",
    )
