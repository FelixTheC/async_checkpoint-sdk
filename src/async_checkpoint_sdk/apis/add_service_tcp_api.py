from aiohttp import ClientSession

from async_checkpoint_sdk.models.tcp_service_reply import TcpServiceReply
from async_checkpoint_sdk.models.tcp_service_request_new import TcpServiceRequestNew
from config import Config


async def add_service_tcp(
    client: ClientSession, data: TcpServiceRequestNew, config: Config, **kwargs
) -> TcpServiceReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : TcpServiceRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TcpServiceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-service-tcp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TcpServiceReply(**resp)
