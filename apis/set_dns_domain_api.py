from config import Config
from aiohttp import ClientSession
from models.dns_domain_reply import DnsDomainReply
from models.dns_domain_request_edit import DnsDomainRequestEdit


async def set_dns_domain(
    client: ClientSession, data: DnsDomainRequestEdit, config: Config, **kwargs
) -> DnsDomainReply:
    """
    Edit an existing Domain object using the object name or UID.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : DnsDomainRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DnsDomainReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-dns-domain"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DnsDomainReply(**resp)
