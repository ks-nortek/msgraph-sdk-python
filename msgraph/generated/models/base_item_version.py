from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .document_set_version import DocumentSetVersion
    from .drive_item_version import DriveItemVersion
    from .entity import Entity
    from .identity_set import IdentitySet
    from .list_item_version import ListItemVersion
    from .publication_facet import PublicationFacet

from .entity import Entity

@dataclass
class BaseItemVersion(Entity):
    # Identity of the user which last modified the version. Read-only.
    last_modified_by: Optional[IdentitySet] = None
    # Date and time the version was last modified. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the publication status of this particular version. Read-only.
    publication: Optional[PublicationFacet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BaseItemVersion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BaseItemVersion
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.documentSetVersion".casefold():
            from .document_set_version import DocumentSetVersion

            return DocumentSetVersion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.driveItemVersion".casefold():
            from .drive_item_version import DriveItemVersion

            return DriveItemVersion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.listItemVersion".casefold():
            from .list_item_version import ListItemVersion

            return ListItemVersion()
        return BaseItemVersion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .document_set_version import DocumentSetVersion
        from .drive_item_version import DriveItemVersion
        from .entity import Entity
        from .identity_set import IdentitySet
        from .list_item_version import ListItemVersion
        from .publication_facet import PublicationFacet

        from .document_set_version import DocumentSetVersion
        from .drive_item_version import DriveItemVersion
        from .entity import Entity
        from .identity_set import IdentitySet
        from .list_item_version import ListItemVersion
        from .publication_facet import PublicationFacet

        fields: Dict[str, Callable[[Any], None]] = {
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "publication": lambda n : setattr(self, 'publication', n.get_object_value(PublicationFacet)),
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
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("publication", self.publication)
    

