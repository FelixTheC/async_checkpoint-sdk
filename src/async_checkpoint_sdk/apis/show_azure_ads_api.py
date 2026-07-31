from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_query_object_reply import ApiQueryObjectReply
from async_checkpoint_sdk.models.api_query_request import ApiQueryRequest
from config import Config


async def show_azure_ads(
    client: ClientSession, data: ApiQueryRequest, config: Config, **kwargs
) -> ApiQueryObjectReply:
    """
    Retrieve existing Microsoft Entra ID Servers (formerly, Azure AD). <br>Reply will not contain the sensitive properties <i><b>application key</i></b> and <i><b>password</i></b>.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiQueryObjectReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-azure-ads"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiQueryObjectReply(**resp)
