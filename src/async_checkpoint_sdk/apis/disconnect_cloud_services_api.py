from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_message_reply import ApiMessageReply
from async_checkpoint_sdk.models.cloud_disconnect_mgmt_request import CloudDisconnectMgmtRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def disconnect_cloud_services(
    client: ClientSession, data: CloudDisconnectMgmtRequest, config: SDKConfig, **kwargs
) -> ApiMessageReply:
    """
    Disconnect the Management Server from Check Point's Infinity Portal.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : CloudDisconnectMgmtRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiMessageReply
    """
    url = f"https://{config.server}:{config.port}/web_api/disconnect-cloud-services"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiMessageReply(**resp)
