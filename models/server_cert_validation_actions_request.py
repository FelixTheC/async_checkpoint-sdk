from pydantic import BaseModel, Field


class ServerCertValidationActionsRequest(BaseModel):
    block_expired: bool = Field(
        alias="block-expired",
        description="""Set to be true in order to drop traffic from servers with expired server certificate.""",
    )
    block_revoked: bool = Field(
        alias="block-revoked",
        description="""Set to be true in order to drop traffic from servers with revoked server certificate (validate CRL).""",
    )
    block_untrusted: bool = Field(
        alias="block-untrusted",
        description="""Set to be true in order to drop traffic from servers with untrusted server certificate.""",
    )
    track_errors: str = Field(
        alias="track-errors",
        description="""Whether to log and send a notification for the server validation errors:<br><ul style=list-style-type:square><li>None - Does not record the event.</li><li>Log - Records the event details in SmartView.</li><li>Alert - Logs the event and executes a command.</li><li>Mail - Sends an email to the administrator.</li><li>SNMP Trap - Sends an SNMP alert to the SNMP GU.</li><li>User Defined Alert - Sends customized alerts.</li></ul>.""",
    )
