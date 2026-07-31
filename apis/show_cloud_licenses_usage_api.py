from config import Config
from aiohttp import ClientSession
from models.view_central_licenses_request import ViewCentralLicensesRequest
from models.view_central_licenses_list_reply import ViewCentralLicensesListReply


async def show_cloud_licenses_usage(
    client: ClientSession, data: ViewCentralLicensesRequest, config: Config, **kwargs
) -> ViewCentralLicensesListReply:
    """
    Show attached licenses usage.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ViewCentralLicensesRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ViewCentralLicensesListReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-cloud-licenses-usage"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ViewCentralLicensesListReply(**resp)
