from aiohttp import ClientSession

from async_checkpoint_sdk.models.https_advanced_settings_reply import HttpsAdvancedSettingsReply
from async_checkpoint_sdk.models.https_advanced_settings_request import (
    HttpsAdvancedSettingsRequest,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_https_advanced_settings(
    client: ClientSession, data: HttpsAdvancedSettingsRequest, config: SDKConfig, **kwargs
) -> HttpsAdvancedSettingsReply:
    """
    Configure advanced settings for HTTPS Inspection.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : HttpsAdvancedSettingsRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    HttpsAdvancedSettingsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-https-advanced-settings"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return HttpsAdvancedSettingsReply(**resp)
