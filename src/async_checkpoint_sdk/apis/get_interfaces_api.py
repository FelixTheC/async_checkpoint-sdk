from aiohttp import ClientSession

from async_checkpoint_sdk.models.get_interfaces_async_reply import GetInterfacesAsyncReply
from async_checkpoint_sdk.models.get_interfaces_request import GetInterfacesRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def get_interfaces(
    client: ClientSession, data: GetInterfacesRequest, config: SDKConfig, **kwargs
) -> GetInterfacesAsyncReply:
    """
        Get physical interfaces with or without their topology from a Gaia Security Gateway or Cluster.
    Note: The fetched topology is based on static routes.
    Prerequisites:
    1) SIC must be established in the Security Gateway or Cluster Member object.
    2) Security Gateway or Cluster Members must be up and running.

    Parameters
    ----------
    client : ClientSession
    data : GetInterfacesRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    GetInterfacesAsyncReply

    """
    url = f"https://{config.server}:{config.port}/web_api/get-interfaces"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GetInterfacesAsyncReply(**resp)
