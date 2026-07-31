from aiohttp import ClientSession

from config import Config
from models.trusted_ca_status_reply import TrustedCaStatusReply
from models.trusted_ca_status_request import TrustedCaStatusRequest


async def show_trusted_ca_status(
    client: ClientSession, data: TrustedCaStatusRequest, config: Config, **kwargs
) -> TrustedCaStatusReply:
    """
    Show Trusted CAs package status.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : TrustedCaStatusRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TrustedCaStatusReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-trusted-ca-status"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TrustedCaStatusReply(**resp)
