from pydantic import BaseModel, Field


class PackageInfoCommandRequest(BaseModel):
    name: str = Field(alias="name", description="""The name of the software package.""")
