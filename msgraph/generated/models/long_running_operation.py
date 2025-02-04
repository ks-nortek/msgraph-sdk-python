from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .long_running_operation_status import LongRunningOperationStatus
    from .rich_long_running_operation import RichLongRunningOperation

from .entity import Entity

@dataclass
class LongRunningOperation(Entity):
    # The start time of the operation. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The time of the last action in the operation. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_action_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # URI of the resource that the operation is performed on.
    resource_location: Optional[str] = None
    # The status of the operation. The possible values are: notStarted, running, succeeded, failed, unknownFutureValue.
    status: Optional[LongRunningOperationStatus] = None
    # Details about the status of the operation.
    status_detail: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LongRunningOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LongRunningOperation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.richLongRunningOperation".casefold():
            from .rich_long_running_operation import RichLongRunningOperation

            return RichLongRunningOperation()
        return LongRunningOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .long_running_operation_status import LongRunningOperationStatus
        from .rich_long_running_operation import RichLongRunningOperation

        from .entity import Entity
        from .long_running_operation_status import LongRunningOperationStatus
        from .rich_long_running_operation import RichLongRunningOperation

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "resourceLocation": lambda n : setattr(self, 'resource_location', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(LongRunningOperationStatus)),
            "statusDetail": lambda n : setattr(self, 'status_detail', n.get_str_value()),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_str_value("resourceLocation", self.resource_location)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("statusDetail", self.status_detail)
    

