from pydantic import BaseModel, Field


class AddPackageCommandRequest(BaseModel):
    name: str = Field(alias="name", description="""The name of the repository package.""")
    path: str = Field(
        alias="path",
        description="""The path of the repository package.<br><font color=red>Required only for</font> adding package from local.""",
    )
    source: str = Field(alias="source", description="""The source of the repository package.""")
