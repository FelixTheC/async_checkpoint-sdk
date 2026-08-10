from aiohttp import ClientSession

from async_checkpoint_sdk.models.global_properties_reply import GlobalPropertiesReply
from async_checkpoint_sdk.models.global_properties_request_show import GlobalPropertiesRequestShow
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_global_properties(
    client: ClientSession, data: GlobalPropertiesRequestShow, config: SDKConfig, **kwargs
) -> GlobalPropertiesReply:
    """
    Retrieve existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : GlobalPropertiesRequestShow
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    GlobalPropertiesReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-global-properties"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GlobalPropertiesReply(**resp)
