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

class GetSharePointActivityPagesWithPeriodRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the getSharePointActivityPages method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None, period: Optional[str] = None) -> None:
        """
        Instantiates a new GetSharePointActivityPagesWithPeriodRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            period: Usage: period='{period}'
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/reports/getSharePointActivityPages(period='{period}')", path_parameters)
    
    async def get(self,request_configuration: Optional[GetSharePointActivityPagesWithPeriodRequestBuilderGetRequestConfiguration] = None) -> bytes:
        """
        Invoke function getSharePointActivityPages
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
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
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[GetSharePointActivityPagesWithPeriodRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Invoke function getSharePointActivityPages
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class GetSharePointActivityPagesWithPeriodRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

