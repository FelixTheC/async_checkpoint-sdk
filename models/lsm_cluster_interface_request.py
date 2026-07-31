from pydantic import BaseModel, Field


class LsmClusterInterfaceRequest(BaseModel):
    new_name: str = Field(
        alias="new-name",
        description="""New name. Overrides the interface name on profile.""",
    )
    ip_address_override: str = Field(
        alias="ip-address-override",
        description="""IP address override. Net mask is defined by the attached LSM profile.""",
    )
    member_network_override: str = Field(
        alias="member-network-override",
        description="""Member network override. Net mask is defined by the attached LSM profile.""",
    )
