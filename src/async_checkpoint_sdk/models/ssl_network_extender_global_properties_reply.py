from pydantic import BaseModel, Field


class SslNetworkExtenderGlobalPropertiesReply(BaseModel):
    user_auth_method: str = Field(
        alias="user-auth-method",
        description="""Wide Impact: Also applies for SecureClient Mobile devices and Check Point GO clients!<br>User authentication method indicates how the user will be authenticated by the gateway. Changes made here will also apply for SSL clients.<br>Legacy - Username and password only.<br>Certificate - Certificate only with an existing certificate.<br>Certificate with Enrollment - Allows you to obtain a new certificate and then use certificate authentication only.<br>Mixed - Can use either username and password or certificate.""",
    )
    supported_encryption_methods: str = Field(
        alias="supported-encryption-methods",
        description="""Wide Impact: Also applies to SecureClient Mobile devices!<br>Select the encryption algorithms that will be supported for remote users. Changes made here will also apply for all SSL clients.""",
    )
    client_upgrade_upon_connection: str = Field(
        alias="client-upgrade-upon-connection",
        description="""When a client connects to the gateway with SSL Network Extender, the client automatically checks for upgrade. Select whether the client should automatically upgrade.""",
    )
    client_uninstall_upon_disconnection: str = Field(
        alias="client-uninstall-upon-disconnection",
        description="""Select whether the client should automatically uninstall SSL Network Extender when it disconnects from the gateway.""",
    )
    re_auth_user_interval: int = Field(
        alias="re-auth-user-interval",
        description="""Wide Impact: Applies for the SecureClient Mobile!<br>Select the interval that users will need to reauthenticate.""",
    )
    scan_ep_machine_for_compliance_with_ep_compliance_policy: bool = Field(
        alias="scan-ep-machine-for-compliance-with-ep-compliance-policy",
        description="""Set to true if you want endpoint machines to be scanned for compliance with the Endpoint Compliance Policy.""",
    )
    client_outgoing_keep_alive_packets_frequency: int = Field(
        alias="client-outgoing-keep-alive-packets-frequency",
        description="""Select the interval which the keep-alive packets are sent.""",
    )
