from aiohttp import ClientSession

from async_checkpoint_sdk.models.tcp_resource_reply import TcpResourceReply
from async_checkpoint_sdk.models.tcp_resource_request_edit import TcpResourceRequestEdit
from config import Config


async def clone_resource_tcp(
    client: ClientSession, data: TcpResourceRequestEdit, config: Config, **kwargs
) -> TcpResourceReply:
    """
    Clone existing TCP resource.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : TcpResourceRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TcpResourceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-resource-tcp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TcpResourceReply(**resp)
