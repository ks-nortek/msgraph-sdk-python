from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_feedback import EducationFeedback
    from .education_outcome import EducationOutcome

from .education_outcome import EducationOutcome

@dataclass
class EducationFeedbackOutcome(EducationOutcome):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.educationFeedbackOutcome"
    # Teacher's written feedback to the student.
    feedback: Optional[EducationFeedback] = None
    # A copy of the feedback property that is made when the grade is released to the student.
    published_feedback: Optional[EducationFeedback] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationFeedbackOutcome:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationFeedbackOutcome
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EducationFeedbackOutcome()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .education_feedback import EducationFeedback
        from .education_outcome import EducationOutcome

        from .education_feedback import EducationFeedback
        from .education_outcome import EducationOutcome

        fields: Dict[str, Callable[[Any], None]] = {
            "feedback": lambda n : setattr(self, 'feedback', n.get_object_value(EducationFeedback)),
            "publishedFeedback": lambda n : setattr(self, 'published_feedback', n.get_object_value(EducationFeedback)),
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
        writer.write_object_value("feedback", self.feedback)
        writer.write_object_value("publishedFeedback", self.published_feedback)
    

