from .pydantic import BaseModel, Field


class PortalWebSettingsReply(BaseModel):
    aliases: list[str] = Field(
        alias="aliases",
        description="""List of URL aliases that are redirected to the main portal URL.""",
    )
    ip_address: str = Field(
        alias="ip-address",
        description="""Optional: IP address for the web portal to use, if your DNS server fails to resolve the main portal URL.
Note: If your DNS server resolves the main portal URL, this IP address is ignored.""",
    )
    main_url: str = Field(alias="main-url", description="""The main URL for the web portal.""")
