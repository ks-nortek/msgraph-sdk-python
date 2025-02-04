from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .child_selectability import ChildSelectability
    from .tag import Tag

from .tag import Tag

@dataclass
class EdiscoveryReviewTag(Tag):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.ediscoveryReviewTag"
    # Indicates whether a single or multiple child tags can be associated with a document. Possible values are: One, Many.  This value controls whether the UX presents the tags as checkboxes or a radio button group.
    child_selectability: Optional[ChildSelectability] = None
    # Returns the tags that are a child of a tag.
    child_tags: Optional[List[EdiscoveryReviewTag]] = None
    # Returns the parent tag of the specified tag.
    parent: Optional[EdiscoveryReviewTag] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdiscoveryReviewTag:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryReviewTag
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EdiscoveryReviewTag()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .child_selectability import ChildSelectability
        from .tag import Tag

        from .child_selectability import ChildSelectability
        from .tag import Tag

        fields: Dict[str, Callable[[Any], None]] = {
            "childSelectability": lambda n : setattr(self, 'child_selectability', n.get_enum_value(ChildSelectability)),
            "childTags": lambda n : setattr(self, 'child_tags', n.get_collection_of_object_values(EdiscoveryReviewTag)),
            "parent": lambda n : setattr(self, 'parent', n.get_object_value(EdiscoveryReviewTag)),
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
        writer.write_enum_value("childSelectability", self.child_selectability)
        writer.write_collection_of_object_values("childTags", self.child_tags)
        writer.write_object_value("parent", self.parent)
    

