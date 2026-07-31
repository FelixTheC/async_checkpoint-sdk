from .access_control_domain_permissions_reply import AccessControlDomainPermissionsReply
from .api_domain_identifier import ApiDomainIdentifier
from .available_actions_reply import AvailableActionsReply
from .endpoint_domain_permissions_reply import EndpointDomainPermissionsReply
from .events_and_reports_domain_permissions_reply import (
    EventsAndReportsDomainPermissionsReply,
)
from .gateways_domain_permissions_reply import GatewaysDomainPermissionsReply
from .management_domain_permissions_reply import ManagementDomainPermissionsReply
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .monitoring_and_logging_domain_permissions_reply import (
    MonitoringAndLoggingDomainPermissionsReply,
)
from .other_domain_permissions_reply import OtherDomainPermissionsReply
from .pydantic import BaseModel, Field
from .threat_prevention_domain_permissions_reply import (
    ThreatPreventionDomainPermissionsReply,
)


class DomainPermissionsProfileReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    permission_type: str = Field(
        alias="permission-type", description="""The type of the Permission Profile."""
    )
    edit_common_objects: bool = Field(
        alias="edit-common-objects",
        description="""Define and manage objects in the Check Point database: Network Objects, Services, Custom Application Site, VPN Community, Users, Servers, Resources, Time, UserCheck, and Limit.<br>Only a 'Customized' permission-type profile can edit this permission.""",
    )
    access_control: AccessControlDomainPermissionsReply = Field(
        alias="access-control",
        description="""Access Control permissions.<br>Only a 'Customized' permission-type profile can edit these permissions.""",
    )
    endpoint: EndpointDomainPermissionsReply = Field(
        alias="endpoint",
        description="""Endpoint permissions. Not supported for Multi-Domain Servers.<br>Only a 'Customized' permission-type profile can edit these permissions.""",
    )
    events_and_reports: EventsAndReportsDomainPermissionsReply = Field(
        alias="events-and-reports",
        description="""Events and Reports permissions.<br>Only a 'Customized' permission-type profile can edit these permissions.""",
    )
    gateways: GatewaysDomainPermissionsReply = Field(
        alias="gateways",
        description="""Gateways permissions. <br>Only a 'Customized' permission-type profile can edit these permissions.""",
    )
    management: ManagementDomainPermissionsReply = Field(
        alias="management", description="""Management permissions."""
    )
    monitoring_and_logging: MonitoringAndLoggingDomainPermissionsReply = Field(
        alias="monitoring-and-logging",
        description="""Monitoring and Logging permissions.<br>'Customized' permission-type profile can edit all these permissions. 'Read Write All' permission-type can edit only dlp-logs-including-confidential-fields and manage-dlp-messages permissions.""",
    )
    threat_prevention: ThreatPreventionDomainPermissionsReply = Field(
        alias="threat-prevention",
        description="""Threat Prevention permissions.<br>Only a 'Customized' permission-type profile can edit these permissions.""",
    )
    others: OtherDomainPermissionsReply = Field(
        alias="others",
        description="""Additional permissions.<br>Only a 'Customized' permission-type profile can edit these permissions.""",
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    icon: str = Field(alias="icon", description="""Object icon.""")
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
    read_only: bool = Field(
        alias="read-only", description="""Indicates whether the object is read-only."""
    )
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
