from date_reply import DateReply
from pydantic import BaseModel, Field


class RemoteDataCenterObjectMetaData(BaseModel):
    updated_on_data_center: DateReply = Field(
        alias="updated-on-data-center", description="""Last update time in the Data Center."""
    )
