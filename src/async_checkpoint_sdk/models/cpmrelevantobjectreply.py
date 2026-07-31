from pydantic import BaseModel, Field


class Cpmrelevantobjectreply(BaseModel):
    cpm_relevant_object_type: str = Field(
        alias="cpm-relevant-object-type", description="""The type of the relevant object."""
    )
    enabled: bool = Field(
        alias="enabled",
        description="""Shows if the Compliance scan is enabled or not for this object.""",
    )
    name: str = Field(alias="name", description="""The name of the relevant object.""")
    status: str = Field(alias="status", description="""The status of the relevant object.""")
    uid: str = Field(alias="uid", description="""The UID of the relevant object.""")
