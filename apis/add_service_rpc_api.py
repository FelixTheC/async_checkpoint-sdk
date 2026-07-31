from config import Config
from aiohttp import ClientSession
from models.rpc_service_request_new import RpcServiceRequestNew
from models.rpc_service_reply import RpcServiceReply


async def add_service_rpc(
    client: ClientSession, data: RpcServiceRequestNew, config: Config, **kwargs
) -> RpcServiceReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : RpcServiceRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    RpcServiceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-service-rpc"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return RpcServiceReply(**resp)
