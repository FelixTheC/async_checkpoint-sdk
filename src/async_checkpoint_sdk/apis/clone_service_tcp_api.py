from aiohttp import ClientSession

from async_checkpoint_sdk.models.tcp_service_reply import TcpServiceReply
from async_checkpoint_sdk.models.tcp_service_request_edit import TcpServiceRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_service_tcp(
    client: ClientSession, data: TcpServiceRequestEdit, config: SDKConfig, **kwargs
) -> TcpServiceReply:
    """
    Clone existing object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : TcpServiceRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TcpServiceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-service-tcp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TcpServiceReply(**resp)
