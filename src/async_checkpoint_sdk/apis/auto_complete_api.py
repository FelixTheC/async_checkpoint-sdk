from aiohttp import ClientSession

from async_checkpoint_sdk.models.auto_complete_reply import AutoCompleteReply
from async_checkpoint_sdk.models.auto_complete_request import AutoCompleteRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def auto_complete(
    client: ClientSession, data: AutoCompleteRequest, config: SDKConfig, **kwargs
) -> AutoCompleteReply:
    """
    Parameters
    ----------
    client : ClientSession [Argument]
    data : AutoCompleteRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AutoCompleteReply
    """
    url = f"https://{config.server}:{config.port}/web_api/auto-complete"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AutoCompleteReply(**resp)
