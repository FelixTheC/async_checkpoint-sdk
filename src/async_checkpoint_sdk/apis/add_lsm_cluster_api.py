from aiohttp import ClientSession

from async_checkpoint_sdk.models.lsm_cluster_reply import LsmClusterReply
from async_checkpoint_sdk.models.lsm_cluster_request_new import LsmClusterRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_lsm_cluster(
    client: ClientSession, data: LsmClusterRequestNew, config: SDKConfig, **kwargs
) -> LsmClusterReply:
    """
    Add LSM Cluster.

    Parameters
    ----------
    client : ClientSession
    data : LsmClusterRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    LsmClusterReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-lsm-cluster"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LsmClusterReply(**resp)
