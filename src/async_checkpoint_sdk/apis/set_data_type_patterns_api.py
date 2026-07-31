from aiohttp import ClientSession

from async_checkpoint_sdk.models.patterns_data_type_reply import PatternsDataTypeReply
from async_checkpoint_sdk.models.patterns_data_type_request_edit import PatternsDataTypeRequestEdit
from config import Config


async def set_data_type_patterns(
    client: ClientSession, data: PatternsDataTypeRequestEdit, config: Config, **kwargs
) -> PatternsDataTypeReply:
    """
    Edit existing Pattern Data Type object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : PatternsDataTypeRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    PatternsDataTypeReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-data-type-patterns"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return PatternsDataTypeReply(**resp)
