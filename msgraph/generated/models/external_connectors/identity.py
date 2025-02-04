from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .identity_type import IdentityType

from ..entity import Entity

@dataclass
class Identity(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The type of identity. Possible values are: user or group for Azure AD identities and externalgroup for groups in an external system.
    type: Optional[IdentityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Identity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Identity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Identity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .identity_type import IdentityType

        from ..entity import Entity
        from .identity_type import IdentityType

        fields: Dict[str, Callable[[Any], None]] = {
            "type": lambda n : setattr(self, 'type', n.get_enum_value(IdentityType)),
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
        writer.write_enum_value("type", self.type)
    

