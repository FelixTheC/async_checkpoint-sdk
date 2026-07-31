from pydantic import BaseModel, Field


class LsmGatewayClusterCommonRequestShow(BaseModel):
    show_statuses: bool = Field(
        alias="show-statuses",
        description="""Show statuses for an LSM Gateway or a Cluster.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
