from aiohttp import ClientSession

from config import Config
from models.scada_application_reply import ScadaApplicationReply
from models.scada_application_request_edit import ScadaApplicationRequestEdit


async def set_scada_application(
    client: ClientSession, data: ScadaApplicationRequestEdit, config: Config, **kwargs
) -> ScadaApplicationReply:
    """
    Edit existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ScadaApplicationRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ScadaApplicationReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-scada-application"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ScadaApplicationReply(**resp)
