from pydantic import BaseModel, Field


class DataLeakPreventionRequestNew(BaseModel):
    open_extension_with_external_app: str | list[str] = Field(
        alias="open-extension-with-external-app",
        description="""Open the following extensions from your app with external apps when they cannot be opened with Capsule viewer.""",
    )
    share_protected_extension: str | list[str] = Field(
        alias="share-protected-extension",
        description="""Share protected files extensions to external apps.""",
    )
    share_unprotected_extension: str | list[str] = Field(
        alias="share-unprotected-extension",
        description="""Share unprotected files extensions to external apps.""",
    )
    allow_copy_paste: bool = Field(
        alias="allow-copy-paste", description="""Allow copy paste of mail content."""
    )
    block_forward_attachments: bool = Field(
        alias="block-forward-attachments",
        description="""Allow share mail attachments with external mails.""",
    )
    block_screenshot: bool = Field(
        alias="block-screenshot",
        description="""If true - you can't make a screenshot from your app.""",
    )
    allowed_domains_forward_attachment: str = Field(
        alias="allowed-domains-forward-attachment",
        description="""exclusion of domains which attachments are allowed to be sent, even that shared policy prevents sharing these kinds of attached files - can contain only English characters, digits, comma, spaces and points.""",
    )
    accept_protected_file_extensions: str | list[str] = Field(
        alias="accept-protected-file-extensions",
        description="""Accept protected files with these extensions from external apps to your app.""",
    )
    accept_unprotected_file_extensions: str | list[str] = Field(
        alias="accept-unprotected-file-extensions",
        description="""Accept unprotected files with these extensions from external apps to your app.""",
    )
    allow_import_from_gallery: bool = Field(
        alias="allow-import-from-gallery", description="""Allow import media from gallery."""
    )
    allow_taking_photos_and_videos: bool = Field(
        alias="allow-taking-photos-and-videos",
        description="""Allow the camera to be used from your app.""",
    )
    offer_capsule_as_viewer: bool = Field(
        alias="offer-capsule-as-viewer",
        description="""Offer Capsule as a viewer for external protected documents.""",
    )
