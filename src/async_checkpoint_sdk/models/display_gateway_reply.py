from pydantic import BaseModel, Field


class DisplayGatewayReply(BaseModel):
    domain_name: str = Field(
        alias="domain-name",
        description="""The domain name to which the gateway is connected(In case of MDS - system domain mode).""",
    )
    name: str = Field(alias="name", description="""The name of the security gateway.""")
    used_quota: int = Field(
        alias="used-quota", description="""Cores quantity of the security gateway."""
    )
