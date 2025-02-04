from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .data_source_container_status import DataSourceContainerStatus
    from .data_source_hold_status import DataSourceHoldStatus
    from .ediscovery_custodian import EdiscoveryCustodian
    from .ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource

from ..entity import Entity

@dataclass
class DataSourceContainer(Entity):
    # Created date and time of the dataSourceContainer entity.
    created_date_time: Optional[datetime.datetime] = None
    # Display name of the dataSourceContainer entity.
    display_name: Optional[str] = None
    # The hold status of the dataSourceContainer. The possible values are: notApplied, applied, applying, removing, partial
    hold_status: Optional[DataSourceHoldStatus] = None
    # Last modified date and time of the dataSourceContainer.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Date and time that the dataSourceContainer was released from the case.
    released_date_time: Optional[datetime.datetime] = None
    # Latest status of the dataSourceContainer. Possible values are: Active, Released.
    status: Optional[DataSourceContainerStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DataSourceContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DataSourceContainer
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryCustodian".casefold():
            from .ediscovery_custodian import EdiscoveryCustodian

            return EdiscoveryCustodian()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryNoncustodialDataSource".casefold():
            from .ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource

            return EdiscoveryNoncustodialDataSource()
        return DataSourceContainer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .data_source_container_status import DataSourceContainerStatus
        from .data_source_hold_status import DataSourceHoldStatus
        from .ediscovery_custodian import EdiscoveryCustodian
        from .ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource

        from ..entity import Entity
        from .data_source_container_status import DataSourceContainerStatus
        from .data_source_hold_status import DataSourceHoldStatus
        from .ediscovery_custodian import EdiscoveryCustodian
        from .ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "holdStatus": lambda n : setattr(self, 'hold_status', n.get_enum_value(DataSourceHoldStatus)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "releasedDateTime": lambda n : setattr(self, 'released_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(DataSourceContainerStatus)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("holdStatus", self.hold_status)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_datetime_value("releasedDateTime", self.released_date_time)
        writer.write_enum_value("status", self.status)
    

