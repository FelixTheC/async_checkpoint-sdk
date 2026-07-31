from config import Config
from aiohttp import ClientSession
from models.large_scale_vpn_reply import LargeScaleVpnReply
from models.large_scale_vpn_request_edit import LargeScaleVpnRequestEdit


async def set_lsv_profile(
    client: ClientSession, data: LargeScaleVpnRequestEdit, config: Config, **kwargs
) -> LargeScaleVpnReply:
    """
    Set LSV Profile object's fields. Set CA by uid or name, change peers limit or restrict encryption domain.
    
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
    url = f"https://{config.server}:{config.port}/web_api/set-lsv-profile"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LargeScaleVpnReply(**resp)
