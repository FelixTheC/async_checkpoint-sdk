from .pydantic import BaseModel, Field


class ScadaApplicationEntryItem(BaseModel):
    key: str = Field(alias="key", description="""SCADA property key.""")
    value: str = Field(alias="value", description="""SCADA property value.""")
