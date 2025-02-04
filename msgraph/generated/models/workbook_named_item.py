from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .json import Json
    from .workbook_worksheet import WorkbookWorksheet

from .entity import Entity

@dataclass
class WorkbookNamedItem(Entity):
    # Represents the comment associated with this name.
    comment: Optional[str] = None
    # The name of the object. Read-only.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether the name is scoped to the workbook or to a specific worksheet. Read-only.
    scope: Optional[str] = None
    # Indicates what type of reference is associated with the name. The possible values are: String, Integer, Double, Boolean, Range. Read-only.
    type: Optional[str] = None
    # Represents the formula that the name is defined to refer to. E.g. =Sheet14!$B$2:$H$12, =4.75, etc. Read-only.
    value: Optional[Json] = None
    # Specifies whether the object is visible or not.
    visible: Optional[bool] = None
    # Returns the worksheet on which the named item is scoped to. Available only if the item is scoped to the worksheet. Read-only.
    worksheet: Optional[WorkbookWorksheet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookNamedItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookNamedItem
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkbookNamedItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .json import Json
        from .workbook_worksheet import WorkbookWorksheet

        from .entity import Entity
        from .json import Json
        from .workbook_worksheet import WorkbookWorksheet

        fields: Dict[str, Callable[[Any], None]] = {
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_object_value(Json)),
            "visible": lambda n : setattr(self, 'visible', n.get_bool_value()),
            "worksheet": lambda n : setattr(self, 'worksheet', n.get_object_value(WorkbookWorksheet)),
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
        writer.write_str_value("comment", self.comment)
        writer.write_str_value("name", self.name)
        writer.write_str_value("scope", self.scope)
        writer.write_str_value("type", self.type)
        writer.write_object_value("value", self.value)
        writer.write_bool_value("visible", self.visible)
        writer.write_object_value("worksheet", self.worksheet)
    

