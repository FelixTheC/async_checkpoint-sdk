from .license_info_reply import LicenseInfoReply
from .pydantic import BaseModel, Field


class CentralLicensesReply(BaseModel):
    central: bool = Field(
        alias="central",
        description="""Indicates whether the license is central or local.""",
    )
    ck: str = Field(
        alias="ck",
        description="""A unique identifier which represent a specific license.""",
    )
    expiration: str = Field(alias="expiration", description="""The license expiration date.""")
    ip_address: str = Field(alias="ip-address", description="""The license IP address.""")
    signature: str = Field(alias="signature", description="""The license signature.""")
    sku: str = Field(
        alias="sku",
        description="""An several alpha-numeric strings separated by a dash used to define the functionality of a specific license.""",
    )
    additional_info: LicenseInfoReply = Field(
        alias="additional-info",
        description="""Additional info for cloud licenses (ve licenses).""",
    )
