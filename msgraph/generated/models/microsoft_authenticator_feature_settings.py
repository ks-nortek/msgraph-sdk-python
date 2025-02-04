from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_feature_configuration import AuthenticationMethodFeatureConfiguration

@dataclass
class MicrosoftAuthenticatorFeatureSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Determines whether the user's Authenticator app will show them the client app they are signing into.
    display_app_information_required_state: Optional[AuthenticationMethodFeatureConfiguration] = None
    # Determines whether the user's Authenticator app will show them the geographic location of where the authentication request originated from.
    display_location_information_required_state: Optional[AuthenticationMethodFeatureConfiguration] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MicrosoftAuthenticatorFeatureSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftAuthenticatorFeatureSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MicrosoftAuthenticatorFeatureSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_feature_configuration import AuthenticationMethodFeatureConfiguration

        from .authentication_method_feature_configuration import AuthenticationMethodFeatureConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "displayAppInformationRequiredState": lambda n : setattr(self, 'display_app_information_required_state', n.get_object_value(AuthenticationMethodFeatureConfiguration)),
            "displayLocationInformationRequiredState": lambda n : setattr(self, 'display_location_information_required_state', n.get_object_value(AuthenticationMethodFeatureConfiguration)),
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
        writer.write_object_value("displayAppInformationRequiredState", self.display_app_information_required_state)
        writer.write_object_value("displayLocationInformationRequiredState", self.display_location_information_required_state)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

