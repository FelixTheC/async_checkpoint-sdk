from aiohttp import ClientSession

from async_checkpoint_sdk.models.compound_group_reply import CompoundGroupReply
from async_checkpoint_sdk.models.compound_group_request_edit import CompoundGroupRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_data_type_compound_group(
    client: ClientSession, data: CompoundGroupRequestEdit, config: SDKConfig, **kwargs
) -> CompoundGroupReply:
    """
    Edit existing Compound Data Type Group object using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : CompoundGroupRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    CompoundGroupReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-data-type-compound-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CompoundGroupReply(**resp)
