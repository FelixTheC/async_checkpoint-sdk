from pydantic import BaseModel, Field


class PutFileRequest(BaseModel):
    targets: str | list[str] = Field(
        alias="targets",
        description="""On what targets to execute this command. Targets may be identified by their name, or object unique identifier.""",
    )
    file_content: str = Field(alias="file-content", description="""N/A""")
    file_name: str = Field(alias="file-name", description="""N/A""")
    file_path: str = Field(alias="file-path", description="""N/A""")
    comments: str = Field(alias="comments", description="""Comments string.""")
