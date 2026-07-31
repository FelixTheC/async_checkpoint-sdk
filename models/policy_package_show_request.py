from pydantic import BaseModel, Field


class PolicyPackageShowRequest(BaseModel):
    show_installation_targets: bool = Field(
        alias="show-installation-targets",
        description="""Indicates whether to calculate and show installation-targets field in reply.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
