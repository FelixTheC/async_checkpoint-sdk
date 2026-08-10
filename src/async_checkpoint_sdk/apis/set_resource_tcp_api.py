from aiohttp import ClientSession

from async_checkpoint_sdk.models.tcp_resource_reply import TcpResourceReply
from async_checkpoint_sdk.models.tcp_resource_request_edit import TcpResourceRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_resource_tcp(
    client: ClientSession, data: TcpResourceRequestEdit, config: SDKConfig, **kwargs
) -> TcpResourceReply:
    """
    Edit existing TCP resource using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : TcpResourceRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    TcpResourceReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-resource-tcp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TcpResourceReply(**resp)
