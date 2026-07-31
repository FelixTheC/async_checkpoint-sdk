from aiohttp import ClientSession

from async_checkpoint_sdk.models.citrix_tcp_service_reply import CitrixTcpServiceReply
from async_checkpoint_sdk.models.citrix_tcp_service_request_edit import CitrixTcpServiceRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_service_citrix_tcp(
    client: ClientSession, data: CitrixTcpServiceRequestEdit, config: SDKConfig, **kwargs
) -> CitrixTcpServiceReply:
    """
    Clone existing object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : CitrixTcpServiceRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CitrixTcpServiceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-service-citrix-tcp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CitrixTcpServiceReply(**resp)
