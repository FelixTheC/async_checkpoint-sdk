from api_domain_identifier import ApiDomainIdentifier
from pydantic import BaseModel, Field


class RuleReply(BaseModel):
    name: str = Field(alias="name", description="""Object name.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    rule_number: int = Field(alias="rule-number", description="""Rule number.""")
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    icon: str = Field(alias="icon", description="""Object icon.""")
