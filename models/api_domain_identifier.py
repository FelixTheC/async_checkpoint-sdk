from pydantic import BaseModel, Field


class ApiDomainIdentifier(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    domain_type: str = Field(alias="domain-type", description="""Domain type.""")
