from aiohttp import ClientSession

from async_checkpoint_sdk.models.smtp_resource_reply import SmtpResourceReply
from async_checkpoint_sdk.models.smtp_resource_request_new import SmtpResourceRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_resource_smtp(
    client: ClientSession, data: SmtpResourceRequestNew, config: SDKConfig, **kwargs
) -> SmtpResourceReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : SmtpResourceRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SmtpResourceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-resource-smtp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SmtpResourceReply(**resp)
