from pydantic import BaseModel, Field


class DefaultAdminSettingsRequestEdit(BaseModel):
    authentication_method: str = Field(
        alias="authentication-method",
        description="""Authentication method for new administrator.""",
    )
    expiration_type: str = Field(
        alias="expiration-type", description="""Expiration type for new administrator."""
    )
    expiration_date: str = Field(
        alias="expiration-date",
        description="""Expiration date for new administrator in YYYY-MM-DD format. <font color=red>Required only when</font> 'expiration-type' is set to 'expiration date'.""",
    )
    expiration_period: int = Field(
        alias="expiration-period",
        description="""Expiration period for new administrator. <font color=red>Required only when</font> 'expiration-type' is set to 'expiration period'.""",
    )
    expiration_period_time_units: str = Field(
        alias="expiration-period-time-units",
        description="""Expiration period time units for new administrator. <font color=red>Required only when</font> 'expiration-type' is set to 'expiration period'.""",
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
