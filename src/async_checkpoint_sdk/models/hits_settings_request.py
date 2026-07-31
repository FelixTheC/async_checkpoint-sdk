from .pydantic import BaseModel, Field


class HitsSettingsRequest(BaseModel):
    from_date: str = Field(
        alias="from-date", description="""Format: YYYY-MM-DD, YYYY-mm-ddThh:mm:ss."""
    )
    target: str = Field(alias="target", description="""Target gateway name or UID.""")
    to_date: str = Field(
        alias="to-date", description="""Format: YYYY-MM-DD, YYYY-mm-ddThh:mm:ss."""
    )
