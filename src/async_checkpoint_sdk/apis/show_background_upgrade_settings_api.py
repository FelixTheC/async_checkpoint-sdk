from aiohttp import ClientSession

from async_checkpoint_sdk.models.background_upgrade_settings_reply import (
    BackgroundUpgradeSettingsReply,
)
from async_checkpoint_sdk.models.background_upgrade_settings_show import (
    BackgroundUpgradeSettingsShow,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_background_upgrade_settings(
    client: ClientSession, data: BackgroundUpgradeSettingsShow, config: SDKConfig, **kwargs
) -> BackgroundUpgradeSettingsReply:
    """
    Show background upgrade settings.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : BackgroundUpgradeSettingsShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    BackgroundUpgradeSettingsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-background-upgrade-settings"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return BackgroundUpgradeSettingsReply(**resp)
