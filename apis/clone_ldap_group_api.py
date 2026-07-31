from aiohttp import ClientSession

from config import Config
from models.ldap_group_reply import LdapGroupReply
from models.ldap_group_request_edit import LdapGroupRequestEdit


async def clone_ldap_group(
    client: ClientSession, data: LdapGroupRequestEdit, config: Config, **kwargs
) -> LdapGroupReply:
    """
    Clone existing LDAP Group.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : LdapGroupRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LdapGroupReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-ldap-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LdapGroupReply(**resp)
