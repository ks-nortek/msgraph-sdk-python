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
    from ......models.o_data_errors.o_data_error import ODataError
    from ......models.time_off_reason import TimeOffReason

class TimeOffReasonItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the timeOffReasons property of the microsoft.graph.schedule entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TimeOffReasonItemRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/teams/{team%2Did}/schedule/timeOffReasons/{timeOffReason%2Did}{?%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[TimeOffReasonItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Mark a timeOffReason as inactive by setting the isActive property. Every team must include at least one timeoff reason. This method does not remove the specified timeOffReason instance. timeOffItem instances that have been assigned this reason remain assigned to this reason.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[TimeOffReasonItemRequestBuilderGetRequestConfiguration] = None) -> Optional[TimeOffReason]:
        """
        Retrieve the properties and relationships of a timeOffReason object by ID.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TimeOffReason]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.time_off_reason import TimeOffReason

        return await self.request_adapter.send_async(request_info, TimeOffReason, error_mapping)
    
    async def patch(self,body: Optional[TimeOffReason] = None, request_configuration: Optional[TimeOffReasonItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[TimeOffReason]:
        """
        Replace an existing timeOffReason. If the specified timeOffReason doesn't exist, this method returns 404 Not found.
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TimeOffReason]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.time_off_reason import TimeOffReason

        return await self.request_adapter.send_async(request_info, TimeOffReason, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[TimeOffReasonItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Mark a timeOffReason as inactive by setting the isActive property. Every team must include at least one timeoff reason. This method does not remove the specified timeOffReason instance. timeOffItem instances that have been assigned this reason remain assigned to this reason.
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
    
    def to_get_request_information(self,request_configuration: Optional[TimeOffReasonItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of a timeOffReason object by ID.
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
    
    def to_patch_request_information(self,body: Optional[TimeOffReason] = None, request_configuration: Optional[TimeOffReasonItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Replace an existing timeOffReason. If the specified timeOffReason doesn't exist, this method returns 404 Not found.
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
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class TimeOffReasonItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class TimeOffReasonItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of a timeOffReason object by ID.
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
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class TimeOffReasonItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[TimeOffReasonItemRequestBuilder.TimeOffReasonItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class TimeOffReasonItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

