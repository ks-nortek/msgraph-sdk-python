from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application import Application
    from .service_principal import ServicePrincipal

@dataclass
class ApplicationServicePrincipal(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The application property
    application: Optional[Application] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The servicePrincipal property
    service_principal: Optional[ServicePrincipal] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApplicationServicePrincipal:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApplicationServicePrincipal
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ApplicationServicePrincipal()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .application import Application
        from .service_principal import ServicePrincipal

        from .application import Application
        from .service_principal import ServicePrincipal

        fields: Dict[str, Callable[[Any], None]] = {
            "application": lambda n : setattr(self, 'application', n.get_object_value(Application)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "servicePrincipal": lambda n : setattr(self, 'service_principal', n.get_object_value(ServicePrincipal)),
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
        writer.write_object_value("application", self.application)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("servicePrincipal", self.service_principal)
        writer.write_additional_data_value(self.additional_data)
    

