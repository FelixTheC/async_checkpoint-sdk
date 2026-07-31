from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_ok_reply import ApiOkReply
from async_checkpoint_sdk.models.get_interfaces_request import GetInterfacesRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def get_interfaces_sync(
    client: ClientSession, data: GetInterfacesRequest, config: SDKConfig, **kwargs
) -> ApiOkReply:
    """
    Parameters
    ----------
    client : ClientSession [Argument]
    data : GetInterfacesRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/get-interfaces-sync"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
