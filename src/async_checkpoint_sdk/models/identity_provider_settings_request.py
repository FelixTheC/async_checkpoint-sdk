from .pydantic import BaseModel, Field


class IdentityProviderSettingsRequest(BaseModel):
    providers: str | list[str] = Field(
        alias="providers",
        description="""List of identity provider object references. At least one provider must be specified when using identity provider authentication.""",
    )
