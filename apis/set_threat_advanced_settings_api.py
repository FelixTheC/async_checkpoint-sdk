from aiohttp import ClientSession

from config import Config
from models.threat_advanced_settings_reply import ThreatAdvancedSettingsReply
from models.threat_advanced_settings_request_edit import ThreatAdvancedSettingsRequestEdit


async def set_threat_advanced_settings(
    client: ClientSession, data: ThreatAdvancedSettingsRequestEdit, config: Config, **kwargs
) -> ThreatAdvancedSettingsReply:
    """
    Edit Threat Prevention's Blades' Settings.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ThreatAdvancedSettingsRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ThreatAdvancedSettingsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-threat-advanced-settings"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ThreatAdvancedSettingsReply(**resp)
