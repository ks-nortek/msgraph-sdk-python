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
    from .......models.o_data_errors.o_data_error import ODataError
    from .......models.security.ediscovery_review_set import EdiscoveryReviewSet
    from .microsoft_graph_security_add_to_review_set.microsoft_graph_security_add_to_review_set_request_builder import MicrosoftGraphSecurityAddToReviewSetRequestBuilder
    from .microsoft_graph_security_export.microsoft_graph_security_export_request_builder import MicrosoftGraphSecurityExportRequestBuilder
    from .queries.queries_request_builder import QueriesRequestBuilder

class EdiscoveryReviewSetItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the reviewSets property of the microsoft.graph.security.ediscoveryCase entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EdiscoveryReviewSetItemRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}/reviewSets/{ediscoveryReviewSet%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[EdiscoveryReviewSetItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property reviewSets for security
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[EdiscoveryReviewSetItemRequestBuilderGetRequestConfiguration] = None) -> Optional[EdiscoveryReviewSet]:
        """
        Read the properties and relationships of an ediscoveryReviewSet object.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EdiscoveryReviewSet]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.security.ediscovery_review_set import EdiscoveryReviewSet

        return await self.request_adapter.send_async(request_info, EdiscoveryReviewSet, error_mapping)
    
    async def patch(self,body: Optional[EdiscoveryReviewSet] = None, request_configuration: Optional[EdiscoveryReviewSetItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[EdiscoveryReviewSet]:
        """
        Update the navigation property reviewSets in security
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EdiscoveryReviewSet]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.security.ediscovery_review_set import EdiscoveryReviewSet

        return await self.request_adapter.send_async(request_info, EdiscoveryReviewSet, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[EdiscoveryReviewSetItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property reviewSets for security
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
    
    def to_get_request_information(self,request_configuration: Optional[EdiscoveryReviewSetItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read the properties and relationships of an ediscoveryReviewSet object.
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
    
    def to_patch_request_information(self,body: Optional[EdiscoveryReviewSet] = None, request_configuration: Optional[EdiscoveryReviewSetItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property reviewSets in security
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
    def microsoft_graph_security_add_to_review_set(self) -> MicrosoftGraphSecurityAddToReviewSetRequestBuilder:
        """
        Provides operations to call the addToReviewSet method.
        """
        from .microsoft_graph_security_add_to_review_set.microsoft_graph_security_add_to_review_set_request_builder import MicrosoftGraphSecurityAddToReviewSetRequestBuilder

        return MicrosoftGraphSecurityAddToReviewSetRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_security_export(self) -> MicrosoftGraphSecurityExportRequestBuilder:
        """
        Provides operations to call the export method.
        """
        from .microsoft_graph_security_export.microsoft_graph_security_export_request_builder import MicrosoftGraphSecurityExportRequestBuilder

        return MicrosoftGraphSecurityExportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def queries(self) -> QueriesRequestBuilder:
        """
        Provides operations to manage the queries property of the microsoft.graph.security.ediscoveryReviewSet entity.
        """
        from .queries.queries_request_builder import QueriesRequestBuilder

        return QueriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class EdiscoveryReviewSetItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class EdiscoveryReviewSetItemRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of an ediscoveryReviewSet object.
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
    class EdiscoveryReviewSetItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[EdiscoveryReviewSetItemRequestBuilder.EdiscoveryReviewSetItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class EdiscoveryReviewSetItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

