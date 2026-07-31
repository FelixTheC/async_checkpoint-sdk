from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_query_object_reply import ApiQueryObjectReply
from async_checkpoint_sdk.models.idp_to_domain_assignment_api_query_request import (
    IdpToDomainAssignmentApiQueryRequest,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_idp_to_domain_assignments(
    client: ClientSession, data: IdpToDomainAssignmentApiQueryRequest, config: SDKConfig, **kwargs
) -> ApiQueryObjectReply:
    """
    Retrieve all Identity Provider to domain assignments. This command only available  for Multi-Domain server.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : IdpToDomainAssignmentApiQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiQueryObjectReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-idp-to-domain-assignments"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiQueryObjectReply(**resp)
