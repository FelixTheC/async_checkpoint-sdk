from pydantic import BaseModel, Field


class StateSyncronization(BaseModel):
    delayed: bool = Field(
        alias="delayed",
        description="""Start synchronizing with delay of seconds, as defined by delayed-seconds, after connection initiation. Disabled when state-synchronization disabled.""",
    )
    delayed_seconds: int = Field(
        alias="delayed-seconds",
        description="""Start synchronizing X seconds after connection initiation
. The values must be in a range between 2 and 3600.""",
    )
    enabled: bool = Field(alias="enabled", description="""Use State Synchronization.""")
