from aiohttp import ClientSession

from async_checkpoint_sdk.models.ips_update_schedule_reply import IpsUpdateScheduleReply
from async_checkpoint_sdk.models.ips_update_schedule_request_show import (
    IpsUpdateScheduleRequestShow,
)
from config import Config


async def show_ips_update_schedule(
    client: ClientSession, data: IpsUpdateScheduleRequestShow, config: Config, **kwargs
) -> IpsUpdateScheduleReply:
    """
    Retrieve existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : IpsUpdateScheduleRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    IpsUpdateScheduleReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-ips-update-schedule"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return IpsUpdateScheduleReply(**resp)
