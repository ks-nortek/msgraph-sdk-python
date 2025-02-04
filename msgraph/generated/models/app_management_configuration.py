from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .key_credential_configuration import KeyCredentialConfiguration
    from .password_credential_configuration import PasswordCredentialConfiguration

@dataclass
class AppManagementConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Collection of keyCredential restrictions settings to be applied to an application or service principal.
    key_credentials: Optional[List[KeyCredentialConfiguration]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Collection of password restrictions settings to be applied to an application or service principal.
    password_credentials: Optional[List[PasswordCredentialConfiguration]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppManagementConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppManagementConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AppManagementConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .key_credential_configuration import KeyCredentialConfiguration
        from .password_credential_configuration import PasswordCredentialConfiguration

        from .key_credential_configuration import KeyCredentialConfiguration
        from .password_credential_configuration import PasswordCredentialConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "keyCredentials": lambda n : setattr(self, 'key_credentials', n.get_collection_of_object_values(KeyCredentialConfiguration)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "passwordCredentials": lambda n : setattr(self, 'password_credentials', n.get_collection_of_object_values(PasswordCredentialConfiguration)),
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
        writer.write_collection_of_object_values("keyCredentials", self.key_credentials)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("passwordCredentials", self.password_credentials)
        writer.write_additional_data_value(self.additional_data)
    

