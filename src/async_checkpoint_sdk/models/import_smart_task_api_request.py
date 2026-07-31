from pydantic import BaseModel, Field


class ImportSmartTaskApiRequest(BaseModel):
    file_path: str = Field(
        alias="file-path",
        description="""Path to the SmartTask file to be imported. <br>Should be the full file path (example, /home/admin/exported-smart-task.txt).""",
    )
