from config import Config
from aiohttp import ClientSession
from models.api_query_request import ApiQueryRequest
from models.infinity_cloud_idp_query_reply import InfinityCloudIdpQueryReply


async def show_infinity_cloud_idps(
    client: ClientSession, data: ApiQueryRequest, config: Config, **kwargs
) -> InfinityCloudIdpQueryReply:
    """
    Retrieve all objects.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    InfinityCloudIdpQueryReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-infinity-cloud-idps"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return InfinityCloudIdpQueryReply(**resp)
