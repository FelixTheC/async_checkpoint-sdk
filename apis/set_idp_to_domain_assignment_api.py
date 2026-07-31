from config import Config
from aiohttp import ClientSession
from models.idp_to_domain_assignment_reply import IdpToDomainAssignmentReply
from models.idp_to_domain_assignment_request_edit import IdpToDomainAssignmentRequestEdit


async def set_idp_to_domain_assignment(
    client: ClientSession, data: IdpToDomainAssignmentRequestEdit, config: Config, **kwargs
) -> IdpToDomainAssignmentReply:
    """
    Set Identity Provider assignment to domain, to allow administrator login to that domain using that identity provider, if there is no Identity Provider assigned to the domain the 'idp-default-assignment' will be used. This command only available  for Multi-Domain server.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : IdpToDomainAssignmentRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    IdpToDomainAssignmentReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-idp-to-domain-assignment"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return IdpToDomainAssignmentReply(**resp)
