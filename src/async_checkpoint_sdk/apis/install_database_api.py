from aiohttp import ClientSession

from async_checkpoint_sdk.models.install_db_reply import InstallDbReply
from async_checkpoint_sdk.models.install_db_request import InstallDbRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def install_database(
    client: ClientSession, data: InstallDbRequest, config: SDKConfig, **kwargs
) -> InstallDbReply:
    """
    Copies the user database and network objects information to specified targets.

    Parameters
    ----------
    client : ClientSession [Argument]
        data : InstallDbRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    InstallDbReply
    data : InstallDbRequest [Argument]
        data : InstallDbRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    InstallDbReply
    data : InstallDbRequest [Argument]
        data : InstallDbRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    InstallDbReply
    """
    url = f"https://{config.server}:{config.port}/web_api/install-database"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return InstallDbReply(**resp)
