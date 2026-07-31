from aiohttp import ClientSession

from config import Config
from models.central_licenses_list_reply import CentralLicensesListReply
from models.delete_central_licenses_request import DeleteCentralLicensesRequest


async def delete_central_license(
    client: ClientSession, data: DeleteCentralLicensesRequest, config: Config, **kwargs
) -> CentralLicensesListReply:
    """
    Delete central license.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : DeleteCentralLicensesRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CentralLicensesListReply
    """
    url = f"https://{config.server}:{config.port}/web_api/delete-central-license"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CentralLicensesListReply(**resp)
