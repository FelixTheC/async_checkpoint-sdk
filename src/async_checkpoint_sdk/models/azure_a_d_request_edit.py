from pydantic import BaseModel, Field


class AzureADRequestEdit(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    authentication_method: str = Field(
        alias="authentication-method",
        description="""<b>user-authentication</b><br>Uses the Azure AD User to authenticate.<br><b>service-principal-authentication</b><br>Uses the Service Principal to authenticate.""",
    )
    password: str = Field(
        alias="password",
        description="""Password of the Azure account.<br><p><font color=red>Required for authentication-method:</font></p>user-authentication.""",
    )
    username: str = Field(
        alias="username",
        description="""An Azure Active Directory user Format<br>&lt;username&gt;@&lt;domain&gt;.<br><p><font color=red>Required for authentication-method:</font></p>user-authentication.""",
    )
    application_id: str = Field(
        alias="application-id",
        description="""The Application ID of the Service Principal, in UUID format.<br><p><font color=red>Required for authentication-method:</font></p>service-principal-authentication.""",
    )
    application_key: str = Field(
        alias="application-key",
        description="""The key created for the Service Principal.<br><p><font color=red>Required for authentication-method:</font></p>service-principal-authentication.""",
    )
    directory_id: str = Field(
        alias="directory-id",
        description="""The Directory ID of the Azure AD, in UUID format.<br><p><font color=red>Required for authentication-method:</font></p>service-principal-authentication.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
    ignore_warnings: bool = Field(
        alias="ignore-warnings",
        description="""Apply changes ignoring warnings. By Setting this parameter to 'true' test connection failure will be ignored.""",
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
