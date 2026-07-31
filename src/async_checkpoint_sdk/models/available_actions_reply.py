from pydantic import BaseModel, Field


class AvailableActionsReply(BaseModel):
    clone: str = Field(alias="clone", description="""Whether you can clone the object.""")
    delete: str = Field(alias="delete", description="""Whether you can delete the object.""")
    edit: str = Field(alias="edit", description="""Whether you can edit the object.""")
