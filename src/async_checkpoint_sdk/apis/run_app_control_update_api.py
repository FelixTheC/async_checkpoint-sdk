from aiohttp import ClientSession

from async_checkpoint_sdk.models.appi_update_reply import AppiUpdateReply
from async_checkpoint_sdk.models.appi_update_request import AppiUpdateRequest
from config import Config


async def run_app_control_update(
    client: ClientSession, data: AppiUpdateRequest, config: Config, **kwargs
) -> AppiUpdateReply:
    """
    Runs Application Control & URL Filtering database update.

    Parameters
    ----------
    client : ClientSession [Argument]
        data : AppiUpdateRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AppiUpdateReply
    data : AppiUpdateRequest [Argument]
        data : AppiUpdateRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AppiUpdateReply
    data : AppiUpdateRequest [Argument]
        data : AppiUpdateRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AppiUpdateReply
    """
    url = f"https://{config.server}:{config.port}/web_api/run-app-control-update"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AppiUpdateReply(**resp)
