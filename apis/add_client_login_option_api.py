from config import Config
from aiohttp import ClientSession
from models.client_login_option_request_new import ClientLoginOptionRequestNew
from models.client_login_option_reply import ClientLoginOptionReply


async def add_client_login_option(
    client: ClientSession, data: ClientLoginOptionRequestNew, config: Config, **kwargs
) -> ClientLoginOptionReply:
    """
    Create new client login option with authentication methods and user directory configurations.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ClientLoginOptionRequestNew [Argument]
        config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ClientLoginOptionReply
    config : Config [Argument]
        data : ClientLoginOptionRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ClientLoginOptionReply
    config : Config [Argument]
        data : ClientLoginOptionRequestNew [Argument]
        config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ClientLoginOptionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-client-login-option"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ClientLoginOptionReply(**resp)
