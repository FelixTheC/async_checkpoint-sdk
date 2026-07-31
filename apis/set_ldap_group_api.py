from config import Config
from aiohttp import ClientSession
from models.ldap_group_request_edit import LdapGroupRequestEdit
from models.ldap_group_reply import LdapGroupReply


async def set_ldap_group(
    client: ClientSession, data: LdapGroupRequestEdit, config: Config, **kwargs
) -> LdapGroupReply:
    """
    Edit existing LDAP Group using object name or uid.
    
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
    url = f"https://{config.server}:{config.port}/web_api/set-ldap-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LdapGroupReply(**resp)
