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
    from .....models.o_data_errors.o_data_error import ODataError
    from .....models.synchronization_secret_key_string_value_pair import SynchronizationSecretKeyStringValuePair
    from .count.count_request_builder import CountRequestBuilder

class SecretsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /applications/{application-id}/synchronization/secrets
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SecretsRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/applications/{application%2Did}/synchronization/secrets", path_parameters)
    
    async def put(self,body: Optional[List[SynchronizationSecretKeyStringValuePair]] = None, request_configuration: Optional[SecretsRequestBuilderPutRequestConfiguration] = None) -> Optional[List[SynchronizationSecretKeyStringValuePair]]:
        """
        Update property secrets value.
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[List[SynchronizationSecretKeyStringValuePair]]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.synchronization_secret_key_string_value_pair import SynchronizationSecretKeyStringValuePair

        return await self.request_adapter.send_collection_async(request_info, SynchronizationSecretKeyStringValuePair, error_mapping)
    
    def to_put_request_information(self,body: Optional[List[SynchronizationSecretKeyStringValuePair]] = None, request_configuration: Optional[SecretsRequestBuilderPutRequestConfiguration] = None) -> RequestInformation:
        """
        Update property secrets value.
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
        request_info.http_method = Method.PUT
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class SecretsRequestBuilderPutRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

