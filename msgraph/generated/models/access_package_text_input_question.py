from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_question import AccessPackageQuestion

from .access_package_question import AccessPackageQuestion

@dataclass
class AccessPackageTextInputQuestion(AccessPackageQuestion):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.accessPackageTextInputQuestion"
    # Indicates whether the answer will be in single or multiple line format.
    is_single_line_question: Optional[bool] = None
    # The regular expression pattern which any answer to this question must match.
    regex_pattern: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageTextInputQuestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageTextInputQuestion
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageTextInputQuestion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_question import AccessPackageQuestion

        from .access_package_question import AccessPackageQuestion

        fields: Dict[str, Callable[[Any], None]] = {
            "isSingleLineQuestion": lambda n : setattr(self, 'is_single_line_question', n.get_bool_value()),
            "regexPattern": lambda n : setattr(self, 'regex_pattern', n.get_str_value()),
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
        writer.write_bool_value("isSingleLineQuestion", self.is_single_line_question)
        writer.write_str_value("regexPattern", self.regex_pattern)
    

