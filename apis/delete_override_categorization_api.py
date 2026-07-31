from aiohttp import ClientSession

from config import Config
from models.api_ok_reply import ApiOkReply
from models.override_categorization_request_delete import OverrideCategorizationRequestDelete


async def delete_override_categorization(
    client: ClientSession, data: OverrideCategorizationRequestDelete, config: Config, **kwargs
) -> ApiOkReply:
    """
    Delete existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : OverrideCategorizationRequestDelete [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/delete-override-categorization"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
