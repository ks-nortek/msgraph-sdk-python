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
    from .......models.mail_folder import MailFolder
    from .......models.o_data_errors.o_data_error import ODataError
    from .copy.copy_request_builder import CopyRequestBuilder
    from .message_rules.message_rules_request_builder import MessageRulesRequestBuilder
    from .messages.messages_request_builder import MessagesRequestBuilder
    from .move.move_request_builder import MoveRequestBuilder

class MailFolderItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the childFolders property of the microsoft.graph.mailFolder entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new MailFolderItemRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/mailFolders/{mailFolder%2Did}/childFolders/{mailFolder%2Did1}{?includeHiddenFolders*,%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[MailFolderItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property childFolders for users
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
    
    async def get(self,request_configuration: Optional[MailFolderItemRequestBuilderGetRequestConfiguration] = None) -> Optional[MailFolder]:
        """
        The collection of child folders in the mailFolder.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MailFolder]
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
        from .......models.mail_folder import MailFolder

        return await self.request_adapter.send_async(request_info, MailFolder, error_mapping)
    
    async def patch(self,body: Optional[MailFolder] = None, request_configuration: Optional[MailFolderItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[MailFolder]:
        """
        Update the navigation property childFolders in users
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MailFolder]
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
        from .......models.mail_folder import MailFolder

        return await self.request_adapter.send_async(request_info, MailFolder, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[MailFolderItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property childFolders for users
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
    
    def to_get_request_information(self,request_configuration: Optional[MailFolderItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The collection of child folders in the mailFolder.
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
    
    def to_patch_request_information(self,body: Optional[MailFolder] = None, request_configuration: Optional[MailFolderItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property childFolders in users
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
    def copy(self) -> CopyRequestBuilder:
        """
        Provides operations to call the copy method.
        """
        from .copy.copy_request_builder import CopyRequestBuilder

        return CopyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def message_rules(self) -> MessageRulesRequestBuilder:
        """
        Provides operations to manage the messageRules property of the microsoft.graph.mailFolder entity.
        """
        from .message_rules.message_rules_request_builder import MessageRulesRequestBuilder

        return MessageRulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def messages(self) -> MessagesRequestBuilder:
        """
        Provides operations to manage the messages property of the microsoft.graph.mailFolder entity.
        """
        from .messages.messages_request_builder import MessagesRequestBuilder

        return MessagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def move(self) -> MoveRequestBuilder:
        """
        Provides operations to call the move method.
        """
        from .move.move_request_builder import MoveRequestBuilder

        return MoveRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class MailFolderItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class MailFolderItemRequestBuilderGetQueryParameters():
        """
        The collection of child folders in the mailFolder.
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
            if original_name == "include_hidden_folders":
                return "includeHiddenFolders"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Include Hidden Folders
        include_hidden_folders: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class MailFolderItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[MailFolderItemRequestBuilder.MailFolderItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class MailFolderItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

