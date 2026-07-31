from pydantic import BaseModel, Field


class TurnOnOffCentralLicensesRequest(BaseModel):
    targets: str | list[str] = Field(
        alias="targets",
        description="""On what targets to execute this command. Targets may be identified by their name, or object unique identifier.""",
    )
    state: str = Field(alias="state", description="""N/A""")
