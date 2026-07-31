from .pydantic import BaseModel, Field
from .run_script_action_reply import RunScriptActionReply
from .send_mail_action_reply import SendMailActionReply
from .send_web_request_action_reply import SendWebRequestActionReply


class SmartTaskActionReply(BaseModel):
    run_script: RunScriptActionReply = Field(alias="run-script", description="""N/A""")
    send_mail: SendMailActionReply = Field(alias="send-mail", description="""N/A""")
    send_web_request: SendWebRequestActionReply = Field(
        alias="send-web-request", description="""N/A"""
    )
