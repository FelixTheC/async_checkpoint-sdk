from aiohttp import ClientSession

from async_checkpoint_sdk.models.idp_to_domain_assignment_reply import IdpToDomainAssignmentReply
from async_checkpoint_sdk.models.idp_to_domain_assignment_request_show import (
    IdpToDomainAssignmentRequestShow,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_idp_to_domain_assignment(
    client: ClientSession, data: IdpToDomainAssignmentRequestShow, config: SDKConfig, **kwargs
) -> IdpToDomainAssignmentReply:
    """
    Retrieve existing Identity Provider assignment to domain object by UID or by 'assigned-domain' name or UID. This command only available  for Multi-Domain server.

    Parameters
    ----------
    client : ClientSession
    data : IdpToDomainAssignmentRequestShow
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    IdpToDomainAssignmentReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-idp-to-domain-assignment"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return IdpToDomainAssignmentReply(**resp)
