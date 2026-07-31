from api_domain_identifier import ApiDomainIdentifier
from applications_reply import ApplicationsReply
from available_actions_reply import AvailableActionsReply
from client_customization_reply import ClientCustomizationReply
from data_leak_prevention_reply import DataLeakPreventionReply
from harmony_mobile_reply import HarmonyMobileReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field
from security_reply import SecurityReply


class MobileProfileReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    applications: ApplicationsReply = Field(
        alias="applications", description="""Applications settings."""
    )
    client_customization: ClientCustomizationReply = Field(
        alias="client-customization", description="""Client customization settings."""
    )
    data_leak_prevention: DataLeakPreventionReply = Field(
        alias="data-leak-prevention", description="""Data leak prevention settings."""
    )
    harmony_mobile: HarmonyMobileReply = Field(
        alias="harmony-mobile", description="""Integrations settings."""
    )
    security: SecurityReply = Field(alias="security", description="""Security settings.""")
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain", description="""Information about the domain that holds the Object."""
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
        alias="available-actions", description="""Actions that are available on the object."""
    )
