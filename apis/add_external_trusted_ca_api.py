from aiohttp import ClientSession

from config import Config
from models.trusted_ca_reply import TrustedCaReply
from models.trusted_ca_request_new import TrustedCaRequestNew


async def add_external_trusted_ca(
    client: ClientSession, data: TrustedCaRequestNew, config: Config, **kwargs
) -> TrustedCaReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : TrustedCaRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TrustedCaReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-external-trusted-ca"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TrustedCaReply(**resp)
