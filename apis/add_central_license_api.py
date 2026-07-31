from aiohttp import ClientSession

from config import Config
from models.add_central_licenses_request import AddCentralLicensesRequest
from models.central_licenses_reply import CentralLicensesReply


async def add_central_license(
    client: ClientSession, data: AddCentralLicensesRequest, config: Config, **kwargs
) -> CentralLicensesReply:
    """
    Add central license.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : AddCentralLicensesRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CentralLicensesReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-central-license"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CentralLicensesReply(**resp)
