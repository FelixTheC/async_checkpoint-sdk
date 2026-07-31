from pydantic import BaseModel, Field


class IdentityProviderSettingsReply(BaseModel):
    providers: list[str] = Field(
        alias="providers",
        description="""List of identity provider object references. At least one provider must be specified when using identity provider authentication.""",
    )
