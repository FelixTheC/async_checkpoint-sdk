from aiohttp import ClientSession

from async_checkpoint_sdk.models.idp_group_request_new import IdpGroupRequestNew
from async_checkpoint_sdk.models.idp_group_role_reply import IdpGroupRoleReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_idp_administrator_group(
    client: ClientSession, data: IdpGroupRequestNew, config: SDKConfig, **kwargs
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
