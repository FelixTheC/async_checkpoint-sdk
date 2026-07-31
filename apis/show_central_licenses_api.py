from aiohttp import ClientSession

from config import Config
from models.central_licenses_list_reply import CentralLicensesListReply
from models.show_central_licenses_request import ShowCentralLicensesRequest


async def show_central_licenses(
    client: ClientSession, data: ShowCentralLicensesRequest, config: Config, **kwargs
) -> CentralLicensesListReply:
    """
    Show attached licenses.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ShowCentralLicensesRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CentralLicensesListReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-central-licenses"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CentralLicensesListReply(**resp)
