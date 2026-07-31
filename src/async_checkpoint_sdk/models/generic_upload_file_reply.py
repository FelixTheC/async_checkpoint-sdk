from .pydantic import BaseModel, Field


class GenericUploadFileReply(BaseModel):
    full_file_path: str = Field(alias="full-file-path", description="""N/A""")
