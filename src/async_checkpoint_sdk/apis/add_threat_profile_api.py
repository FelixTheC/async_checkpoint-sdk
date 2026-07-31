from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_task_reply import ApiTaskReply
from async_checkpoint_sdk.models.profile_request_new import ProfileRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_threat_profile(
    client: ClientSession, data: ProfileRequestNew, config: SDKConfig, **kwargs
) -> ApiTaskReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ProfileRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiTaskReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-threat-profile"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiTaskReply(**resp)
