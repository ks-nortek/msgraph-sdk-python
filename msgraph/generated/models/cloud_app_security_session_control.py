from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_app_security_session_control_type import CloudAppSecuritySessionControlType
    from .conditional_access_session_control import ConditionalAccessSessionControl

from .conditional_access_session_control import ConditionalAccessSessionControl

@dataclass
class CloudAppSecuritySessionControl(ConditionalAccessSessionControl):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.cloudAppSecuritySessionControl"
    # Possible values are: mcasConfigured, monitorOnly, blockDownloads, unknownFutureValue. For more information, see Deploy Conditional Access App Control for featured apps.
    cloud_app_security_type: Optional[CloudAppSecuritySessionControlType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudAppSecuritySessionControl:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudAppSecuritySessionControl
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CloudAppSecuritySessionControl()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_app_security_session_control_type import CloudAppSecuritySessionControlType
        from .conditional_access_session_control import ConditionalAccessSessionControl

        from .cloud_app_security_session_control_type import CloudAppSecuritySessionControlType
        from .conditional_access_session_control import ConditionalAccessSessionControl

        fields: Dict[str, Callable[[Any], None]] = {
            "cloudAppSecurityType": lambda n : setattr(self, 'cloud_app_security_type', n.get_enum_value(CloudAppSecuritySessionControlType)),
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
        writer.write_enum_value("cloudAppSecurityType", self.cloud_app_security_type)
    

