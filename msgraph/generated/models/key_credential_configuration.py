from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_key_credential_restriction_type import AppKeyCredentialRestrictionType

@dataclass
class KeyCredentialConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The maxLifetime property
    max_lifetime: Optional[datetime.timedelta] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Timestamp when the policy is enforced for all apps created on or after the specified date. For existing applications, the enforcement date would be back dated. To apply to all applications regardless of their creation date, this property would be null. Nullable.
    restrict_for_apps_created_after_date_time: Optional[datetime.datetime] = None
    # The type of restriction being applied. Possible values are asymmetricKeyLifetime, unknownFutureValue. Each value of restrictionType can be used only once per policy.
    restriction_type: Optional[AppKeyCredentialRestrictionType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> KeyCredentialConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: KeyCredentialConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return KeyCredentialConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .app_key_credential_restriction_type import AppKeyCredentialRestrictionType

        from .app_key_credential_restriction_type import AppKeyCredentialRestrictionType

        fields: Dict[str, Callable[[Any], None]] = {
            "maxLifetime": lambda n : setattr(self, 'max_lifetime', n.get_timedelta_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "restrictForAppsCreatedAfterDateTime": lambda n : setattr(self, 'restrict_for_apps_created_after_date_time', n.get_datetime_value()),
            "restrictionType": lambda n : setattr(self, 'restriction_type', n.get_enum_value(AppKeyCredentialRestrictionType)),
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
        writer.write_timedelta_value("maxLifetime", self.max_lifetime)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("restrictForAppsCreatedAfterDateTime", self.restrict_for_apps_created_after_date_time)
        writer.write_enum_value("restrictionType", self.restriction_type)
        writer.write_additional_data_value(self.additional_data)
    

