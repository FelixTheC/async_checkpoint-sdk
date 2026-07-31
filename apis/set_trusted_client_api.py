from config import Config
from aiohttp import ClientSession
from models.trusted_client_request_edit import TrustedClientRequestEdit
from models.trusted_client_reply import TrustedClientReply


async def set_trusted_client(
    client: ClientSession, data: TrustedClientRequestEdit, config: Config, **kwargs
) -> TrustedClientReply:
    """
    Edit existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : TrustedClientRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TrustedClientReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-trusted-client"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TrustedClientReply(**resp)
