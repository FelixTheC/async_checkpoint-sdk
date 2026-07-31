from config import Config
from aiohttp import ClientSession
from models.secu_remote_dns_reply import SecuRemoteDnsReply
from models.secu_remote_dns_request_new import SecuRemoteDnsRequestNew


async def add_securemote_dns_server(
    client: ClientSession, data: SecuRemoteDnsRequestNew, config: Config, **kwargs
) -> SecuRemoteDnsReply:
    """
    Create new SecuRemote DNS server.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : SecuRemoteDnsRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SecuRemoteDnsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-securemote-dns-server"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SecuRemoteDnsReply(**resp)
