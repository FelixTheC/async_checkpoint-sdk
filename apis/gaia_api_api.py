from aiohttp import ClientSession

from config import Config
from models.gw_proxy_cmd_reply import GwProxyCmdReply
from models.gw_proxy_cmd_request import GwProxyCmdRequest


async def gaia_api(
    client: ClientSession, data: GwProxyCmdRequest, config: Config, **kwargs
) -> GwProxyCmdReply:
    """
    Runs a gaia-api command from the management.
    Syntax: gaia-api/gateway-command. Gateway-command is the gaia-api command which you want to send the request. Please take a look at the examples to know how to use it. Please include any input parameters needed in the request body.
     The cache config file in $FWDIR/api/conf/cache.conf can be used to change the settings.
    NOTE: Please add a rule to allow the connection from the management to the targets.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : GwProxyCmdRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    GwProxyCmdReply
    """
    url = f"https://{config.server}:{config.port}/web_api/gaia-api"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GwProxyCmdReply(**resp)
