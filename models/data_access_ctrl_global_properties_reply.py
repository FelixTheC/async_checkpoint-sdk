from pydantic import BaseModel, Field


class DataAccessCtrlGlobalPropertiesReply(BaseModel):
    auto_download_important_data: bool = Field(
        alias="auto-download-important-data",
        description="""Automatically download and install Software Blade Contracts, security updates and other important data (highly recommended).""",
    )
    auto_download_sw_updates_and_new_features: bool = Field(
        alias="auto-download-sw-updates-and-new-features",
        description="""Automatically download software updates and new features (highly recommended).<br>Available only if auto-download-important-data is set to true.""",
    )
    send_anonymous_info: bool = Field(
        alias="send-anonymous-info",
        description="""Help Check Point improve the product by sending anonymous information.""",
    )
    share_sensitive_info: bool = Field(
        alias="share-sensitive-info",
        description="""Approve sharing core dump files and other relevant crash data which might contain personal information. All shared data will be processed in accordance with Check Point's Privacy Policy.<br>Available only if send-anonymous-info is set to true.""",
    )
