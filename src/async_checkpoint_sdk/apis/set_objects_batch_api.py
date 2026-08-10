from aiohttp import ClientSession

from async_checkpoint_sdk.models.batch_reply_task import BatchReplyTask
from async_checkpoint_sdk.models.batch_request_edit import BatchRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_objects_batch(
    client: ClientSession, data: BatchRequestEdit, config: SDKConfig, **kwargs
) -> BatchReplyTask:
    """
    Edits existing objects in batch using object name or uid. To achieve optimum performance when updating more than one object, use this API. <br>Note: "ignore-errors" and "ignore-warnings" cannot be used in this API, errors and warnings are ignored and operation will apply changes while ignoring errors. It is not possible to publish changes that contain validations errors. <br>You must use the "show-validations" API to see any validation errors and warnings caused by the batch creation. <br>Batch supported types: access-role, address-range, application-site-category, application-site-group, dns-domain, dynamic-object, group, group-with-exclusion, host, lsv-profile, multicast-address-range, network, package, security-zone, service-dce-rpc, service-group, service-icmp, service-other, service-sctp, service-tcp, service-udp, tacacs-server, tacacs-group, tag, time, time-group, vpn-community-meshed, vpn-community-star, wildcard.

    Parameters
    ----------
    client : ClientSession
    data : BatchRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    BatchReplyTask

    """
    url = f"https://{config.server}:{config.port}/web_api/set-objects-batch"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return BatchReplyTask(**resp)
