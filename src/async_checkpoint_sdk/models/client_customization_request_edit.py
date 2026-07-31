from .pydantic import BaseModel, Field


class ClientCustomizationRequestEdit(BaseModel):
    app_theme_color_dark: str = Field(
        alias="app-theme-color-dark",
        description="""Configure the application display colors in Dark mode. 6 hex digits that define RGB color - relevant for IOS.""",
    )
    app_theme_color_light: str = Field(
        alias="app-theme-color-light",
        description="""Configure the application display colors in light mode. 6 hex digits that define RGB color - relevant for IOS.""",
    )
    allow_calendar: bool = Field(
        alias="allow-calendar",
        description="""Allow sync business calendar to device calendar.""",
    )
    allow_contacts: bool = Field(
        alias="allow-contacts", description="""Enable/Disable contacts app."""
    )
    allow_mail: bool = Field(alias="allow-mail", description="""Enable/Disable email app.""")
    allow_notes_sync: bool = Field(
        alias="allow-notes-sync",
        description="""Allow sync business notes to device notes.""",
    )
    allow_saved_file_apps: bool = Field(
        alias="allow-saved-file-apps",
        description="""Allow the appearance of 'Saved file app' in the app list.""",
    )
    allow_secure_chat: bool = Field(
        alias="allow-secure-chat",
        description="""Enable/Disable Messages app (depends on Mail app).""",
    )
    allow_tasks: bool = Field(alias="allow-tasks", description="""Enable/Disable Tasks app.""")
    certificate_expire_message: str = Field(
        alias="certificate-expire-message",
        description="""message to show users when certificate is expired - for admin to fill - can contain only English characters, digits, comma, spaces and points.""",
    )
