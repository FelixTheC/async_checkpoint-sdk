from pydantic import BaseModel, Field
from trust_settings_request import TrustSettingsRequest


class SetTrustRequest(BaseModel):
    ipv4_address: str = Field(
        alias="ipv4-address",
        description="""IP address of the object, for establishing trust with dynamic gateways.""",
    )
    one_time_password: str = Field(
        alias="one-time-password",
        description="""Shared password to establish SIC between the Security Management and the Security Gateway.""",
    )
    trust_method: str = Field(
        alias="trust-method",
        description="""Establish the trust communication method.""",
    )
    trust_settings: TrustSettingsRequest = Field(
        alias="trust-settings",
        description="""Settings for the trusted communication establishment.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
    )
