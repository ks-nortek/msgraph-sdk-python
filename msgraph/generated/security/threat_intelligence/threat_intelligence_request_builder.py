from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.security.threat_intelligence import ThreatIntelligence
    from .article_indicators.article_indicators_request_builder import ArticleIndicatorsRequestBuilder
    from .articles.articles_request_builder import ArticlesRequestBuilder
    from .host_components.host_components_request_builder import HostComponentsRequestBuilder
    from .host_cookies.host_cookies_request_builder import HostCookiesRequestBuilder
    from .hosts.hosts_request_builder import HostsRequestBuilder
    from .host_trackers.host_trackers_request_builder import HostTrackersRequestBuilder
    from .intelligence_profile_indicators.intelligence_profile_indicators_request_builder import IntelligenceProfileIndicatorsRequestBuilder
    from .intel_profiles.intel_profiles_request_builder import IntelProfilesRequestBuilder
    from .passive_dns_records.passive_dns_records_request_builder import PassiveDnsRecordsRequestBuilder
    from .vulnerabilities.vulnerabilities_request_builder import VulnerabilitiesRequestBuilder

class ThreatIntelligenceRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the threatIntelligence property of the microsoft.graph.security entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ThreatIntelligenceRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/security/threatIntelligence{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[ThreatIntelligenceRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property threatIntelligence for security
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[ThreatIntelligenceRequestBuilderGetRequestConfiguration] = None) -> Optional[ThreatIntelligence]:
        """
        Get threatIntelligence from security
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ThreatIntelligence]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.security.threat_intelligence import ThreatIntelligence

        return await self.request_adapter.send_async(request_info, ThreatIntelligence, error_mapping)
    
    async def patch(self,body: Optional[ThreatIntelligence] = None, request_configuration: Optional[ThreatIntelligenceRequestBuilderPatchRequestConfiguration] = None) -> Optional[ThreatIntelligence]:
        """
        Update the navigation property threatIntelligence in security
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ThreatIntelligence]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.security.threat_intelligence import ThreatIntelligence

        return await self.request_adapter.send_async(request_info, ThreatIntelligence, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ThreatIntelligenceRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property threatIntelligence for security
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[ThreatIntelligenceRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get threatIntelligence from security
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[ThreatIntelligence] = None, request_configuration: Optional[ThreatIntelligenceRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property threatIntelligence in security
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def article_indicators(self) -> ArticleIndicatorsRequestBuilder:
        """
        Provides operations to manage the articleIndicators property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .article_indicators.article_indicators_request_builder import ArticleIndicatorsRequestBuilder

        return ArticleIndicatorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def articles(self) -> ArticlesRequestBuilder:
        """
        Provides operations to manage the articles property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .articles.articles_request_builder import ArticlesRequestBuilder

        return ArticlesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def host_components(self) -> HostComponentsRequestBuilder:
        """
        Provides operations to manage the hostComponents property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .host_components.host_components_request_builder import HostComponentsRequestBuilder

        return HostComponentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def host_cookies(self) -> HostCookiesRequestBuilder:
        """
        Provides operations to manage the hostCookies property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .host_cookies.host_cookies_request_builder import HostCookiesRequestBuilder

        return HostCookiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hosts(self) -> HostsRequestBuilder:
        """
        Provides operations to manage the hosts property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .hosts.hosts_request_builder import HostsRequestBuilder

        return HostsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def host_trackers(self) -> HostTrackersRequestBuilder:
        """
        Provides operations to manage the hostTrackers property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .host_trackers.host_trackers_request_builder import HostTrackersRequestBuilder

        return HostTrackersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def intelligence_profile_indicators(self) -> IntelligenceProfileIndicatorsRequestBuilder:
        """
        Provides operations to manage the intelligenceProfileIndicators property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .intelligence_profile_indicators.intelligence_profile_indicators_request_builder import IntelligenceProfileIndicatorsRequestBuilder

        return IntelligenceProfileIndicatorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def intel_profiles(self) -> IntelProfilesRequestBuilder:
        """
        Provides operations to manage the intelProfiles property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .intel_profiles.intel_profiles_request_builder import IntelProfilesRequestBuilder

        return IntelProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def passive_dns_records(self) -> PassiveDnsRecordsRequestBuilder:
        """
        Provides operations to manage the passiveDnsRecords property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .passive_dns_records.passive_dns_records_request_builder import PassiveDnsRecordsRequestBuilder

        return PassiveDnsRecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vulnerabilities(self) -> VulnerabilitiesRequestBuilder:
        """
        Provides operations to manage the vulnerabilities property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .vulnerabilities.vulnerabilities_request_builder import VulnerabilitiesRequestBuilder

        return VulnerabilitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ThreatIntelligenceRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class ThreatIntelligenceRequestBuilderGetQueryParameters():
        """
        Get threatIntelligence from security
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ThreatIntelligenceRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[ThreatIntelligenceRequestBuilder.ThreatIntelligenceRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ThreatIntelligenceRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

