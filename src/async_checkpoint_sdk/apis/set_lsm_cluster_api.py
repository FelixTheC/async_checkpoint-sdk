from aiohttp import ClientSession

from async_checkpoint_sdk.models.lsm_cluster_reply import LsmClusterReply
from async_checkpoint_sdk.models.lsm_cluster_request_edit import LsmClusterRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_lsm_cluster(
    client: ClientSession, data: LsmClusterRequestEdit, config: SDKConfig, **kwargs
) -> LsmClusterReply:
    """
    Edit existing LSM Cluster.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : LsmClusterRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LsmClusterReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-lsm-cluster"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LsmClusterReply(**resp)
