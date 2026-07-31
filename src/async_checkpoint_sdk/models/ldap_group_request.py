from .pydantic import BaseModel, Field


class LdapGroupRequest(BaseModel):
    enable: bool = Field(alias="enable", description="""""")
    group: str = Field(
        alias="group",
        description="""The Ldap Group object identified by Name or UID.""",
    )
    according_to: str = Field(
        alias="according-to",
        description="""According to MS-ISDN or according to IMSI.""",
    )
