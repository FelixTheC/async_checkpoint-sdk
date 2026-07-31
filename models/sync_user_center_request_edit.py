from pydantic import BaseModel, Field


class SyncUserCenterRequestEdit(BaseModel):
    enabled: bool = Field(
        alias="enabled",
        description="""Synchronize information once a day.<br>Warning: Synchronizing with the Check Point UserCenter requires a valid licence.""",
    )
