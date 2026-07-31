from aiohttp import ClientSession

from async_checkpoint_sdk.models.protection_query_reply import ProtectionQueryReply
from async_checkpoint_sdk.models.protection_query_request import ProtectionQueryRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_threat_protections(
    client: ClientSession, data: ProtectionQueryRequest, config: SDKConfig, **kwargs
) -> ProtectionQueryReply:
    """
    Retrieve all objects.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ProtectionQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ProtectionQueryReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-threat-protections"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ProtectionQueryReply(**resp)
