from aiohttp import ClientSession

from async_checkpoint_sdk.models.cluster_async_reply import ClusterAsyncReply
from async_checkpoint_sdk.models.cluster_request_edit import ClusterRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_simple_cluster(
    client: ClientSession, data: ClusterRequestEdit, config: SDKConfig, **kwargs
) -> ClusterAsyncReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ClusterRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ClusterAsyncReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-simple-cluster"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ClusterAsyncReply(**resp)
