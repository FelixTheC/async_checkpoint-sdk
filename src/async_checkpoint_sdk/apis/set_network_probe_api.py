from aiohttp import ClientSession

from async_checkpoint_sdk.models.network_probe_reply import NetworkProbeReply
from async_checkpoint_sdk.models.network_probe_request_edit import NetworkProbeRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_network_probe(
    client: ClientSession, data: NetworkProbeRequestEdit, config: SDKConfig, **kwargs
) -> NetworkProbeReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : NetworkProbeRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    NetworkProbeReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-network-probe"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return NetworkProbeReply(**resp)
