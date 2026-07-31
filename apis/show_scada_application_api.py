from aiohttp import ClientSession

from config import Config
from models.application_site_identifier_request_show import ApplicationSiteIdentifierRequestShow
from models.scada_application_reply import ScadaApplicationReply


async def show_scada_application(
    client: ClientSession, data: ApplicationSiteIdentifierRequestShow, config: Config, **kwargs
) -> ScadaApplicationReply:
    """
    Retrieve existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApplicationSiteIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ScadaApplicationReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-scada-application"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ScadaApplicationReply(**resp)
