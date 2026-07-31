from .pydantic import BaseModel, Field


class OtherDomainPermissionsRequest(BaseModel):
    client_certificates: bool = Field(
        alias="client-certificates",
        description="""Create and manage client certificates for Mobile Access.""",
    )
    edit_cp_users_db: bool = Field(
        alias="edit-cp-users-db", description="""Work with user accounts and groups."""
    )
    https_inspection: str = Field(
        alias="https-inspection",
        description="""Enable and configure HTTPS Inspection rules.""",
    )
    ldap_users_db: str = Field(
        alias="ldap-users-db",
        description="""Work with the LDAP database and user accounts, groups and OUs.""",
    )
    user_authority_access: str = Field(
        alias="user-authority-access",
        description="""Work with Check Point User Authority authentication.""",
    )
    user_device_mgmt_conf: str = Field(
        alias="user-device-mgmt-conf",
        description="""Gives access to the UDM (User & Device Management) web-based application that handles security challenges in a bring your own device (BYOD) workspace.""",
    )
