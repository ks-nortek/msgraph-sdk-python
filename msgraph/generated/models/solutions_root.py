from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .booking_business import BookingBusiness
    from .booking_currency import BookingCurrency

@dataclass
class SolutionsRoot(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The bookingBusinesses property
    booking_businesses: Optional[List[BookingBusiness]] = None
    # The bookingCurrencies property
    booking_currencies: Optional[List[BookingCurrency]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SolutionsRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SolutionsRoot
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SolutionsRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .booking_business import BookingBusiness
        from .booking_currency import BookingCurrency

        from .booking_business import BookingBusiness
        from .booking_currency import BookingCurrency

        fields: Dict[str, Callable[[Any], None]] = {
            "bookingBusinesses": lambda n : setattr(self, 'booking_businesses', n.get_collection_of_object_values(BookingBusiness)),
            "bookingCurrencies": lambda n : setattr(self, 'booking_currencies', n.get_collection_of_object_values(BookingCurrency)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("bookingBusinesses", self.booking_businesses)
        writer.write_collection_of_object_values("bookingCurrencies", self.booking_currencies)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

