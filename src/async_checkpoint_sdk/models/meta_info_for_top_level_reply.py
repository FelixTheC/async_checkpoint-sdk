from api_date_reply import ApiDateReply
from pydantic import BaseModel, Field


class MetaInfoForTopLevelReply(BaseModel):
    creation_time: ApiDateReply = Field(alias="creation-time", description="""N/A""")
    creator: str = Field(alias="creator", description="""N/A""")
    last_modifier: str = Field(alias="last-modifier", description="""N/A""")
    last_modify_time: ApiDateReply = Field(alias="last-modify-time", description="""N/A""")
    lock: str = Field(
        alias="lock",
        description="""Object lock state. It's not allowed to edit objects locked by other session.""",
    )
    locking_admin: str = Field(
        alias="locking-admin",
        description="""in case the object is locked by another session it will show the administrator name that locked the object.""",
    )
    locking_session_id: str = Field(
        alias="locking-session-id",
        description="""in case the object is locked by another session it will show the session uid that locked the object.""",
    )
    validation_state: str = Field(alias="validation-state", description="""N/A""")
