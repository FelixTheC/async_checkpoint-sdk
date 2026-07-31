from aiohttp import ClientSession

from async_checkpoint_sdk.models.administrator_query_request import AdministratorQueryRequest
from async_checkpoint_sdk.models.api_query_object_reply import ApiQueryObjectReply
from config import Config


async def show_administrators(
    client: ClientSession, data: AdministratorQueryRequest, config: Config, **kwargs
) -> ApiQueryObjectReply:
    """
    Retrieve all administrators.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : AdministratorQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiQueryObjectReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-administrators"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiQueryObjectReply(**resp)
