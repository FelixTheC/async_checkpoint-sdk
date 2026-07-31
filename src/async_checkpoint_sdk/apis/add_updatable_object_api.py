from aiohttp import ClientSession

from async_checkpoint_sdk.models.updatable_object_reply import UpdatableObjectReply
from async_checkpoint_sdk.models.updatable_object_request_new import UpdatableObjectRequestNew
from config import Config


async def add_updatable_object(
    client: ClientSession, data: UpdatableObjectRequestNew, config: Config, **kwargs
) -> UpdatableObjectReply:
    """
    Import an updatable object from the repository to the management server. This operation takes effect immediately and doesn't require publishing.

    Parameters
    ----------
    client : ClientSession [Argument]
        data : UpdatableObjectRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UpdatableObjectReply
    data : UpdatableObjectRequestNew [Argument]
        data : UpdatableObjectRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UpdatableObjectReply
    data : UpdatableObjectRequestNew [Argument]
        data : UpdatableObjectRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UpdatableObjectReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-updatable-object"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return UpdatableObjectReply(**resp)
