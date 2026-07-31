from aiohttp import ClientSession

from config import Config
from models.trusted_client_reply import TrustedClientReply
from models.trusted_client_request_new import TrustedClientRequestNew


async def add_trusted_client(
    client: ClientSession, data: TrustedClientRequestNew, config: Config, **kwargs
) -> TrustedClientReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : TrustedClientRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TrustedClientReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-trusted-client"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TrustedClientReply(**resp)
