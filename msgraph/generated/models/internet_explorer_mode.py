from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .browser_site_list import BrowserSiteList
    from .entity import Entity

from .entity import Entity

@dataclass
class InternetExplorerMode(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of site lists to support Internet Explorer mode.
    site_lists: Optional[List[BrowserSiteList]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InternetExplorerMode:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InternetExplorerMode
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return InternetExplorerMode()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .browser_site_list import BrowserSiteList
        from .entity import Entity

        from .browser_site_list import BrowserSiteList
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "siteLists": lambda n : setattr(self, 'site_lists', n.get_collection_of_object_values(BrowserSiteList)),
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
        writer.write_collection_of_object_values("siteLists", self.site_lists)
    

