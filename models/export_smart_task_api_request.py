from pydantic import BaseModel, Field


class ExportSmartTaskApiRequest(BaseModel):
    file_path: str = Field(
        alias="file-path",
        description="""Path to the SmartTask file to be exported. <br>Should be the full file path (example, /home/admin/exported-smart-task.txt).<br>If no path was inserted the default will be: /var/log/<task_name>.txt.""",
    )
