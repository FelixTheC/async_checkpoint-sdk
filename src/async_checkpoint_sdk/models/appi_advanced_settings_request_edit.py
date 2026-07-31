from .add import add
from .custom_categorization_settings_request import CustomCategorizationSettingsRequest
from .pydantic import BaseModel, Field
from .remove import remove
from .url_filtering_settings_request import UrlFilteringSettingsRequest


class AppiAdvancedSettingsRequestEdit(BaseModel):
    internal_error_fail_mode: str = Field(
        alias="internal-error-fail-mode",
        description="""In case of internal system error, allow or block all connections.<br>This property is not available in the Global domain of an MDS machine.""",
    )
    url_filtering_settings: UrlFilteringSettingsRequest = Field(
        alias="url-filtering-settings",
        description="""In this section user can enable  URL Filtering features.<br>This property is not available in the Global domain of an MDS machine.""",
    )
    web_browsing_services: add | remove | str | list[str] = Field(
        alias="web-browsing-services",
        description="""Web browsing services are the services that match a Web-based custom Application/Site.""",
    )
    match_application_on_any_port: bool = Field(
        alias="match-application-on-any-port",
        description="""Match Web application on 'Any' port when used in Block rule - By default this is set to true. and so applications are matched on all services when used in a Block rule.""",
    )
    enable_web_browsing: bool = Field(
        alias="enable-web-browsing",
        description="""If you do not enable URL Filtering on the Security Gateway, you can use a generic Web browser application called Web Browsing in the rule.<br>This application includes all HTTP traffic that is not a defined application
Application and URL Filtering assigns Web Browsing as the default application for all HTTP traffic that does not match an application in the Application and URL Filtering Database.<br>This property is not available in the Global domain of an MDS machine.""",
    )
    httpi_non_standard_ports: bool = Field(
        alias="httpi-non-standard-ports",
        description="""Enable HTTP inspection on non standard ports for application and URL filtering.<br>This property is not available in the Global domain of an MDS machine.""",
    )
    block_request_when_web_service_is_unavailable: bool = Field(
        alias="block-request-when-web-service-is-unavailable",
        description="""Block requests when the web service is unavailable.
<br>When selected, requests are blocked when there is no connectivity to the Check Point Online Web Service.<br>When cleared, requests are allowed when there is no connectivity.<br>This property is not available in the Global domain of an MDS machine.""",
    )
    website_categorization_mode: str = Field(
        alias="website-categorization-mode",
        description="""Hold - Requests are blocked until categorization is complete.<br>Background - Requests are allowed until categorization is complete.<br>Custom - configure different settings depending on the service -Lets you set different modes for URL Filtering and Social Networking Widgets.<br>This property is not available in the Global domain of an MDS machine.""",
    )
    custom_categorization_settings: CustomCategorizationSettingsRequest = Field(
        alias="custom-categorization-settings",
        description="""Website categorization mode - select the mode that is used for website categorization.<br>This property is not available in the Global domain of an MDS machine.""",
    )
    categorize_social_network_widgets: bool = Field(
        alias="categorize-social-network-widgets",
        description="""When selected, the Security Gateway connects to the Check Point Online Web Service to identify social networking widgets that it does not recognize.<br>When cleared or there is no connectivity between the Security Gateway and the Check Point Online Web, the unknown widget is treated as Web Browsing traffic.<br>This property is not available in the Global domain of an MDS machine.""",
    )
    domain_level_permission: bool = Field(
        alias="domain-level-permission",
        description="""Allows the editing of applications, categories, and services. This property is used only in the Global Domain of an MDS machine.""",
    )
