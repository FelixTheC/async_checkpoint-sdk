from .pydantic import BaseModel, Field


class PutFileRequest(BaseModel):
    file_content: str = Field(alias="file-content", description="""N/A""")
    file_name: str = Field(alias="file-name", description="""N/A""")
    file_path: str = Field(alias="file-path", description="""N/A""")
    comments: str = Field(alias="comments", description="""Comments string.""")
