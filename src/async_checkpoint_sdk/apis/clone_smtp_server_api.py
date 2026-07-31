from aiohttp import ClientSession

from async_checkpoint_sdk.models.smtp_server_reply import SmtpServerReply
from async_checkpoint_sdk.models.smtp_server_request_edit import SmtpServerRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_smtp_server(
    client: ClientSession, data: SmtpServerRequestEdit, config: SDKConfig, **kwargs
) -> SmtpServerReply:
    """
    Clone existing object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : SmtpServerRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SmtpServerReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-smtp-server"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SmtpServerReply(**resp)
