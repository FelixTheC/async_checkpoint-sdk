from .pydantic import BaseModel, Field


class CustomCategorizationSettingsReply(BaseModel):
    url_filtering_mode: str = Field(
        alias="url-filtering-mode",
        description="""Hold - Requests are blocked until categorization is complete.<br>Background - Requests are allowed until categorization is complete.<br>This property is not available in the Global domain of an MDS machine.""",
    )
    social_network_widgets_mode: str = Field(
        alias="social-network-widgets-mode",
        description="""Hold - Requests are blocked until categorization is complete.<br>Background - Requests are allowed until categorization is complete.<br>This property is not available in the Global domain of an MDS machine.""",
    )
