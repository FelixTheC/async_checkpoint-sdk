from config import Config
from aiohttp import ClientSession
from models.appi_update_schedule_request_show import AppiUpdateScheduleRequestShow
from models.appi_update_schedule_reply import AppiUpdateScheduleReply


async def show_app_control_update_schedule(
    client: ClientSession, data: AppiUpdateScheduleRequestShow, config: Config, **kwargs
) -> AppiUpdateScheduleReply:
    """
    Retrieve existing Application Control and URL Filtering update schedule.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : AppiUpdateScheduleRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AppiUpdateScheduleReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-app-control-update-schedule"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AppiUpdateScheduleReply(**resp)
