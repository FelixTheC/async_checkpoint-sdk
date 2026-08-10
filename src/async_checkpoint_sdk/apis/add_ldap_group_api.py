from aiohttp import ClientSession

from async_checkpoint_sdk.models.ldap_group_reply import LdapGroupReply
from async_checkpoint_sdk.models.ldap_group_request_new import LdapGroupRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_ldap_group(
    client: ClientSession, data: LdapGroupRequestNew, config: SDKConfig, **kwargs
) -> LdapGroupReply:
    """
    Create new LDAP Group.

    Parameters
    ----------
    client : ClientSession
    data : LdapGroupRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    LdapGroupReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-ldap-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LdapGroupReply(**resp)
