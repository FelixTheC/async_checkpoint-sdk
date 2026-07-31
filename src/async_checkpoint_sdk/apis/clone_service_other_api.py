from aiohttp import ClientSession

from async_checkpoint_sdk.models.other_service_reply import OtherServiceReply
from async_checkpoint_sdk.models.other_service_request_edit import OtherServiceRequestEdit
from config import Config


async def clone_service_other(
    client: ClientSession, data: OtherServiceRequestEdit, config: Config, **kwargs
) -> OtherServiceReply:
    """
    Clone existing object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : OtherServiceRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    OtherServiceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-service-other"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return OtherServiceReply(**resp)
