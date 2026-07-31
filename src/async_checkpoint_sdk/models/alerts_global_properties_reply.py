from .pydantic import BaseModel, Field


class AlertsGlobalPropertiesReply(BaseModel):
    send_popup_alert_to_smartview_monitor: bool = Field(
        alias="send-popup-alert-to-smartview-monitor",
        description="""Send popup alert to SmartView Monitor when an alert is issued, it is also sent to SmartView Monitor.""",
    )
    popup_alert_script: str = Field(
        alias="popup-alert-script",
        description="""Run popup alert script the operating system script to be executed when an alert is issued. For example, set another form of notification, such as an email or a user-defined command.""",
    )
    send_mail_alert_to_smartview_monitor: bool = Field(
        alias="send-mail-alert-to-smartview-monitor",
        description="""Send mail alert to SmartView Monitor when a mail alert is issued, it is also sent to SmartView Monitor.""",
    )
    mail_alert_script: str = Field(
        alias="mail-alert-script",
        description="""Run mail alert script the operating system script to be executed when Mail is specified as the Track in a rule. The default is internal_sendmail, which is not a script but an internal Security Gateway command.""",
    )
    send_snmp_trap_alert_to_smartview_monitor: bool = Field(
        alias="send-snmp-trap-alert-to-smartview-monitor",
        description="""Send SNMP trap alert to SmartView Monitor when an SNMP trap alert is issued, it is also sent to SmartView Monitor.""",
    )
    snmp_trap_alert_script: str = Field(
        alias="snmp-trap-alert-script",
        description="""Run SNMP trap alert script command to be executed when SNMP Trap is specified as the Track in a rule. By default the internal_snmp_trap is used. This command is executed by the fwd process.""",
    )
    send_user_defined_alert_num1_to_smartview_monitor: bool = Field(
        alias="send-user-defined-alert-num1-to-smartview-monitor",
        description="""Send user defined alert no. 1 to SmartView Monitor when an alert is issued, it is also sent to SmartView Monitor.""",
    )
    user_defined_script_num1: str = Field(
        alias="user-defined-script-num1",
        description="""Run user defined script the operating system script to be run when User-Defined is specified as the Track in a rule, or when User Defined Alert no. 1 is selected as a Track Option.""",
    )
    send_user_defined_alert_num2_to_smartview_monitor: bool = Field(
        alias="send-user-defined-alert-num2-to-smartview-monitor",
        description="""Send user defined alert no. 2 to SmartView Monitor when an alert is issued, it is also sent to SmartView Monitor.""",
    )
    user_defined_script_num2: str = Field(
        alias="user-defined-script-num2",
        description="""Run user defined 2 script the operating system script to be run when User-Defined is specified as the Track in a rule, or when User Defined Alert no. 2 is selected as a Track Option.""",
    )
    send_user_defined_alert_num3_to_smartview_monitor: bool = Field(
        alias="send-user-defined-alert-num3-to-smartview-monitor",
        description="""Send user defined alert no. 3 to SmartView Monitor when an alert is issued, it is also sent to SmartView Monitor.""",
    )
    user_defined_script_num3: str = Field(
        alias="user-defined-script-num3",
        description="""Run user defined 3 script the operating system script to be run when User-Defined is specified as the Track in a rule, or when User Defined Alert no. 3 is selected as a Track Option.""",
    )
    default_track_option_for_system_alerts: str = Field(
        alias="default-track-option-for-system-alerts",
        description="""Set the default track option for System Alerts.""",
    )
