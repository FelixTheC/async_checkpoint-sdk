from pydantic import BaseModel, Field


class UpgradeMessagesReply(BaseModel):
    global_and_system_domain_title: str = Field(
        alias="global-and-system-domain-title",
        description="""Global and System domain prepare message title.""",
    )
    global_and_system_domain_body: str = Field(
        alias="global-and-system-domain-body",
        description="""Global and System domain prepare message body.""",
    )
    local_domain_title: str = Field(
        alias="local-domain-title",
        description="""Local domain prepare message title.""",
    )
    local_domain_body: str = Field(
        alias="local-domain-body", description="""Local domain prepare message body."""
    )
