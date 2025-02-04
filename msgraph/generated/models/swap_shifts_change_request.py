from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .offer_shift_request import OfferShiftRequest

from .offer_shift_request import OfferShiftRequest

@dataclass
class SwapShiftsChangeRequest(OfferShiftRequest):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.swapShiftsChangeRequest"
    # ShiftId for the recipient user with whom the request is to swap.
    recipient_shift_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SwapShiftsChangeRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SwapShiftsChangeRequest
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SwapShiftsChangeRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .offer_shift_request import OfferShiftRequest

        from .offer_shift_request import OfferShiftRequest

        fields: Dict[str, Callable[[Any], None]] = {
            "recipientShiftId": lambda n : setattr(self, 'recipient_shift_id', n.get_str_value()),
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
        writer.write_str_value("recipientShiftId", self.recipient_shift_id)
    

