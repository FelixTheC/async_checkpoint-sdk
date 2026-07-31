from pydantic import BaseModel, Field


class MailSettingsReply(BaseModel):
    add_customized_text_to_email_body: bool = Field(
        alias="add-customized-text-to-email-body",
        description="""Add customized text to the malicious email body.""",
    )
    add_email_subject_prefix: bool = Field(
        alias="add-email-subject-prefix",
        description="""Add a prefix to the malicious email subject.""",
    )
    add_x_header_to_email: bool = Field(
        alias="add-x-header-to-email", description="""Add an X-Header to the malicious email."""
    )
    email_action: str = Field(
        alias="email-action",
        description="""Block - block the entire malicious email<br>Allow - pass the malicious email and apply email changes (like: remove attachments and links, add x-header, etc...).""",
    )
    email_body_customized_text: str = Field(
        alias="email-body-customized-text",
        description="""Customized text for the malicious email body.<br> Available predefined fields:<br> $verdicts$ - the malicious/error attachments/links verdict.""",
    )
    email_subject_prefix_text: str = Field(
        alias="email-subject-prefix-text", description="""Prefix for the malicious email subject."""
    )
    failed_to_scan_attachments_text: str = Field(
        alias="failed-to-scan-attachments-text",
        description="""Replace attachments that failed to be scanned with this text.<br> Available predefined fields:<br> $filename$ - the malicious file name.<br> $md5$ - MD5 of the malicious file.""",
    )
    malicious_attachments_text: str = Field(
        alias="malicious-attachments-text",
        description="""Replace malicious attachments with this text.<br> Available predefined fields:<br> $filename$ - the malicious file name.<br> $md5$ - MD5 of the malicious file.""",
    )
    malicious_links_text: str = Field(
        alias="malicious-links-text",
        description="""Replace malicious links with this text.<br> Available predefined fields:<br> $neutralized_url$ - neutralized malicious link.""",
    )
    remove_attachments_and_links: bool = Field(
        alias="remove-attachments-and-links",
        description="""Remove attachments and links from the malicious email.""",
    )
    send_copy: bool = Field(
        alias="send-copy",
        description="""Send a copy of the malicious email to the recipient list.""",
    )
    send_copy_list: list[str] = Field(
        alias="send-copy-list",
        description="""Recipient list to send a copy of the malicious email.""",
    )
