from pydantic import BaseModel, Field


class CustomSettingsReply(BaseModel):
    anti_bot: str = Field(alias="anti-bot", description="""Custom Settings for Anti Bot Blade.""")
    anti_virus: str = Field(
        alias="anti-virus", description="""Custom Settings for Anti Virus Blade."""
    )
    zero_phishing: str = Field(
        alias="zero-phishing", description="""Custom Settings for Zero Phishing Blade."""
    )
