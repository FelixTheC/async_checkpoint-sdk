from pydantic import BaseModel, Field
from where_used_report_reply import WhereUsedReportReply


class WhereUsedObjectReply(BaseModel):
    used_directly: WhereUsedReportReply = Field(
        alias="used-directly", description="""Direct usage of the object."""
    )
    used_indirectly: WhereUsedReportReply = Field(
        alias="used-indirectly", description="""Indirect usage of the object."""
    )
