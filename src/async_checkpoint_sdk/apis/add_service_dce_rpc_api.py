from aiohttp import ClientSession

from async_checkpoint_sdk.models.dcerpc_service_reply import DcerpcServiceReply
from async_checkpoint_sdk.models.dcerpc_service_request_new import DcerpcServiceRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_service_dce_rpc(
    client: ClientSession, data: DcerpcServiceRequestNew, config: SDKConfig, **kwargs
) -> DcerpcServiceReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : DcerpcServiceRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DcerpcServiceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-service-dce-rpc"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DcerpcServiceReply(**resp)
