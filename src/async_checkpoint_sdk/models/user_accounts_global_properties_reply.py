from .api_date_reply import ApiDateReply
from .pydantic import BaseModel, Field


class UserAccountsGlobalPropertiesReply(BaseModel):
    expiration_date_method: str = Field(
        alias="expiration-date-method",
        description="""Select an Expiration Date Method.<br>Expire at - Account expires on the date that you select.<br>Expire after - Account expires after the number of days that you select.""",
    )
    expiration_date: ApiDateReply = Field(
        alias="expiration-date", description="""Expiration Date."""
    )
    days_until_expiration: int = Field(
        alias="days-until-expiration",
        description="""Account expires after the number of days that you select.""",
    )
    show_accounts_expiration_indication_days_in_advance: bool = Field(
        alias="show-accounts-expiration-indication-days-in-advance",
        description="""Activates the Expired Accounts link, to open the Expired Accounts window.""",
    )
    days_in_advance_to_show_accounts_expiration_indication: int = Field(
        alias="days-in-advance-to-show-accounts-expiration-indication",
        description="""Days in advance to show accounts expiration indication.""",
    )
