from config import Config
from aiohttp import ClientSession
from models.patterns_data_type_reply import PatternsDataTypeReply
from models.patterns_data_type_request_new import PatternsDataTypeRequestNew


async def add_data_type_patterns(
    client: ClientSession, data: PatternsDataTypeRequestNew, config: Config, **kwargs
) -> PatternsDataTypeReply:
    """
    Create new Pattern Data Type Object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : PatternsDataTypeRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    PatternsDataTypeReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-data-type-patterns"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return PatternsDataTypeReply(**resp)
