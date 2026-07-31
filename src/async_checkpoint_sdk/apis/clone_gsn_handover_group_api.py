from aiohttp import ClientSession

from async_checkpoint_sdk.models.gsn_handover_group_reply import GsnHandoverGroupReply
from async_checkpoint_sdk.models.gsn_handover_group_request_edit import GsnHandoverGroupRequestEdit
from config import Config


async def clone_gsn_handover_group(
    client: ClientSession, data: GsnHandoverGroupRequestEdit, config: Config, **kwargs
) -> GsnHandoverGroupReply:
    """
    Clone existing object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : GsnHandoverGroupRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    GsnHandoverGroupReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-gsn-handover-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GsnHandoverGroupReply(**resp)
