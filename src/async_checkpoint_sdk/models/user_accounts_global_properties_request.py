from pydantic import BaseModel, Field


class UserAccountsGlobalPropertiesRequest(BaseModel):
    expiration_date_method: str = Field(
        alias="expiration-date-method",
        description="""Select an Expiration Date Method.<br>Expire at - Account expires on the date that you select.<br>Expire after - Account expires after the number of days that you select.""",
    )
    expiration_date: str = Field(
        alias="expiration-date",
        description="""Specify an Expiration Date in the following format: YYYY-MM-DD.<br>Available only if expiration-date-method is set to expire at.""",
    )
    days_until_expiration: int = Field(
        alias="days-until-expiration",
        description="""Account expires after the number of days that you select.<br>Available only if expiration-date-method is set to expire after.""",
    )
    show_accounts_expiration_indication_days_in_advance: bool = Field(
        alias="show-accounts-expiration-indication-days-in-advance",
        description="""Activates the Expired Accounts link, to open the Expired Accounts window.""",
    )
