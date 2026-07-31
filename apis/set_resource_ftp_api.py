from config import Config
from aiohttp import ClientSession
from models.ftp_resource_reply import FtpResourceReply
from models.ftp_resource_request_edit import FtpResourceRequestEdit


async def set_resource_ftp(
    client: ClientSession, data: FtpResourceRequestEdit, config: Config, **kwargs
) -> FtpResourceReply:
    """
    Edit existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : FtpResourceRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

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
