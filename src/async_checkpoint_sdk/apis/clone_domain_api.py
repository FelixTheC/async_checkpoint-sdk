from aiohttp import ClientSession

from async_checkpoint_sdk.models.clone_domain_request import CloneDomainRequest
from async_checkpoint_sdk.models.migration_reply import MigrationReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_domain(
    client: ClientSession, data: CloneDomainRequest, config: SDKConfig, **kwargs
) -> MigrationReply:
    """
    Clones an existing Domain and applicable Check Point configuration. <br>This command applies only to a Multi-Domain Security Management Server. <br>This command is available only after you log in to the System Data domain. <br><br>For more information and list of limitations, see <span class="show-only-in-doc-ui"><a data-toggle="modal" href=https://support.checkpoint.com/results/sk/sk180631><u>sk180631</u></a></span>.

    Parameters
    ----------
    client : ClientSession [Argument]
        data : CloneDomainRequest [Argument]
        data-toggle="modal" href=https://support.checkpoint.com/results/sk/sk180631><u>sk180631</u></a></span>.
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MigrationReply
    data : CloneDomainRequest [Argument]
        data : CloneDomainRequest [Argument]
        data-toggle="modal" href=https://support.checkpoint.com/results/sk/sk180631><u>sk180631</u></a></span>.
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MigrationReply
    config : Config [Argument]
        data : CloneDomainRequest [Argument]
        data-toggle="modal" href=https://support.checkpoint.com/results/sk/sk180631><u>sk180631</u></a></span>.
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MigrationReply
    data : CloneDomainRequest [Argument]
        data : CloneDomainRequest [Argument]
        data-toggle="modal" href=https://support.checkpoint.com/results/sk/sk180631><u>sk180631</u></a></span>.
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MigrationReply
    data : CloneDomainRequest [Argument]
        data : CloneDomainRequest [Argument]
        data-toggle="modal" href=https://support.checkpoint.com/results/sk/sk180631><u>sk180631</u></a></span>.
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MigrationReply
    config : Config [Argument]
        data : CloneDomainRequest [Argument]
        data-toggle="modal" href=https://support.checkpoint.com/results/sk/sk180631><u>sk180631</u></a></span>.
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MigrationReply
    config : Config [Argument]
        data : CloneDomainRequest [Argument]
        data-toggle="modal" href=https://support.checkpoint.com/results/sk/sk180631><u>sk180631</u></a></span>.
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MigrationReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-domain"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MigrationReply(**resp)
