from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_action_result import DeviceActionResult

from .device_action_result import DeviceActionResult

@dataclass
class DeleteUserFromSharedAppleDeviceActionResult(DeviceActionResult):
    """
    Delete user from shared apple device action result
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # User principal name of the user to be deleted
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeleteUserFromSharedAppleDeviceActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeleteUserFromSharedAppleDeviceActionResult
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeleteUserFromSharedAppleDeviceActionResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_action_result import DeviceActionResult

        from .device_action_result import DeviceActionResult

        fields: Dict[str, Callable[[Any], None]] = {
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

