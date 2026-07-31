from api_domain_identifier import ApiDomainIdentifier
from api_object_standard_identifier import ApiObjectStandardIdentifier
from available_actions_reply import AvailableActionsReply
from cvp_object_reply import CvpObjectReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field
from smtp_action1_reply import SmtpAction1Reply
from smtp_action2_reply import SmtpAction2Reply
from smtp_match_object_reply import SmtpMatchObjectReply


class SmtpResourceReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    mail_delivery_server: str = Field(
        alias="mail-delivery-server",
        description="""Specify the server to which mail is forwarded.""",
    )
    type: str = Field(alias="type", description="""Object type.""")
    deliver_messages_using_dns_mx_records: bool = Field(
        alias="deliver-messages-using-dns-mx-records",
        description="""MX record resolving is used to set the destination IP address of the connection.""",
    )
    check_rulebase_with_new_destination: bool = Field(
        alias="check-rulebase-with-new-destination",
        description="""The Rule Base will be rechecked with the new resolved IP address for mail delivery.""",
    )
    notify_sender_on_error: bool = Field(
        alias="notify-sender-on-error", description="""Enable error mail delivery."""
    )
    error_mail_delivery_server: str = Field(
        alias="error-mail-delivery-server",
        description="""Error mail delivery happens if the SMTP security server is unable to deliver the message within the abandon time, and Notify Sender on Error is checked.""",
    )
    error_deliver_messages_using_dns_mx_records: bool = Field(
        alias="error-deliver-messages-using-dns-mx-records",
        description="""MX record resolving will be used to set the source IP address of the connection used to send the error message.""",
    )
    error_check_rulebase_with_new_destination: bool = Field(
        alias="error-check-rulebase-with-new-destination",
        description="""The Rule Base will be rechecked with the new resolved IP address for error mail delivery.""",
    )
    exception_track: ApiObjectStandardIdentifier = Field(
        alias="exception-track",
        description="""Determines if an action specified in the Action 2 and CVP categories taken as a result of a resource definition is logged.""",
    )
    match: SmtpMatchObjectReply = Field(
        alias="match", description="""Set the Match properties for the SMTP resource."""
    )
    action_1: SmtpAction1Reply = Field(
        alias="action-1",
        description="""Use the Rewriting Rules to rewrite Sender and Recipient headers in emails, you can also rewrite other email headers by using the custom header field.""",
    )
    action_2: SmtpAction2Reply = Field(
        alias="action-2",
        description="""Use this window to configure mail inspection for the SMTP Resource.""",
    )
    cvp: CvpObjectReply = Field(
        alias="cvp", description="""Configure CVP inspection on mail messages."""
    )
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
    available_actions: AvailableActionsReply = Field(
        alias="available-actions", description="""Actions that are available on the object."""
    )
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
