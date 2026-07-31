from aiohttp import ClientSession

from async_checkpoint_sdk.models.idp_group_request_edit import IdpGroupRequestEdit
from async_checkpoint_sdk.models.idp_group_role_reply import IdpGroupRoleReply
from config import Config


async def set_idp_administrator_group(
    client: ClientSession, data: IdpGroupRequestEdit, config: Config, **kwargs
) -> IdpGroupRoleReply:
    """
    Edit existing Identity Provider administrators group using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : IdpGroupRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    IdpGroupRoleReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-idp-administrator-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return IdpGroupRoleReply(**resp)
