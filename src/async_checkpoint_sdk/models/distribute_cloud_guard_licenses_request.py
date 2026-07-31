from .pydantic import BaseModel, Field


class DistributeCloudGuardLicensesRequest(BaseModel):
    targets: str | list[str] = Field(
        alias="targets",
        description="""Targets are uid or name of the security gateway(s). In case no target specified, the license will be distributed to all CloudGuard security gateways.""",
    )
