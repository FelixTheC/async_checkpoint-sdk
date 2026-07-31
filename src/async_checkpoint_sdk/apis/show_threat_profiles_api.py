from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_query_request import ApiQueryRequest
from async_checkpoint_sdk.models.profile_query_reply import ProfileQueryReply
from config import Config


async def show_threat_profiles(
    client: ClientSession, data: ApiQueryRequest, config: Config, **kwargs
) -> ProfileQueryReply:
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
    ProfileQueryReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-threat-profiles"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ProfileQueryReply(**resp)
