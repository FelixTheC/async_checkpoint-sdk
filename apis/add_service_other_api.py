from aiohttp import ClientSession

from config import Config
from models.other_service_reply import OtherServiceReply
from models.other_service_request_new import OtherServiceRequestNew


async def add_service_other(
    client: ClientSession, data: OtherServiceRequestNew, config: Config, **kwargs
) -> OtherServiceReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : OtherServiceRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    OtherServiceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-service-other"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return OtherServiceReply(**resp)
