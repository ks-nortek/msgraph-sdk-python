from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.teleconference_device_quality import TeleconferenceDeviceQuality

@dataclass
class LogTeleconferenceDeviceQualityPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The quality property
    quality: Optional[TeleconferenceDeviceQuality] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LogTeleconferenceDeviceQualityPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LogTeleconferenceDeviceQualityPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return LogTeleconferenceDeviceQualityPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....models.teleconference_device_quality import TeleconferenceDeviceQuality

        from ....models.teleconference_device_quality import TeleconferenceDeviceQuality

        fields: Dict[str, Callable[[Any], None]] = {
            "quality": lambda n : setattr(self, 'quality', n.get_object_value(TeleconferenceDeviceQuality)),
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
        writer.write_object_value("quality", self.quality)
        writer.write_additional_data_value(self.additional_data)
    

