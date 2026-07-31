from aiohttp import ClientSession

from config import Config
from models.gateway_ckp_reply import GatewayCkpReply
from models.gateway_ckp_request_edit import GatewayCkpRequestEdit


async def set_simple_gateway(
    client: ClientSession, data: GatewayCkpRequestEdit, config: Config, **kwargs
) -> GatewayCkpReply:
    """
    Edit existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : GatewayCkpRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    GatewayCkpReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-simple-gateway"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GatewayCkpReply(**resp)
