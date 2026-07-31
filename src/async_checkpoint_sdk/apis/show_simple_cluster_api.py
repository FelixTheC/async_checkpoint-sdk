from aiohttp import ClientSession

from async_checkpoint_sdk.models.cluster_reply import ClusterReply
from async_checkpoint_sdk.models.cluster_request_show import ClusterRequestShow
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_simple_cluster(
    client: ClientSession, data: ClusterRequestShow, config: SDKConfig, **kwargs
) -> ClusterReply:
    """
    Retrieve existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ClusterRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ClusterReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-simple-cluster"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ClusterReply(**resp)
