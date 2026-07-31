from api_date_reply import ApiDateReply
from api_domain_identifier import ApiDomainIdentifier
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class DefaultAdminSettingsReply(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    authentication_method: str = Field(
        alias="authentication-method",
        description="""Authentication method for new administrator.""",
    )
    expiration_type: str = Field(
        alias="expiration-type", description="""Expiration type for new administrator."""
    )
    expiration_date: ApiDateReply = Field(
        alias="expiration-date",
        description="""Expiration date for new administrator. <br> <font color=red>Required only when</font> 'expiration-type' is set to 'expiration date'.""",
    )
    expiration_period: int = Field(
        alias="expiration-period",
        description="""Expiration period for new administrator. <br> <font color=red>Required only when</font> 'expiration-type' is set to 'expiration period'.""",
    )
    expiration_period_time_units: str = Field(
        alias="expiration-period-time-units",
        description="""Expiration period time units for new administrator. <br> <font color=red>Required only when</font> 'expiration-type' is set to 'expiration period'.""",
    )
    indicate_expiration_in_admin_view: bool = Field(
        alias="indicate-expiration-in-admin-view",
        description="""Indicates whether to notify administrator about expiration.""",
    )
    notify_expiration_to_admin: bool = Field(
        alias="notify-expiration-to-admin",
        description="""Indicates whether to show 'about to expire' indication in administrator view.""",
    )
    days_to_indicate_expiration_in_admin_view: int = Field(
        alias="days-to-indicate-expiration-in-admin-view",
        description="""Number of days in advanced to show 'about to expire' indication in administrator view.""",
    )
    days_to_notify_expiration_to_admin: int = Field(
        alias="days-to-notify-expiration-to-admin",
        description="""Number of days in advanced to notify administrator about expiration.""",
    )
    domain: ApiDomainIdentifier = Field(
        alias="domain", description="""Information about the domain that holds the Object."""
    )
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
