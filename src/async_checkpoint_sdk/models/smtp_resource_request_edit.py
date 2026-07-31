from .add import add
from .cvp_object_request import CvpObjectRequest
from .pydantic import BaseModel, Field
from .remove import remove
from .smtp_action1_request import SmtpAction1Request
from .smtp_action2_request import SmtpAction2Request
from .smtp_match_object_request import SmtpMatchObjectRequest


class SmtpResourceRequestEdit(BaseModel):
    mail_delivery_server: str = Field(
        alias="mail-delivery-server",
        description="""Specify the server to which mail is forwarded.""",
    )
    deliver_messages_using_dns_mx_records: bool = Field(
        alias="deliver-messages-using-dns-mx-records",
        description="""MX record resolving is used to set the destination IP address of the connection.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
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
    exception_track: str = Field(
        alias="exception-track",
        description="""Determines if an action specified in the Action 2 and CVP categories taken as a result of a resource definition is logged.""",
    )
    match: SmtpMatchObjectRequest = Field(
        alias="match", description="""Set the Match properties for the SMTP resource."""
    )
    action_1: SmtpAction1Request = Field(
        alias="action-1",
        description="""Use the Rewriting Rules to rewrite Sender and Recipient headers in emails, you can also rewrite other email headers by using the custom header field.""",
    )
    action_2: SmtpAction2Request = Field(
        alias="action-2",
        description="""Use this window to configure mail inspection for the SMTP Resource.""",
    )
    cvp: CvpObjectRequest = Field(
        alias="cvp", description="""Configure CVP inspection on mail messages."""
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
    tags: add | remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
