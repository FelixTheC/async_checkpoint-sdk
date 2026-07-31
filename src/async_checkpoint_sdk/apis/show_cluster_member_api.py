from aiohttp import ClientSession

from async_checkpoint_sdk.models.cluster_member_reply_ex import ClusterMemberReplyEx
from async_checkpoint_sdk.models.cluster_member_show_request import ClusterMemberShowRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_cluster_member(
    client: ClientSession, data: ClusterMemberShowRequest, config: SDKConfig, **kwargs
) -> ClusterMemberReplyEx:
    """
    Retrieve existing cluster member using uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ClusterMemberShowRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ClusterMemberReplyEx
    """
    url = f"https://{config.server}:{config.port}/web_api/show-cluster-member"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ClusterMemberReplyEx(**resp)
