from .date_reply import DateReply
from .pydantic import BaseModel, Field


class RemoteUpdatableObjectMetaData(BaseModel):
    updated_on_updatable_objects_repository: DateReply = Field(
        alias="updated-on-updatable-objects-repository",
        description="""Last update time from .the Updatable Objects Repository.""",
    )
