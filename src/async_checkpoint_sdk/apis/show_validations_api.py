from aiohttp import ClientSession

from async_checkpoint_sdk.models.validations_query_request import ValidationsQueryRequest
from async_checkpoint_sdk.models.validations_reply import ValidationsReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_validations(
    client: ClientSession, data: ValidationsQueryRequest, config: SDKConfig, **kwargs
) -> ValidationsReply:
    """
    Show all validation incidents limited to 500.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ValidationsQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ValidationsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-validations"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ValidationsReply(**resp)
