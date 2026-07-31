from pydantic import BaseModel, Field


class BypassUnderLoadReply(BaseModel):
    track: str = Field(
        alias="track",
        description="""Whether to log and send a notification for the bypass under load:<br><ul style=list-style-type:square><li>None - Does not record the event.</li><li>Log - Records the event details. Use SmartConsole or SmartView to see the logs.</li><li>Alert - Logs the event and executes a command you configured.</li><li>Mail - Sends an email to the administrator.</li><li>SNMP Trap - Sends an SNMP alert to the configured SNMP Management Server.</li><li>User Defined Alert - Sends a custom alert.</li></ul>.""",
    )
