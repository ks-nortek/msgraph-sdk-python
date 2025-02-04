from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration

from .device_configuration import DeviceConfiguration

@dataclass
class WindowsDefenderAdvancedThreatProtectionConfiguration(DeviceConfiguration):
    """
    Windows Defender AdvancedThreatProtection Configuration.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsDefenderAdvancedThreatProtectionConfiguration"
    # Windows Defender AdvancedThreatProtection 'Allow Sample Sharing' Rule
    allow_sample_sharing: Optional[bool] = None
    # Expedite Windows Defender Advanced Threat Protection telemetry reporting frequency.
    enable_expedited_telemetry_reporting: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsDefenderAdvancedThreatProtectionConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDefenderAdvancedThreatProtectionConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WindowsDefenderAdvancedThreatProtectionConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration

        from .device_configuration import DeviceConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "allowSampleSharing": lambda n : setattr(self, 'allow_sample_sharing', n.get_bool_value()),
            "enableExpeditedTelemetryReporting": lambda n : setattr(self, 'enable_expedited_telemetry_reporting', n.get_bool_value()),
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
        writer.write_bool_value("allowSampleSharing", self.allow_sample_sharing)
        writer.write_bool_value("enableExpeditedTelemetryReporting", self.enable_expedited_telemetry_reporting)
    

