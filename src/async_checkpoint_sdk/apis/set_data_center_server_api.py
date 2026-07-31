from aiohttp import ClientSession

from async_checkpoint_sdk.models.data_center_server_request_edit import DataCenterServerRequestEdit
from async_checkpoint_sdk.models.data_center_server_task_reply import DataCenterServerTaskReply
from config import Config


async def set_data_center_server(
    client: ClientSession, data: DataCenterServerRequestEdit, config: Config, **kwargs
) -> DataCenterServerTaskReply:
    """
    Edit existing Data Center Server using name or uid.<br> Data Center Server represents the connection to a cloud environment.<br> The Data Center Server contains Data Center Objects, these objects can be imported from it using the add-data-center-object command.<span class="show-only-in-doc-ui"><br><span class="show-only-in-doc-ui"><span style="color: red;">Note:</span> Each Data Center Server type uses additional dedicated arguments, <a data-toggle="modal" href="#" data-target="#DataCenterParametersModal" onclick="openDataCenterParametersModal()" ><u style="font-weight: bold;">see arguments per Data Center Server type</u></a></span><script>function openDataCenterParametersModal(){currentApiVersion = document.getElementsByClassName("version-name")[0].innerText;DataCenterParametersHTMLFile = "./data/" + currentApiVersion + "/static_content/datacenter_arguments.html";$("#data_center_modal").load(DataCenterParametersHTMLFile);}</script><div class="modal fade" id="DataCenterParametersModal" role="dialog" style="overflow-y: auto; z-index: 10000;"><div class="modal-dialog modal-lg" style="margin-top: 150px" role="document"><div id="data_center_modal" class="modal-content"/></div></div></span>.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : DataCenterServerRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DataCenterServerTaskReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-data-center-server"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DataCenterServerTaskReply(**resp)
