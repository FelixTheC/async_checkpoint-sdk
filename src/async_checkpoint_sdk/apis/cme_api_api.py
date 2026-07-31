from aiohttp import ClientSession

from async_checkpoint_sdk.models.cme_api_cmd_reply import CmeApiCmdReply
from async_checkpoint_sdk.models.cme_api_cmd_request import CmeApiCmdRequest
from config import Config


async def cme_api(
    client: ClientSession, data: CmeApiCmdRequest, config: Config, **kwargs
) -> CmeApiCmdReply:
    """
    CME is a utility that runs on Check Point's Security Management Server and Multi-Domain Servers running Gaia OS. CME allows cloud native integration between Check Point CloudGuard Network solutions and Cloud platforms. For more information, see the <A HREF = "https://sc1.checkpoint.com/documents/IaaS/WebAdminGuides/EN/CP_CME/Default.htm"><b>CME Administration Guide</b></A>. <br><br>This Management API allow you to control and configure the CME utility that is deployed on the Management Server. <br><br>Use this format to execute CME API requests: <br><u>Web Services syntax: </u> <b>&lt;HTTP-Method&gt; https://&lt;mgmt-server&gt;:&lt;port&gt;/web_api/cme-api/&lt;cme-api-version&gt;/&lt;cme-command&gt; </b><br><u>mgmt_cli syntax:</u> <b>mgmt_cli cme-api/&lt;cme-api-version&gt;/&lt;cme-command&gt; --method &lt;HTTP-Method&gt; </b><br><br><ul><li>&lt;HTTP-Method&gt; - It is possible to use either POST, GET, DELETE or PUT based on the API documentation below. </li><li>&lt;cme-api-version&gt; - <b>Optional</b> parameter. The specific version of CME API to use (such as 'v1'). <br/>Note: the latest version is used by default. </li><li>&lt;cme-command&gt; - The CME API command that you want to use. For all available commands, see below. </li></ul><br>For a description of all CME API commands and versions and end-to-end examples, see the <A HREF = "https://app.swaggerhub.com/apis-docs/Check-Point/cme-api/"><button style="background-color: #ccffcc;"><b><u>CME API Documentation</u></b></button></A> in SwaggerHub. </br></br><b>Note:</b> CME-API is supported from CME take 139 and higher.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : CmeApiCmdRequest [Argument]
        config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CmeApiCmdReply
    config : Config [Argument]
        data : CmeApiCmdRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CmeApiCmdReply
    config : Config [Argument]
        data : CmeApiCmdRequest [Argument]
        config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CmeApiCmdReply
    """
    url = f"https://{config.server}:{config.port}/web_api/cme-api"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with getattr(client, kwargs["method"])(
        url, **data_obj, raise_for_status=True, ssl=False
    ) as response:
        resp = await response.json()
    return CmeApiCmdReply(**resp)
