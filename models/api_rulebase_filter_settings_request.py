from api_rulebase_filter_settings_request__packet_search_settings import (
    ApiRulebaseFilterSettingsRequest_PacketSearchSettings,
)
from pydantic import BaseModel, Field


class ApiRulebaseFilterSettingsRequest(BaseModel):
    search_mode: str = Field(
        alias="search-mode",
        description="""When set to 'general', both the Full Text Search and Packet Search are enabled. In this mode, Packet Search will not match on 'Any' object, a negated cell or a group-with-exclusion. When the search-mode is set to 'packet', by default, the match on 'Any' object, a negated cell or a group-with-exclusion are enabled. packet-search-settings may be provided to change the default behavior.""",
    )
    packet_search_settings: ApiRulebaseFilterSettingsRequest_PacketSearchSettings = Field(
        alias="packet-search-settings",
        description="""When 'search-mode' is set to 'packet', this object allows to set the packet search preferences.""",
    )
