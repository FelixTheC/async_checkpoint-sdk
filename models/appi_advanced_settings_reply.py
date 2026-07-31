from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from custom_categorization_settings_reply import CustomCategorizationSettingsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field
from url_filtering_settings_reply import UrlFilteringSettingsReply


class AppiAdvancedSettingsReply(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    internal_error_fail_mode: str = Field(
        alias="internal-error-fail-mode",
        description="""In case of internal system error, allow or block all connections.<br>This property is not available in the Global domain of an MDS machine.""",
    )
    url_filtering_settings: UrlFilteringSettingsReply = Field(
        alias="url-filtering-settings",
        description="""In this section user can enable  URL Filtering features.<br>This property is not available in the Global domain of an MDS machine.""",
    )
    web_browsing_services: list[dict] = Field(
        alias="web-browsing-services",
        description="""Web browsing services are the services that match a Web-based custom Application/Site.Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
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
        description="""This option lets Application and URL Filtering assign categories to HTTPS sites without activating HTTPS inspection. It assigns a site category based on its domain name and whether the site has a valid certificate. If the server certificate is:<br> Trusted - Application and URL Filtering gets the domain name from the certificate and uses it to categorize the site.<br>Not Trusted - Application and URL Filtering assigns a category based on the IP address.<br>This property is not available in the Global domain of an MDS machine.""",
    )
    custom_categorization_settings: CustomCategorizationSettingsReply = Field(
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
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
    read_only: bool = Field(
        alias="read-only", description="""Indicates whether the object is read-only."""
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
