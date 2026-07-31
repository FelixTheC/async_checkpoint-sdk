from pydantic import BaseModel, Field


class LogExporterDataManipulationReply(BaseModel):
    aggregate_log_updates: bool = Field(
        alias="aggregate-log-updates", description="""Indicates whether to aggregate log updates."""
    )
    format: str = Field(alias="format", description="""Logs format.""")
