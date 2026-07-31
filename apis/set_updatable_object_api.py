from config import Config
from aiohttp import ClientSession
from models.updatable_object_request_edit import UpdatableObjectRequestEdit
from models.updatable_object_reply import UpdatableObjectReply


async def set_updatable_object(
    client: ClientSession, data: UpdatableObjectRequestEdit, config: Config, **kwargs
) -> UpdatableObjectReply:
    """
    Edit existing Updatable Object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
        data : UpdatableObjectRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UpdatableObjectReply
    data : UpdatableObjectRequestEdit [Argument]
        data : UpdatableObjectRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UpdatableObjectReply
    data : UpdatableObjectRequestEdit [Argument]
        data : UpdatableObjectRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UpdatableObjectReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-updatable-object"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return UpdatableObjectReply(**resp)
