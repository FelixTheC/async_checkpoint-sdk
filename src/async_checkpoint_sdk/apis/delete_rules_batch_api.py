from aiohttp import ClientSession

from async_checkpoint_sdk.models.batch_reply_task import BatchReplyTask
from async_checkpoint_sdk.models.rule_batch_request_delete import RuleBatchRequestDelete
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def delete_rules_batch(
    client: ClientSession, data: RuleBatchRequestDelete, config: SDKConfig, **kwargs
) -> BatchReplyTask:
    """
    Delete rules in batch from the same layer. Use this API to achieve optimum performance when removing more than one rule. <br>Note: Warnings are ignored when using this API, operation will apply changes while ignoring warnings. <br>Supported rules types: access-rule, nat-rule, https-rule and threat-exception.

    Parameters
    ----------
    client : ClientSession
    data : RuleBatchRequestDelete
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    BatchReplyTask

    """
    url = f"https://{config.server}:{config.port}/web_api/delete-rules-batch"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return BatchReplyTask(**resp)
