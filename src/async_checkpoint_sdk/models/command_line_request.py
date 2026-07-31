from pydantic import BaseModel, Field


class CommandLineRequest(BaseModel):
    command: str = Field(alias="command", description="""N/A""")
