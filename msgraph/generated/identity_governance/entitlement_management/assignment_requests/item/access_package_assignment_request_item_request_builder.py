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
    from .....models.access_package_assignment_request import AccessPackageAssignmentRequest
    from .....models.o_data_errors.o_data_error import ODataError
    from .access_package.access_package_request_builder import AccessPackageRequestBuilder
    from .assignment.assignment_request_builder import AssignmentRequestBuilder
    from .cancel.cancel_request_builder import CancelRequestBuilder
    from .reprocess.reprocess_request_builder import ReprocessRequestBuilder
    from .requestor.requestor_request_builder import RequestorRequestBuilder
    from .resume.resume_request_builder import ResumeRequestBuilder

class AccessPackageAssignmentRequestItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the assignmentRequests property of the microsoft.graph.entitlementManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AccessPackageAssignmentRequestItemRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/assignmentRequests/{accessPackageAssignmentRequest%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[AccessPackageAssignmentRequestItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete an accessPackageAssignmentRequest object. This request can be made to remove a denied or completed request.  You cannot delete an access package assignment request if it has any accessPackageAssignment objects.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[AccessPackageAssignmentRequestItemRequestBuilderGetRequestConfiguration] = None) -> Optional[AccessPackageAssignmentRequest]:
        """
        In Azure AD entitlement management, retrieve the properties and relationships of an  accessPackageAssignmentRequest object.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessPackageAssignmentRequest]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.access_package_assignment_request import AccessPackageAssignmentRequest

        return await self.request_adapter.send_async(request_info, AccessPackageAssignmentRequest, error_mapping)
    
    async def patch(self,body: Optional[AccessPackageAssignmentRequest] = None, request_configuration: Optional[AccessPackageAssignmentRequestItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[AccessPackageAssignmentRequest]:
        """
        Update the navigation property assignmentRequests in identityGovernance
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessPackageAssignmentRequest]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.access_package_assignment_request import AccessPackageAssignmentRequest

        return await self.request_adapter.send_async(request_info, AccessPackageAssignmentRequest, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[AccessPackageAssignmentRequestItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete an accessPackageAssignmentRequest object. This request can be made to remove a denied or completed request.  You cannot delete an access package assignment request if it has any accessPackageAssignment objects.
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
    
    def to_get_request_information(self,request_configuration: Optional[AccessPackageAssignmentRequestItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        In Azure AD entitlement management, retrieve the properties and relationships of an  accessPackageAssignmentRequest object.
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
    
    def to_patch_request_information(self,body: Optional[AccessPackageAssignmentRequest] = None, request_configuration: Optional[AccessPackageAssignmentRequestItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property assignmentRequests in identityGovernance
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
    def access_package(self) -> AccessPackageRequestBuilder:
        """
        Provides operations to manage the accessPackage property of the microsoft.graph.accessPackageAssignmentRequest entity.
        """
        from .access_package.access_package_request_builder import AccessPackageRequestBuilder

        return AccessPackageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignment(self) -> AssignmentRequestBuilder:
        """
        Provides operations to manage the assignment property of the microsoft.graph.accessPackageAssignmentRequest entity.
        """
        from .assignment.assignment_request_builder import AssignmentRequestBuilder

        return AssignmentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cancel(self) -> CancelRequestBuilder:
        """
        Provides operations to call the cancel method.
        """
        from .cancel.cancel_request_builder import CancelRequestBuilder

        return CancelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reprocess(self) -> ReprocessRequestBuilder:
        """
        Provides operations to call the reprocess method.
        """
        from .reprocess.reprocess_request_builder import ReprocessRequestBuilder

        return ReprocessRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def requestor(self) -> RequestorRequestBuilder:
        """
        Provides operations to manage the requestor property of the microsoft.graph.accessPackageAssignmentRequest entity.
        """
        from .requestor.requestor_request_builder import RequestorRequestBuilder

        return RequestorRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resume(self) -> ResumeRequestBuilder:
        """
        Provides operations to call the resume method.
        """
        from .resume.resume_request_builder import ResumeRequestBuilder

        return ResumeRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AccessPackageAssignmentRequestItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class AccessPackageAssignmentRequestItemRequestBuilderGetQueryParameters():
        """
        In Azure AD entitlement management, retrieve the properties and relationships of an  accessPackageAssignmentRequest object.
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
    class AccessPackageAssignmentRequestItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[AccessPackageAssignmentRequestItemRequestBuilder.AccessPackageAssignmentRequestItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AccessPackageAssignmentRequestItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

