from .pydantic import BaseModel, Field


class NatSettingsRequest(BaseModel):
    hide_behind: str = Field(
        alias="hide-behind",
        description="""Hide behind method. This parameter is forbidden in case method parameter is static.""",
    )
    install_on: str = Field(
        alias="install-on",
        description="""Which gateway should apply the NAT translation.""",
    )
    method: str = Field(alias="method", description="""NAT translation method.""")
