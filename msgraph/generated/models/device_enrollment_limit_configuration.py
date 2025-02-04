from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_enrollment_configuration import DeviceEnrollmentConfiguration

from .device_enrollment_configuration import DeviceEnrollmentConfiguration

@dataclass
class DeviceEnrollmentLimitConfiguration(DeviceEnrollmentConfiguration):
    """
    Device Enrollment Configuration that restricts the number of devices a user can enroll
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceEnrollmentLimitConfiguration"
    # The maximum number of devices that a user can enroll
    limit: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceEnrollmentLimitConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceEnrollmentLimitConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceEnrollmentLimitConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_enrollment_configuration import DeviceEnrollmentConfiguration

        from .device_enrollment_configuration import DeviceEnrollmentConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "limit": lambda n : setattr(self, 'limit', n.get_int_value()),
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
        writer.write_int_value("limit", self.limit)
    

