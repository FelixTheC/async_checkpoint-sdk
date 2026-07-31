from aiohttp import ClientSession

from async_checkpoint_sdk.models.default_admin_settings_reply import DefaultAdminSettingsReply
from async_checkpoint_sdk.models.default_admin_settings_request_edit import (
    DefaultAdminSettingsRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_default_administrator_settings(
    client: ClientSession, data: DefaultAdminSettingsRequestEdit, config: SDKConfig, **kwargs
) -> DefaultAdminSettingsReply:
    """
    Set default administrator settings.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : DefaultAdminSettingsRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DefaultAdminSettingsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-default-administrator-settings"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DefaultAdminSettingsReply(**resp)
