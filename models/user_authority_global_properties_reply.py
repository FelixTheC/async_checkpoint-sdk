from pydantic import BaseModel, Field


class UserAuthorityGlobalPropertiesReply(BaseModel):
    display_web_access_view: bool = Field(
        alias="display-web-access-view",
        description="""Specify whether or not to display the WebAccess rule base. This rule base is used for UserAuthority.""",
    )
    windows_domains_to_trust: str = Field(
        alias="windows-domains-to-trust",
        description="""When matching Firewall usernames to Windows Domains usernames for Single Sign on, selectwhether to trust all or specify which Windows Domain should be trusted.<br>ALL - Enables you to allow all Windows domains to access the internal sites of the organization.<br>SELECTIVELY - Enables you to specify which Windows domains will have access to the internal sites of the organization.""",
    )
    trust_only_following_windows_domains: list[str] = Field(
        alias="trust-only-following-windows-domains",
        description="""Specify which Windows domains will have access to the internal sites of the organization.<br>Available only if windows-domains-to-trust is set to SELECTIVELY.""",
    )
