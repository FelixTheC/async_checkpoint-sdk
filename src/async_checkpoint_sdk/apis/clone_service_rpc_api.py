from aiohttp import ClientSession

from async_checkpoint_sdk.models.rpc_service_reply import RpcServiceReply
from async_checkpoint_sdk.models.rpc_service_request_edit import RpcServiceRequestEdit
from config import Config


async def clone_service_rpc(
    client: ClientSession, data: RpcServiceRequestEdit, config: Config, **kwargs
) -> RpcServiceReply:
    """
    Clone existing object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : RpcServiceRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    RpcServiceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-service-rpc"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return RpcServiceReply(**resp)
