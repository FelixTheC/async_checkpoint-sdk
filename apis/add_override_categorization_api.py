from config import Config
from aiohttp import ClientSession
from models.override_categorization_request_new import OverrideCategorizationRequestNew
from models.override_categorization_reply import OverrideCategorizationReply


async def add_override_categorization(
    client: ClientSession, data: OverrideCategorizationRequestNew, config: Config, **kwargs
) -> OverrideCategorizationReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : OverrideCategorizationRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    OverrideCategorizationReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-override-categorization"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return OverrideCategorizationReply(**resp)
