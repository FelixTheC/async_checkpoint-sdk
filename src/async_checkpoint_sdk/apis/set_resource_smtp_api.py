from aiohttp import ClientSession

from async_checkpoint_sdk.models.smtp_resource_reply import SmtpResourceReply
from async_checkpoint_sdk.models.smtp_resource_request_edit import SmtpResourceRequestEdit
from config import Config


async def set_resource_smtp(
    client: ClientSession, data: SmtpResourceRequestEdit, config: Config, **kwargs
) -> SmtpResourceReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : SmtpResourceRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SmtpResourceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-resource-smtp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SmtpResourceReply(**resp)
