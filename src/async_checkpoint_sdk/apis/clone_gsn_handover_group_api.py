from aiohttp import ClientSession

from async_checkpoint_sdk.models.gsn_handover_group_reply import GsnHandoverGroupReply
from async_checkpoint_sdk.models.gsn_handover_group_request_edit import GsnHandoverGroupRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_gsn_handover_group(
    client: ClientSession, data: GsnHandoverGroupRequestEdit, config: SDKConfig, **kwargs
) -> GsnHandoverGroupReply:
    """
    Clone existing object.

    Parameters
    ----------
    client : ClientSession
    data : GsnHandoverGroupRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

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
