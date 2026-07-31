from aiohttp import ClientSession

from async_checkpoint_sdk.models.gsn_handover_group_reply import GsnHandoverGroupReply
from async_checkpoint_sdk.models.gsn_handover_group_request_new import GsnHandoverGroupRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_gsn_handover_group(
    client: ClientSession, data: GsnHandoverGroupRequestNew, config: SDKConfig, **kwargs
) -> GsnHandoverGroupReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : GsnHandoverGroupRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    GsnHandoverGroupReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-gsn-handover-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GsnHandoverGroupReply(**resp)
