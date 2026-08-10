from aiohttp import ClientSession

from async_checkpoint_sdk.models.compound_tcp_service_reply import CompoundTcpServiceReply
from async_checkpoint_sdk.models.compound_tcp_service_request_edit import (
    CompoundTcpServiceRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_service_compound_tcp(
    client: ClientSession, data: CompoundTcpServiceRequestEdit, config: SDKConfig, **kwargs
) -> CompoundTcpServiceReply:
    """
    Clone existing object.

    Parameters
    ----------
    client : ClientSession
    data : CompoundTcpServiceRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    CompoundTcpServiceReply

    """
    url = f"https://{config.server}:{config.port}/web_api/clone-service-compound-tcp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CompoundTcpServiceReply(**resp)
