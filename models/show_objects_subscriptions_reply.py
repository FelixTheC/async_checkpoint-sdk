from pydantic import BaseModel, Field


class ShowObjectsSubscriptionsReply(BaseModel):
    subscriptions: list[str] = Field(alias="subscriptions", description="""N/A""")
