from aiohttp import ClientSession

from async_checkpoint_sdk.models.cluster_async_reply import ClusterAsyncReply
from async_checkpoint_sdk.models.cluster_request_new import ClusterRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_simple_cluster(
    client: ClientSession, data: ClusterRequestNew, config: SDKConfig, **kwargs
) -> ClusterAsyncReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ClusterRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ClusterAsyncReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-simple-cluster"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ClusterAsyncReply(**resp)
