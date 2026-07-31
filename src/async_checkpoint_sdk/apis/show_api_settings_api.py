from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_server_settings_reply import ApiServerSettingsReply
from async_checkpoint_sdk.models.api_server_settings_request_show import (
    ApiServerSettingsRequestShow,
)
from config import Config


async def show_api_settings(
    client: ClientSession, data: ApiServerSettingsRequestShow, config: Config, **kwargs
) -> ApiServerSettingsReply:
    """
    Retrieve existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiServerSettingsRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiServerSettingsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-api-settings"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiServerSettingsReply(**resp)
