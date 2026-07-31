from aiohttp import ClientSession

from async_checkpoint_sdk.models.administrator_reply import AdministratorReply
from async_checkpoint_sdk.models.administrator_request_new import AdministratorRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_administrator(
    client: ClientSession, data: AdministratorRequestNew, config: SDKConfig, **kwargs
) -> AdministratorReply:
    """
    Create new administrator.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : AdministratorRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AdministratorReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-administrator"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AdministratorReply(**resp)
