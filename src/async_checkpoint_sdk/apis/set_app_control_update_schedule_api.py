from aiohttp import ClientSession

from async_checkpoint_sdk.models.appi_update_schedule_reply import AppiUpdateScheduleReply
from async_checkpoint_sdk.models.appi_update_schedule_request_edit import (
    AppiUpdateScheduleRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_app_control_update_schedule(
    client: ClientSession, data: AppiUpdateScheduleRequestEdit, config: SDKConfig, **kwargs
) -> AppiUpdateScheduleReply:
    """
    Set the Application Control and URL Filtering update schedule.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : AppiUpdateScheduleRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AppiUpdateScheduleReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-app-control-update-schedule"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AppiUpdateScheduleReply(**resp)
