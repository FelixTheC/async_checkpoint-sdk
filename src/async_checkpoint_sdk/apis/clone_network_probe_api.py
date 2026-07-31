from aiohttp import ClientSession

from async_checkpoint_sdk.models.network_probe_reply import NetworkProbeReply
from async_checkpoint_sdk.models.network_probe_request_edit import NetworkProbeRequestEdit
from config import Config


async def clone_network_probe(
    client: ClientSession, data: NetworkProbeRequestEdit, config: Config, **kwargs
) -> NetworkProbeReply:
    """
    Clone existing object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : NetworkProbeRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    NetworkProbeReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-network-probe"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return NetworkProbeReply(**resp)
