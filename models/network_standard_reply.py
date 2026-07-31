from api_domain_identifier import ApiDomainIdentifier
from pydantic import BaseModel, Field


class NetworkStandardReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    subnet4: str = Field(alias="subnet4", description="""IPv4 network address.""")
    subnet6: str = Field(alias="subnet6", description="""IPv6 network address.""")
    mask_length4: int = Field(
        alias="mask-length4", description="""IPv4 network mask length."""
    )
    mask_length6: int = Field(
        alias="mask-length6", description="""IPv6 network mask length."""
    )
    subnet_mask: str = Field(alias="subnet-mask", description="""IPv4 network mask.""")
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    icon: str = Field(alias="icon", description="""Object icon.""")
