from config import Config
from aiohttp import ClientSession
from models.idp_group_request_new import IdpGroupRequestNew
from models.idp_group_role_reply import IdpGroupRoleReply


async def add_idp_administrator_group(
    client: ClientSession, data: IdpGroupRequestNew, config: Config, **kwargs
) -> IdpGroupRoleReply:
    """
    Create new Identity Provider administrators group.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : IdpGroupRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    IdpGroupRoleReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-idp-administrator-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return IdpGroupRoleReply(**resp)
