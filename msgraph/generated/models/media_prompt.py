from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .media_info import MediaInfo
    from .prompt import Prompt

from .prompt import Prompt

@dataclass
class MediaPrompt(Prompt):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.mediaPrompt"
    # The mediaInfo property
    media_info: Optional[MediaInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MediaPrompt:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MediaPrompt
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MediaPrompt()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .media_info import MediaInfo
        from .prompt import Prompt

        from .media_info import MediaInfo
        from .prompt import Prompt

        fields: Dict[str, Callable[[Any], None]] = {
            "mediaInfo": lambda n : setattr(self, 'media_info', n.get_object_value(MediaInfo)),
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
        writer.write_object_value("mediaInfo", self.media_info)
    

