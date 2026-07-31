from aiohttp import ClientSession

from async_checkpoint_sdk.models.access_role_reply import AccessRoleReply
from async_checkpoint_sdk.models.access_role_request_edit import AccessRoleRequestEdit
from config import Config


async def clone_access_role(
    client: ClientSession, data: AccessRoleRequestEdit, config: Config, **kwargs
) -> AccessRoleReply:
    """
    Clone existing object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : AccessRoleRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AccessRoleReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-access-role"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AccessRoleReply(**resp)
