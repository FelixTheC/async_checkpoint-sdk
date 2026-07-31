from aiohttp import ClientSession

from async_checkpoint_sdk.models.scaled_identity_sharing_key_reply import (
    ScaledIdentitySharingKeyReply,
)
from async_checkpoint_sdk.models.scaled_identity_sharing_key_request import (
    ScaledIdentitySharingKeyRequest,
)
from config import Config


async def set_identity_sharing_key(
    client: ClientSession, data: ScaledIdentitySharingKeyRequest, config: Config, **kwargs
) -> ScaledIdentitySharingKeyReply:
    """
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ScaledIdentitySharingKeyRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ScaledIdentitySharingKeyReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-identity-sharing-key"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ScaledIdentitySharingKeyReply(**resp)
