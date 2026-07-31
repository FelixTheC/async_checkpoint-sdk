from aiohttp import ClientSession

from async_checkpoint_sdk.models.appi_advanced_settings_reply import AppiAdvancedSettingsReply
from async_checkpoint_sdk.models.appi_advanced_settings_request_edit import (
    AppiAdvancedSettingsRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_app_control_advanced_settings(
    client: ClientSession, data: AppiAdvancedSettingsRequestEdit, config: SDKConfig, **kwargs
) -> AppiAdvancedSettingsReply:
    """
    Edit Application Control & URL Filtering Blades' Settings.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : AppiAdvancedSettingsRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AppiAdvancedSettingsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-app-control-advanced-settings"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AppiAdvancedSettingsReply(**resp)
