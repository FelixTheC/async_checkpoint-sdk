from pydantic import BaseModel, Field


class DeletePackageCommandRequest(BaseModel):
    name: str = Field(alias="name", description="""The name of the software package.""")
