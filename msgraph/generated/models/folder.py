from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .folder_view import FolderView

@dataclass
class Folder(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Number of children contained immediately within this container.
    child_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of properties defining the recommended view for the folder.
    view: Optional[FolderView] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Folder:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Folder
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Folder()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .folder_view import FolderView

        from .folder_view import FolderView

        fields: Dict[str, Callable[[Any], None]] = {
            "childCount": lambda n : setattr(self, 'child_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "view": lambda n : setattr(self, 'view', n.get_object_value(FolderView)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("childCount", self.child_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("view", self.view)
        writer.write_additional_data_value(self.additional_data)
    

