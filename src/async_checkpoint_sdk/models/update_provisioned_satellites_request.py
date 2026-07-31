from pydantic import BaseModel, Field


class UpdateProvisionedSatellitesRequest(BaseModel):
    vpn_center_gateways: str | list[str] = Field(
        alias="vpn-center-gateways",
        description="""On what targets to execute this command. Targets may be identified by their name, or object unique identifier. The targets should be a corporate gateways.""",
    )
