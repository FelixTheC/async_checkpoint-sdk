from api_object_standard_identifier import ApiObjectStandardIdentifier
from pydantic import BaseModel, Field


class ExportSmartTaskReply(BaseModel):
    file_path: ApiObjectStandardIdentifier = Field(
        alias="file-path",
        description="""Full path of out file that contains the exported task object.""",
    )
