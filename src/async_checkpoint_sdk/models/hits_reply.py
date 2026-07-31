from .api_date_reply import ApiDateReply
from .pydantic import BaseModel, Field


class HitsReply(BaseModel):
    first_date: ApiDateReply = Field(alias="first-date", description="""N/A""")
    last_date: ApiDateReply = Field(alias="last-date", description="""N/A""")
    level: str = Field(alias="level", description="""N/A""")
    percentage: str = Field(alias="percentage", description="""N/A""")
    value: int = Field(alias="value", description="""N/A""")
