from aiohttp import ClientSession

from async_checkpoint_sdk.models.ftp_resource_reply import FtpResourceReply
from async_checkpoint_sdk.models.ftp_resource_request_new import FtpResourceRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_resource_ftp(
    client: ClientSession, data: FtpResourceRequestNew, config: SDKConfig, **kwargs
) -> FtpResourceReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession
    data : FtpResourceRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    FtpResourceReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-resource-ftp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return FtpResourceReply(**resp)
