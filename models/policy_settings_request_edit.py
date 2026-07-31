from pydantic import BaseModel, Field
from security_access_defaults_request_edit import SecurityAccessDefaultsRequestEdit


class PolicySettingsRequestEdit(BaseModel):
    last_in_cell: str = Field(
        alias="last-in-cell",
        description="""Added object after removing the last object in cell.""",
    )
    log_generation: str = Field(
        alias="log-generation",
        description="""Log generation settings for existing and new rules.""",
    )
    none_object_behavior: str = Field(
        alias="none-object-behavior",
        description="""'None' object behavior. Rules with object 'None' will never be matched.""",
    )
    security_access_defaults: SecurityAccessDefaultsRequestEdit = Field(
        alias="security-access-defaults",
        description="""Access Policy default values.""",
    )
