from .cpuuid import CPUUID
from .pydantic import BaseModel, Field


class TrackSettingsRequest(BaseModel):
    layer_uid: CPUUID = Field(alias="layer-uid", description="""N/A""")
    rule_uid: CPUUID = Field(alias="rule-uid", description="""N/A""")
