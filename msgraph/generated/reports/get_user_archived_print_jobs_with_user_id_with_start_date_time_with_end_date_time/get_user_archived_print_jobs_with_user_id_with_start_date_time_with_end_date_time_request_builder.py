from __future__ import annotations
import datetime
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
    from .get_user_archived_print_jobs_with_user_id_with_start_date_time_with_end_date_time_response import GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeResponse

class GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the getUserArchivedPrintJobs method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None, end_date_time: Optional[datetime.datetime] = None, start_date_time: Optional[datetime.datetime] = None, user_id: Optional[str] = None) -> None:
        """
        Instantiates a new GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeRequestBuilder and sets the default values.
        Args:
            end_date_time: Usage: endDateTime={endDateTime}
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
            start_date_time: Usage: startDateTime={startDateTime}
            user_id: Usage: userId='{userId}'
        """
        super().__init__(request_adapter, "{+baseurl}/reports/getUserArchivedPrintJobs(userId='{userId}',startDateTime={startDateTime},endDateTime={endDateTime}){?%24top,%24skip,%24search,%24filter,%24count}", path_parameters)
    
    async def get(self,request_configuration: Optional[GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeRequestBuilderGetRequestConfiguration] = None) -> Optional[GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeResponse]:
        """
        Invoke function getUserArchivedPrintJobs
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeResponse]
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
        from .get_user_archived_print_jobs_with_user_id_with_start_date_time_with_end_date_time_response import GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeResponse

        return await self.request_adapter.send_async(request_info, GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Invoke function getUserArchivedPrintJobs
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
    
    @dataclass
    class GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeRequestBuilderGetQueryParameters():
        """
        Invoke function getUserArchivedPrintJobs
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
            if original_name == "count":
                return "%24count"
            if original_name == "filter":
                return "%24filter"
            if original_name == "search":
                return "%24search"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeRequestBuilder.GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeRequestBuilderGetQueryParameters] = None

    

