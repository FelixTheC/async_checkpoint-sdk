from pydantic import BaseModel, Field


class CkReply(BaseModel):
    ck: str = Field(alias="ck", description="""N/A""")
