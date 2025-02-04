from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_log_collection_request import AppLogCollectionRequest
    from .entity import Entity

from .entity import Entity

@dataclass
class MobileAppTroubleshootingEvent(Entity):
    # Indicates collection of App Log Upload Request.
    app_log_collection_requests: Optional[List[AppLogCollectionRequest]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppTroubleshootingEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppTroubleshootingEvent
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MobileAppTroubleshootingEvent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .app_log_collection_request import AppLogCollectionRequest
        from .entity import Entity

        from .app_log_collection_request import AppLogCollectionRequest
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "appLogCollectionRequests": lambda n : setattr(self, 'app_log_collection_requests', n.get_collection_of_object_values(AppLogCollectionRequest)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("appLogCollectionRequests", self.app_log_collection_requests)
    

