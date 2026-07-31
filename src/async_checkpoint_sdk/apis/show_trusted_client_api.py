from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)
from async_checkpoint_sdk.models.trusted_client_reply import TrustedClientReply
from config import Config


async def show_trusted_client(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: Config, **kwargs
) -> TrustedClientReply:
    """
    Retrieve existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiVisualCPObjectIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TrustedClientReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-trusted-client"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TrustedClientReply(**resp)
