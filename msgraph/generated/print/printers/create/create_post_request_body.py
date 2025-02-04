from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.print_certificate_signing_request import PrintCertificateSigningRequest

@dataclass
class CreatePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The certificateSigningRequest property
    certificate_signing_request: Optional[PrintCertificateSigningRequest] = None
    # The connectorId property
    connector_id: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The hasPhysicalDevice property
    has_physical_device: Optional[bool] = None
    # The manufacturer property
    manufacturer: Optional[str] = None
    # The model property
    model: Optional[str] = None
    # The physicalDeviceId property
    physical_device_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CreatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreatePostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CreatePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....models.print_certificate_signing_request import PrintCertificateSigningRequest

        from ....models.print_certificate_signing_request import PrintCertificateSigningRequest

        fields: Dict[str, Callable[[Any], None]] = {
            "certificateSigningRequest": lambda n : setattr(self, 'certificate_signing_request', n.get_object_value(PrintCertificateSigningRequest)),
            "connectorId": lambda n : setattr(self, 'connector_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "hasPhysicalDevice": lambda n : setattr(self, 'has_physical_device', n.get_bool_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "physicalDeviceId": lambda n : setattr(self, 'physical_device_id', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("certificateSigningRequest", self.certificate_signing_request)
        writer.write_str_value("connectorId", self.connector_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("hasPhysicalDevice", self.has_physical_device)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_str_value("physicalDeviceId", self.physical_device_id)
        writer.write_additional_data_value(self.additional_data)
    

