from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_ok_reply import ApiOkReply
from async_checkpoint_sdk.models.api_visual_c_p_object_identifier_request_delete import (
    ApiVisualCPObjectIdentifierRequestDelete,
)
from config import Config


async def delete_passcode_profile(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestDelete, config: Config, **kwargs
) -> ApiOkReply:
    """
    Delete existing Passcode Profile using name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiVisualCPObjectIdentifierRequestDelete [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/delete-passcode-profile"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
