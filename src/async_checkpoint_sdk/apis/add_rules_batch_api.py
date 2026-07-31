from aiohttp import ClientSession

from async_checkpoint_sdk.models.batch_reply_task import BatchReplyTask
from async_checkpoint_sdk.models.rule_batch_request_new import RuleBatchRequestNew
from config import Config


async def add_rules_batch(
    client: ClientSession, data: RuleBatchRequestNew, config: Config, **kwargs
) -> BatchReplyTask:
    """
    Creates new rules in batch. Use this API to achieve optimum performance when adding more than one rule. <br>Note: Add multiple rules to a layer in a specific position, incrementing position by one for each rule.  <br>Note: Errors and warnings are ignored when using this API, operation will apply changes while ignoring errors. It is not possible to publish changes that contain validations errors. <br>You must use the "show-validations" API to see any validation errors and warnings caused by the batch creation. <br>Supported rules types: access-rule, nat-rule, https-rule and threat-exception.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : RuleBatchRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    BatchReplyTask
    """
    url = f"https://{config.server}:{config.port}/web_api/add-rules-batch"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return BatchReplyTask(**resp)
