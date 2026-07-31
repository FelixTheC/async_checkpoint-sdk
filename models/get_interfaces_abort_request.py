from pydantic import BaseModel, Field


class GetInterfacesAbortRequest(BaseModel):
    force_cleanup: bool = Field(
        alias="force-cleanup",
        description="""Forcefully abort the get-interfaces task.""",
    )
