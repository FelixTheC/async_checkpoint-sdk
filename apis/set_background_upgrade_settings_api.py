from config import Config
from aiohttp import ClientSession
from models.background_upgrade_settings_reply import BackgroundUpgradeSettingsReply
from models.background_upgrade_settings_request_edit import BackgroundUpgradeSettingsRequestEdit


async def set_background_upgrade_settings(
    client: ClientSession, data: BackgroundUpgradeSettingsRequestEdit, config: Config, **kwargs
) -> BackgroundUpgradeSettingsReply:
    """
    Set background upgrade settings.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : BackgroundUpgradeSettingsRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    BackgroundUpgradeSettingsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-background-upgrade-settings"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return BackgroundUpgradeSettingsReply(**resp)
