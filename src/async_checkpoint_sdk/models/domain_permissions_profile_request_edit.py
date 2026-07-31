from access_control_domain_permissions_request import AccessControlDomainPermissionsRequest
from endpoint_domain_permissions_request import EndpointDomainPermissionsRequest
from events_and_reports_domain_permissions_request import EventsAndReportsDomainPermissionsRequest
from gateways_domain_permissions_request import GatewaysDomainPermissionsRequest
from management_domain_permissions_request import ManagementDomainPermissionsRequest
from monitoring_and_logging_domain_permissions_request import (
    MonitoringAndLoggingDomainPermissionsRequest,
)
from other_domain_permissions_request import OtherDomainPermissionsRequest
from pydantic import BaseModel, Field
from threat_prevention_domain_permissions_request import ThreatPreventionDomainPermissionsRequest


class DomainPermissionsProfileRequestEdit(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    permission_type: str = Field(
        alias="permission-type", description="""The type of the Permissions Profile."""
    )
    edit_common_objects: bool = Field(
        alias="edit-common-objects",
        description="""Define and manage objects in the Check Point database: Network Objects, Services, Custom Application Site, VPN Community, Users, Servers, Resources, Time, UserCheck, and Limit.<br>Only a 'Customized' permission-type profile can edit this permission.""",
    )
    access_control: AccessControlDomainPermissionsRequest = Field(
        alias="access-control",
        description="""Access Control permissions.<br>Only a 'Customized' permission-type profile can edit these permissions.""",
    )
    endpoint: EndpointDomainPermissionsRequest = Field(
        alias="endpoint",
        description="""Endpoint permissions. Not supported for Multi-Domain Servers.<br>Only a 'Customized' permission-type profile can edit these permissions.""",
    )
    events_and_reports: EventsAndReportsDomainPermissionsRequest = Field(
        alias="events-and-reports",
        description="""Events and Reports permissions.<br>Only a 'Customized' permission-type profile can edit these permissions.""",
    )
    gateways: GatewaysDomainPermissionsRequest = Field(
        alias="gateways",
        description="""Gateways permissions. <br>Only a 'Customized' permission-type profile can edit these permissions.""",
    )
    management: ManagementDomainPermissionsRequest = Field(
        alias="management", description="""Management permissions."""
    )
    monitoring_and_logging: MonitoringAndLoggingDomainPermissionsRequest = Field(
        alias="monitoring-and-logging",
        description="""Monitoring and Logging permissions.<br>'Customized' permission-type profile can edit all these permissions. Read Write All permission-type can edit only dlp-logs-including-confidential-fields and manage-dlp-messages permissions.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    threat_prevention: ThreatPreventionDomainPermissionsRequest = Field(
        alias="threat-prevention",
        description="""Threat Prevention permissions.<br>Only a 'Customized' permission-type profile can edit these permissions.""",
    )
    others: OtherDomainPermissionsRequest = Field(
        alias="others",
        description="""Additional permissions.<br>Only a 'Customized' permission-type profile can edit these permissions.""",
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
