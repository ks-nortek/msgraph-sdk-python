from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .case_operation import CaseOperation
    from .ediscovery_review_set import EdiscoveryReviewSet
    from .ediscovery_review_set_query import EdiscoveryReviewSetQuery
    from .export_file_metadata import ExportFileMetadata
    from .export_file_structure import ExportFileStructure
    from .export_options import ExportOptions

from .case_operation import CaseOperation

@dataclass
class EdiscoveryExportOperation(CaseOperation):
    # The description provided for the export.
    description: Optional[str] = None
    # The exportFileMetadata property
    export_file_metadata: Optional[List[ExportFileMetadata]] = None
    # The options provided for the export. For more details, see reviewSet: export. Possible values are: originalFiles, text, pdfReplacement,  tags.
    export_options: Optional[ExportOptions] = None
    # The options provided that specify the structure of the export. For more details, see reviewSet: export. Possible values are: none, directory, pst.
    export_structure: Optional[ExportFileStructure] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The name provided for the export.
    output_name: Optional[str] = None
    # Review set from where documents are exported.
    review_set: Optional[EdiscoveryReviewSet] = None
    # The review set query which is used to filter the documents for export.
    review_set_query: Optional[EdiscoveryReviewSetQuery] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdiscoveryExportOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryExportOperation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EdiscoveryExportOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .case_operation import CaseOperation
        from .ediscovery_review_set import EdiscoveryReviewSet
        from .ediscovery_review_set_query import EdiscoveryReviewSetQuery
        from .export_file_metadata import ExportFileMetadata
        from .export_file_structure import ExportFileStructure
        from .export_options import ExportOptions

        from .case_operation import CaseOperation
        from .ediscovery_review_set import EdiscoveryReviewSet
        from .ediscovery_review_set_query import EdiscoveryReviewSetQuery
        from .export_file_metadata import ExportFileMetadata
        from .export_file_structure import ExportFileStructure
        from .export_options import ExportOptions

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "exportFileMetadata": lambda n : setattr(self, 'export_file_metadata', n.get_collection_of_object_values(ExportFileMetadata)),
            "exportOptions": lambda n : setattr(self, 'export_options', n.get_enum_value(ExportOptions)),
            "exportStructure": lambda n : setattr(self, 'export_structure', n.get_enum_value(ExportFileStructure)),
            "outputName": lambda n : setattr(self, 'output_name', n.get_str_value()),
            "reviewSet": lambda n : setattr(self, 'review_set', n.get_object_value(EdiscoveryReviewSet)),
            "reviewSetQuery": lambda n : setattr(self, 'review_set_query', n.get_object_value(EdiscoveryReviewSetQuery)),
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
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("exportFileMetadata", self.export_file_metadata)
        writer.write_enum_value("exportOptions", self.export_options)
        writer.write_enum_value("exportStructure", self.export_structure)
        writer.write_str_value("outputName", self.output_name)
        writer.write_object_value("reviewSet", self.review_set)
        writer.write_object_value("reviewSetQuery", self.review_set_query)
    

