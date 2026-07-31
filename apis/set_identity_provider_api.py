from config import Config
from aiohttp import ClientSession
from models.identity_provider_request_edit import IdentityProviderRequestEdit
from models.identity_provider_reply import IdentityProviderReply


async def set_identity_provider(
    client: ClientSession, data: IdentityProviderRequestEdit, config: Config, **kwargs
) -> IdentityProviderReply:
    """
    Edit existing SAML Identity Provider using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : IdentityProviderRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    IdentityProviderReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-identity-provider"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return IdentityProviderReply(**resp)
