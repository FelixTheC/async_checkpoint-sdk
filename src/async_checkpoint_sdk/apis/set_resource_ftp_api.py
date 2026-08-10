from aiohttp import ClientSession

from async_checkpoint_sdk.models.ftp_resource_reply import FtpResourceReply
from async_checkpoint_sdk.models.ftp_resource_request_edit import FtpResourceRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_resource_ftp(
    client: ClientSession, data: FtpResourceRequestEdit, config: SDKConfig, **kwargs
) -> FtpResourceReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : FtpResourceRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    FtpResourceReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-resource-ftp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return FtpResourceReply(**resp)
