from aiohttp import ClientSession

from async_checkpoint_sdk.models.network_probe_reply import NetworkProbeReply
from async_checkpoint_sdk.models.network_probe_request_new import NetworkProbeRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_network_probe(
    client: ClientSession, data: NetworkProbeRequestNew, config: SDKConfig, **kwargs
) -> NetworkProbeReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : NetworkProbeRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    NetworkProbeReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-network-probe"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return NetworkProbeReply(**resp)
