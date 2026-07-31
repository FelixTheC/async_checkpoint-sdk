from pydantic import BaseModel, Field


class TrackSettingsReply(BaseModel):
    applications_in_rule: bool = Field(
        alias="applications-in-rule", description="""N/A"""
    )
    data_types_in_rule: bool = Field(alias="data-types-in-rule", description="""N/A""")
    default_per_connection: bool = Field(
        alias="default-per-connection", description="""N/A"""
    )
    default_per_session: bool = Field(
        alias="default-per-session", description="""N/A"""
    )
