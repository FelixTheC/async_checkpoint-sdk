from aiohttp import ClientSession

from async_checkpoint_sdk.models.global_domain_edit_reply import GlobalDomainEditReply
from async_checkpoint_sdk.models.global_domain_request_edit import GlobalDomainRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_global_domain(
    client: ClientSession, data: GlobalDomainRequestEdit, config: SDKConfig, **kwargs
) -> GlobalDomainEditReply:
    """
    Edit Global domain object using domain name or UID. When the list of Multi Domain Server is edited, the command is handled asynchronously. A list of task identifiers is returned to a user. In this case, the changes to the Global domain object are done in a public session and so should not be published. If the domain is changed in other parameters than the Multi Domain Servers, i.e.: comments, color or tags, such changes are done in the user's private session and therefore should be published. In this case, the returned command output is similar to the one of 'show-global-domain'.

    Parameters
    ----------
    client : ClientSession
    data : GlobalDomainRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    GlobalDomainEditReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-global-domain"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GlobalDomainEditReply(**resp)
