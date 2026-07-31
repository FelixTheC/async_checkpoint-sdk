from pydantic import BaseModel, Field


class GrcFwRuleObjectReferenceObjectReply(BaseModel):
    name: str = Field(alias="name", description="""The name of the reference object.""")
    reference_object_type: str = Field(
        alias="reference-object-type",
        description="""The type of the reference object.""",
    )
    uid: str = Field(alias="uid", description="""The UID of the reference object.""")
