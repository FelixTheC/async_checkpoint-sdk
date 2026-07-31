from pydantic import BaseModel, Field


class HitCountGlobalPropertiesRequest(BaseModel):
    enable_hit_count: bool = Field(
        alias="enable-hit-count",
        description="""Select to enable or clear to disable all Security Gateways to monitor the number of connections each rule matches.""",
    )
    keep_hit_count_data_up_to: str = Field(
        alias="keep-hit-count-data-up-to",
        description="""Select one of the time range options. Data is kept in the Security Management Server database for this period and is shown in the Hits column.""",
    )
