from aiohttp import ClientSession

from async_checkpoint_sdk.models.lsm_cluster_reply import LsmClusterReply
from async_checkpoint_sdk.models.lsm_gateway_cluster_common_request_show import (
    LsmGatewayClusterCommonRequestShow,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_lsm_cluster(
    client: ClientSession, data: LsmGatewayClusterCommonRequestShow, config: SDKConfig, **kwargs
) -> LsmClusterReply:
    """
    Show LSM Cluster.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : LsmGatewayClusterCommonRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LsmClusterReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-lsm-cluster"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LsmClusterReply(**resp)
