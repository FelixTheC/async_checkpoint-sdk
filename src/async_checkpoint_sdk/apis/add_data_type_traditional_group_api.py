from aiohttp import ClientSession

from async_checkpoint_sdk.models.traditional_group_reply import TraditionalGroupReply
from async_checkpoint_sdk.models.traditional_group_request_new import TraditionalGroupRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_data_type_traditional_group(
    client: ClientSession, data: TraditionalGroupRequestNew, config: SDKConfig, **kwargs
) -> TraditionalGroupReply:
    """
    Create new Traditional Group Data Type Object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : TraditionalGroupRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TraditionalGroupReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-data-type-traditional-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TraditionalGroupReply(**resp)
