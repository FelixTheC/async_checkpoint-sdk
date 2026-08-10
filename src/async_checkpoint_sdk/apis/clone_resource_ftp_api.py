from aiohttp import ClientSession

from async_checkpoint_sdk.models.ftp_resource_reply import FtpResourceReply
from async_checkpoint_sdk.models.ftp_resource_request_edit import FtpResourceRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_resource_ftp(
    client: ClientSession, data: FtpResourceRequestEdit, config: SDKConfig, **kwargs
) -> FtpResourceReply:
    """
    Clone existing object.

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
    url = f"https://{config.server}:{config.port}/web_api/clone-resource-ftp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return FtpResourceReply(**resp)
