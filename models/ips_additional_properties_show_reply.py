from api_domain_identifier import ApiDomainIdentifier
from ips_additional_properties_reply import IpsAdditionalPropertiesReply
from pydantic import BaseModel, Field


class IpsAdditionalPropertiesShowReply(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    object: IpsAdditionalPropertiesReply = Field(alias="object", description="""N/A""")
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
