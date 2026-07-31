from aiohttp import ClientSession

from async_checkpoint_sdk.models.cdm_command_reply import CdmCommandReply
from async_checkpoint_sdk.models.check_intelligence_feed_request import (
    CheckIntelligenceFeedRequest,
)
from config import Config


async def check_threat_ioc_feed(
    client: ClientSession, data: CheckIntelligenceFeedRequest, config: Config, **kwargs
) -> CdmCommandReply:
    """
    Check if a target can reach or parse a threat IOC feed - can work with an existing feed object or with a new one (by providing all relevant feed parameters.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : CheckIntelligenceFeedRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CdmCommandReply
    """
    url = f"https://{config.server}:{config.port}/web_api/check-threat-ioc-feed"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CdmCommandReply(**resp)
