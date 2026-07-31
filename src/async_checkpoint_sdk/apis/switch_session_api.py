from aiohttp import ClientSession

from async_checkpoint_sdk.models.work_session_reply import WorkSessionReply
from async_checkpoint_sdk.models.work_session_switch_request import WorkSessionSwitchRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def switch_session(
    client: ClientSession, data: WorkSessionSwitchRequest, config: SDKConfig, **kwargs
) -> WorkSessionReply:
    """
    Switch to a disconnected Management API session of the same administrator. To switch to an open session or to a session of a different administrator use the take-over session API.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : WorkSessionSwitchRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    WorkSessionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/switch-session"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return WorkSessionReply(**resp)
