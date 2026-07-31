from .pydantic import BaseModel, Field


class ApiServerSettingsRequestEdit(BaseModel):
    accepted_api_calls_from: str = Field(
        alias="accepted-api-calls-from",
        description="""Clients allowed to connect to the API Server.""",
    )
