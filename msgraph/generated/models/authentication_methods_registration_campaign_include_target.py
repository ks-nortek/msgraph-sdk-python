from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_target_type import AuthenticationMethodTargetType

@dataclass
class AuthenticationMethodsRegistrationCampaignIncludeTarget(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The object identifier of an Azure Active Directory user or group.
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The targetType property
    target_type: Optional[AuthenticationMethodTargetType] = None
    # The authentication method that the user is prompted to register. The value must be microsoftAuthenticator.
    targeted_authentication_method: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationMethodsRegistrationCampaignIncludeTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodsRegistrationCampaignIncludeTarget
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationMethodsRegistrationCampaignIncludeTarget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_target_type import AuthenticationMethodTargetType

        from .authentication_method_target_type import AuthenticationMethodTargetType

        fields: Dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "targetType": lambda n : setattr(self, 'target_type', n.get_enum_value(AuthenticationMethodTargetType)),
            "targetedAuthenticationMethod": lambda n : setattr(self, 'targeted_authentication_method', n.get_str_value()),
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
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("targetType", self.target_type)
        writer.write_str_value("targetedAuthenticationMethod", self.targeted_authentication_method)
        writer.write_additional_data_value(self.additional_data)
    

