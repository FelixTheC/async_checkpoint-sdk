from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_server_settings_reply import ApiServerSettingsReply
from async_checkpoint_sdk.models.api_server_settings_request_edit import (
    ApiServerSettingsRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_api_settings(
    client: ClientSession, data: ApiServerSettingsRequestEdit, config: SDKConfig, **kwargs
) -> ApiServerSettingsReply:
    """
    Edit API settings, the changes will be applied after publish followed by running 'api restart' command.

    Parameters
    ----------
    client : ClientSession
    data : ApiServerSettingsRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ApiServerSettingsReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-api-settings"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiServerSettingsReply(**resp)
