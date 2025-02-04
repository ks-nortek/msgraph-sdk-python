from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .host import Host

from .host import Host

@dataclass
class Hostname(Host):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.hostname"
    # The company or individual who registered this hostname, from WHOIS data.
    registrant: Optional[str] = None
    # The registrar for this hostname, from WHOIS data.
    registrar: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Hostname:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Hostname
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Hostname()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .host import Host

        from .host import Host

        fields: Dict[str, Callable[[Any], None]] = {
            "registrant": lambda n : setattr(self, 'registrant', n.get_str_value()),
            "registrar": lambda n : setattr(self, 'registrar', n.get_str_value()),
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
        writer.write_str_value("registrant", self.registrant)
        writer.write_str_value("registrar", self.registrar)
    

