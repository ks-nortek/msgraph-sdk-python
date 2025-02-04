from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
    from ....models.reminder import Reminder

from ....models.base_collection_pagination_count_response import BaseCollectionPaginationCountResponse

@dataclass
class ReminderViewWithStartDateTimeWithEndDateTimeResponse(BaseCollectionPaginationCountResponse):
    # The value property
    value: Optional[List[Reminder]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ReminderViewWithStartDateTimeWithEndDateTimeResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ReminderViewWithStartDateTimeWithEndDateTimeResponse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ReminderViewWithStartDateTimeWithEndDateTimeResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....models.base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
        from ....models.reminder import Reminder

        from ....models.base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
        from ....models.reminder import Reminder

        fields: Dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_collection_of_object_values(Reminder)),
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
        writer.write_collection_of_object_values("value", self.value)
    

