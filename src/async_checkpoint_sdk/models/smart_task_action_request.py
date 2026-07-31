from pydantic import BaseModel, Field
from send_web_request_action_request import SendWebRequestActionRequest


class SmartTaskActionRequest(BaseModel):
    send_web_request: SendWebRequestActionRequest = Field(
        alias="send-web-request",
        description="""When the trigger is fired, sends an HTTPS POST web request to the configured URL.<br>The trigger data will be passed along with the SmartTask's custom data in the request's payload.""",
    )
