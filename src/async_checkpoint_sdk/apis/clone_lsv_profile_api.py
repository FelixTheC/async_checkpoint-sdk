from aiohttp import ClientSession

from async_checkpoint_sdk.models.large_scale_vpn_reply import LargeScaleVpnReply
from async_checkpoint_sdk.models.large_scale_vpn_request_edit import LargeScaleVpnRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_lsv_profile(
    client: ClientSession, data: LargeScaleVpnRequestEdit, config: SDKConfig, **kwargs
) -> LargeScaleVpnReply:
    """
    Clone existing object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : LargeScaleVpnRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LargeScaleVpnReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-lsv-profile"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LargeScaleVpnReply(**resp)
