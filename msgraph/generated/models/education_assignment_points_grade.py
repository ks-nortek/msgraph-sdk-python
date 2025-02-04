from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_assignment_grade import EducationAssignmentGrade

from .education_assignment_grade import EducationAssignmentGrade

@dataclass
class EducationAssignmentPointsGrade(EducationAssignmentGrade):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.educationAssignmentPointsGrade"
    # Number of points a teacher is giving this submission object.
    points: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationAssignmentPointsGrade:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationAssignmentPointsGrade
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EducationAssignmentPointsGrade()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .education_assignment_grade import EducationAssignmentGrade

        from .education_assignment_grade import EducationAssignmentGrade

        fields: Dict[str, Callable[[Any], None]] = {
            "points": lambda n : setattr(self, 'points', n.get_float_value()),
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
        writer.write_float_value("points", self.points)
    

