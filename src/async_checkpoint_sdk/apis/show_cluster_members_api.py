from aiohttp import ClientSession

from async_checkpoint_sdk.models.cluster_member_query_reply import ClusterMemberQueryReply
from async_checkpoint_sdk.models.object_in_group_query_request import ObjectInGroupQueryRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_cluster_members(
    client: ClientSession, data: ObjectInGroupQueryRequest, config: SDKConfig, **kwargs
) -> ClusterMemberQueryReply:
    """
    Retrieve all existing cluster members in domain.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ObjectInGroupQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ClusterMemberQueryReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-cluster-members"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ClusterMemberQueryReply(**resp)
