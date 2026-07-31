from aiohttp import ClientSession

from config import Config
from models.content_awareness_advanced_settings_reply import ContentAwarenessAdvancedSettingsReply
from models.content_awareness_advanced_settings_request_show import (
    ContentAwarenessAdvancedSettingsRequestShow,
)


async def show_content_awareness_advanced_settings(
    client: ClientSession,
    data: ContentAwarenessAdvancedSettingsRequestShow,
    config: Config,
    **kwargs,
) -> ContentAwarenessAdvancedSettingsReply:
    """
    Show Content Awareness Blades' Settings.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ContentAwarenessAdvancedSettingsRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ContentAwarenessAdvancedSettingsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-content-awareness-advanced-settings"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ContentAwarenessAdvancedSettingsReply(**resp)
