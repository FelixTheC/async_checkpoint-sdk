from aiohttp import ClientSession

from async_checkpoint_sdk.models.cdm_command_reply import CdmCommandReply
from async_checkpoint_sdk.models.check_network_feed_request import CheckNetworkFeedRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def check_network_feed(
    client: ClientSession, data: CheckNetworkFeedRequest, config: SDKConfig, **kwargs
) -> CdmCommandReply:
    """
    Check if a target can reach or parse a network feed - can work with an existing feed object or with a new one (by providing all relevant feed parameters).

    Parameters
    ----------
    client : ClientSession
    data : CheckNetworkFeedRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    CdmCommandReply

    """
    url = f"https://{config.server}:{config.port}/web_api/check-network-feed"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CdmCommandReply(**resp)
