from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)
from async_checkpoint_sdk.models.updatable_object_reply import UpdatableObjectReply
from config import Config


async def show_updatable_object(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: Config, **kwargs
) -> UpdatableObjectReply:
    """
    Retrieves an existing Updatable Object from the Management server.

    Parameters
    ----------
    client : ClientSession [Argument]
        data : ApiVisualCPObjectIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UpdatableObjectReply
    data : ApiVisualCPObjectIdentifierRequestShow [Argument]
        data : ApiVisualCPObjectIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UpdatableObjectReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-updatable-object"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return UpdatableObjectReply(**resp)
