from config import Config
from aiohttp import ClientSession
from models.security_group_members_reply import SecurityGroupMembersReply
from models.security_group_members_request import SecurityGroupMembersRequest


async def show_security_group_members(
    client: ClientSession, data: SecurityGroupMembersRequest, config: Config, **kwargs
) -> SecurityGroupMembersReply:
    """
    Shows the list of the Maestro Security Group Members.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : SecurityGroupMembersRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SecurityGroupMembersReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-security-group-members"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SecurityGroupMembersReply(**resp)
