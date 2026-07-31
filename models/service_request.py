from array_node import ArrayNode
from pydantic import BaseModel, Field


class ServiceRequest(BaseModel):
    fields_to_remove: list[str] = Field(alias="fields-to-remove", description="""N/A""")
    params: ArrayNode = Field(
        alias="params",
        description="""Parameters for the command. Each param consists of nested map between full path of the class to the value (the object).""",
    )
