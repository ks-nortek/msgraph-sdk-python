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
    from .verify_windows_enrollment_auto_discovery_with_domain_name_response import VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameResponse

class VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the verifyWindowsEnrollmentAutoDiscovery method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None, domain_name: Optional[str] = None) -> None:
        """
        Instantiates a new VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder and sets the default values.
        Args:
            domain_name: Usage: domainName='{domainName}'
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/verifyWindowsEnrollmentAutoDiscovery(domainName='{domainName}')", path_parameters)
    
    async def get(self,request_configuration: Optional[VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilderGetRequestConfiguration] = None) -> Optional[VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameResponse]:
        """
        Invoke function verifyWindowsEnrollmentAutoDiscovery
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameResponse]
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
        from .verify_windows_enrollment_auto_discovery_with_domain_name_response import VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameResponse

        return await self.request_adapter.send_async(request_info, VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Invoke function verifyWindowsEnrollmentAutoDiscovery
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
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

