from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_action_result import DeviceActionResult

from .device_action_result import DeviceActionResult

@dataclass
class WindowsDefenderScanActionResult(DeviceActionResult):
    """
    Windows Defender last scan result
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # Scan type either full scan or quick scan
    scan_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsDefenderScanActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDefenderScanActionResult
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WindowsDefenderScanActionResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_action_result import DeviceActionResult

        from .device_action_result import DeviceActionResult

        fields: Dict[str, Callable[[Any], None]] = {
            "scanType": lambda n : setattr(self, 'scan_type', n.get_str_value()),
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
        writer.write_str_value("scanType", self.scan_type)
    

