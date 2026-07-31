from aiohttp import ClientSession

from async_checkpoint_sdk.models.ldap_group_reply import LdapGroupReply
from async_checkpoint_sdk.models.ldap_group_request_new import LdapGroupRequestNew
from config import Config


async def add_ldap_group(
    client: ClientSession, data: LdapGroupRequestNew, config: Config, **kwargs
) -> LdapGroupReply:
    """
    Create new LDAP Group.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : LdapGroupRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

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
