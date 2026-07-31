from .object import Object
from .pydantic import BaseModel, Field


class CmeApiCmdReply(BaseModel):
    error: Object = Field(
        alias="error",
        description="""The error object of a failed call response from .the CME API in json format.""",
    )
    result: Object = Field(
        alias="result",
        description="""The result object of a successful call response from .the CME API in json format.""",
    )
    status_code: int = Field(
        alias="status-code",
        description="""HTTP status code  of a response from .the CME API.""",
    )
