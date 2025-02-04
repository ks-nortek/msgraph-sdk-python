from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from ..identity_set import IdentitySet
    from ..result_info import ResultInfo
    from .case_action import CaseAction
    from .case_operation_status import CaseOperationStatus
    from .ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation
    from .ediscovery_estimate_operation import EdiscoveryEstimateOperation
    from .ediscovery_export_operation import EdiscoveryExportOperation
    from .ediscovery_hold_operation import EdiscoveryHoldOperation
    from .ediscovery_index_operation import EdiscoveryIndexOperation
    from .ediscovery_purge_data_operation import EdiscoveryPurgeDataOperation
    from .ediscovery_tag_operation import EdiscoveryTagOperation

from ..entity import Entity

@dataclass
class CaseOperation(Entity):
    # The type of action the operation represents. Possible values are: addToReviewSet,applyTags,contentExport,convertToPdf,estimateStatistics, purgeData
    action: Optional[CaseAction] = None
    # The date and time the operation was completed.
    completed_date_time: Optional[datetime.datetime] = None
    # The user that created the operation.
    created_by: Optional[IdentitySet] = None
    # The date and time the operation was created.
    created_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The progress of the operation.
    percent_progress: Optional[int] = None
    # Contains success and failure-specific result information.
    result_info: Optional[ResultInfo] = None
    # The status of the case operation. Possible values are: notStarted, submissionFailed, running, succeeded, partiallySucceeded, failed.
    status: Optional[CaseOperationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CaseOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CaseOperation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryAddToReviewSetOperation".casefold():
            from .ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation

            return EdiscoveryAddToReviewSetOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryEstimateOperation".casefold():
            from .ediscovery_estimate_operation import EdiscoveryEstimateOperation

            return EdiscoveryEstimateOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryExportOperation".casefold():
            from .ediscovery_export_operation import EdiscoveryExportOperation

            return EdiscoveryExportOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryHoldOperation".casefold():
            from .ediscovery_hold_operation import EdiscoveryHoldOperation

            return EdiscoveryHoldOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryIndexOperation".casefold():
            from .ediscovery_index_operation import EdiscoveryIndexOperation

            return EdiscoveryIndexOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryPurgeDataOperation".casefold():
            from .ediscovery_purge_data_operation import EdiscoveryPurgeDataOperation

            return EdiscoveryPurgeDataOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryTagOperation".casefold():
            from .ediscovery_tag_operation import EdiscoveryTagOperation

            return EdiscoveryTagOperation()
        return CaseOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from ..identity_set import IdentitySet
        from ..result_info import ResultInfo
        from .case_action import CaseAction
        from .case_operation_status import CaseOperationStatus
        from .ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation
        from .ediscovery_estimate_operation import EdiscoveryEstimateOperation
        from .ediscovery_export_operation import EdiscoveryExportOperation
        from .ediscovery_hold_operation import EdiscoveryHoldOperation
        from .ediscovery_index_operation import EdiscoveryIndexOperation
        from .ediscovery_purge_data_operation import EdiscoveryPurgeDataOperation
        from .ediscovery_tag_operation import EdiscoveryTagOperation

        from ..entity import Entity
        from ..identity_set import IdentitySet
        from ..result_info import ResultInfo
        from .case_action import CaseAction
        from .case_operation_status import CaseOperationStatus
        from .ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation
        from .ediscovery_estimate_operation import EdiscoveryEstimateOperation
        from .ediscovery_export_operation import EdiscoveryExportOperation
        from .ediscovery_hold_operation import EdiscoveryHoldOperation
        from .ediscovery_index_operation import EdiscoveryIndexOperation
        from .ediscovery_purge_data_operation import EdiscoveryPurgeDataOperation
        from .ediscovery_tag_operation import EdiscoveryTagOperation

        fields: Dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(CaseAction)),
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "percentProgress": lambda n : setattr(self, 'percent_progress', n.get_int_value()),
            "resultInfo": lambda n : setattr(self, 'result_info', n.get_object_value(ResultInfo)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CaseOperationStatus)),
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
        writer.write_enum_value("action", self.action)
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_int_value("percentProgress", self.percent_progress)
        writer.write_object_value("resultInfo", self.result_info)
        writer.write_enum_value("status", self.status)
    

