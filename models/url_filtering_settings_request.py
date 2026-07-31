from pydantic import BaseModel, Field


class UrlFilteringSettingsRequest(BaseModel):
    categorize_https_websites: bool = Field(
        alias="categorize-https-websites",
        description="""This option lets Application and URL Filtering assign categories to HTTPS sites without activating HTTPS inspection. It assigns a site category based on its domain name and whether the site has a valid certificate. If the server certificate is:<br> Trusted - Application and URL Filtering gets the domain name from the certificate and uses it to categorize the site.<br>Not Trusted - Application and URL Filtering assigns a category based on the IP address.<br>This property is not available in the Global domain of an MDS machine.""",
    )
    enforce_safe_search: bool = Field(
        alias="enforce-safe-search",
        description="""Select this option to require use of the safe search feature in search engines. When activated, the URL Filtering Policy uses the strictest available safe search option for the specified search engine.<br>This option overrides user specified search engine options to block offensive material in search results.<br>This property is not available in the Global domain of an MDS machine.""",
    )
    categorize_cached_and_translated_pages: bool = Field(
        alias="categorize-cached-and-translated-pages",
        description="""Select this option to assign categories to cached search engine results and translated pages.<br>When this option is selected, Application and URL Filtering assigns categories based on the original Web site instead of the 'search engine pages' category.<br>This property is not available in the Global domain of an MDS machine.""",
    )
