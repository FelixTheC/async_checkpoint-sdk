from aiohttp import ClientSession

from async_checkpoint_sdk.models.data_group_reply import DataGroupReply
from async_checkpoint_sdk.models.data_group_request_new import DataGroupRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_data_type_group(
    client: ClientSession, data: DataGroupRequestNew, config: SDKConfig, **kwargs
) -> DataGroupReply:
    """
    Create new Data Group Type Object.

    Parameters
    ----------
    client : ClientSession
    data : DataGroupRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    DataGroupReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-data-type-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DataGroupReply(**resp)
