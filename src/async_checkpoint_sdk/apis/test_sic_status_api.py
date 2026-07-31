from aiohttp import ClientSession

from async_checkpoint_sdk.models.sic_api_request import SicApiRequest
from async_checkpoint_sdk.models.sic_status_reply import SicStatusReply
from config import Config


async def test_sic_status(
    client: ClientSession, data: SicApiRequest, config: Config, **kwargs
) -> SicStatusReply:
    """
    Test SIC Status reflects the state of the gateway after it has received the certificate issued by the ICA. If the SIC status is Unknown then there is no connection between the gateway and the Security Management Server. If the SIC status is No Communication, an error message will appear. It may contain specific instructions on how to fix the situation.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : SicApiRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SicStatusReply
    """
    url = f"https://{config.server}:{config.port}/web_api/test-sic-status"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SicStatusReply(**resp)
