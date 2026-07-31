from .pydantic import BaseModel, Field


class GlobalAssignmentRequestEdit(BaseModel):
    dependent_domain: str = Field(alias="dependent-domain", description="""N/A""")
    global_access_policy: str = Field(
        alias="global-access-policy",
        description="""Global domain access policy that is assigned to a dependent domain.""",
    )
    global_domain: str = Field(alias="global-domain", description="""Global domain name or UID.""")
    global_threat_prevention_policy: str = Field(
        alias="global-threat-prevention-policy",
        description="""Global domain threat prevention policy that is assigned to a dependent domain.""",
    )
    manage_protection_actions: bool = Field(
        alias="manage-protection-actions", description="""N/A"""
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
