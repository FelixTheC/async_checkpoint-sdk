from pydantic import BaseModel, Field


class ManualDetachment(BaseModel):
    layer: str = Field(
        alias="layer",
        description="""The layer of the threat rule to which the group is to be attached.""",
    )
    uid: str = Field(
        alias="uid",
        description="""The uid of the threat rule to which the group is to be attached.""",
    )
