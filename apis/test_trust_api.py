from aiohttp import ClientSession

from config import Config
from models.trust_request_base import TrustRequestBase
from models.trust_status_reply import TrustStatusReply


async def test_trust(
    client: ClientSession, data: TrustRequestBase, config: Config, **kwargs
) -> TrustStatusReply:
    """
    Test an existing Trusted communication between the Management Server and the managed Security Gateway.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : TrustRequestBase [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TrustStatusReply
    """
    url = f"https://{config.server}:{config.port}/web_api/test-trust"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TrustStatusReply(**resp)
