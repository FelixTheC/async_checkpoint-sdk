from config import Config
from aiohttp import ClientSession
from models.dns_domain_reply import DnsDomainReply
from models.dns_domain_request_new import DnsDomainRequestNew


async def add_dns_domain(
    client: ClientSession, data: DnsDomainRequestNew, config: Config, **kwargs
) -> DnsDomainReply:
    """
    Create new Domain object.<br>A Domain object defines a Host of a DNS domain by its name.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : DnsDomainRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DnsDomainReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-dns-domain"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DnsDomainReply(**resp)
