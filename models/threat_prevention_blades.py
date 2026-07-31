from pydantic import BaseModel, Field


class ThreatPreventionBlades(BaseModel):
    autonomous: list[dict] = Field(alias="autonomous", description="""N/A""")
    custom: list[dict] = Field(alias="custom", description="""N/A""")
