from config import Config
from aiohttp import ClientSession
from models.appi_advanced_settings_reply import AppiAdvancedSettingsReply
from models.appi_advanced_settings_request_show import AppiAdvancedSettingsRequestShow


async def show_app_control_advanced_settings(
    client: ClientSession, data: AppiAdvancedSettingsRequestShow, config: Config, **kwargs
) -> AppiAdvancedSettingsReply:
    """
    Show Application Control & URL Filtering Blades' Settings.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : AppiAdvancedSettingsRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AppiAdvancedSettingsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-app-control-advanced-settings"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AppiAdvancedSettingsReply(**resp)
