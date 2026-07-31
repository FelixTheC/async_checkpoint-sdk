from aiohttp import ClientSession

from async_checkpoint_sdk.models.compound_group_reply import CompoundGroupReply
from async_checkpoint_sdk.models.compound_group_request_new import CompoundGroupRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_data_type_compound_group(
    client: ClientSession, data: CompoundGroupRequestNew, config: SDKConfig, **kwargs
) -> CompoundGroupReply:
    """
    Create new Compound Data Type Group Object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : CompoundGroupRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CompoundGroupReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-data-type-compound-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CompoundGroupReply(**resp)
