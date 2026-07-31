from other_range_reply import OtherRangeReply
from pydantic import BaseModel, Field


class RaTechReply(BaseModel):
    utran: bool = Field(alias="utran", description="""(1).""")
    geran: bool = Field(alias="geran", description="""(2).""")
    wlan: bool = Field(alias="wlan", description="""(3).""")
    gan: bool = Field(alias="gan", description="""(4).""")
    hspa_evolution: bool = Field(alias="hspa-evolution", description="""(5).""")
    eutran: bool = Field(alias="eutran", description="""(6).""")
    virtual: bool = Field(alias="virtual", description="""(7).""")
    nb_iot: bool = Field(alias="nb-iot", description="""(8).""")
    other_types_range: OtherRangeReply = Field(
        alias="other-types-range", description="""(9-255)."""
    )
