from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_target import AuthenticationMethodTarget

from .authentication_method_target import AuthenticationMethodTarget

@dataclass
class SmsAuthenticationMethodTarget(AuthenticationMethodTarget):
    # Determines if users can use this authentication method to sign in to Azure AD. true if users can use this method for primary authentication, otherwise false.
    is_usable_for_sign_in: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SmsAuthenticationMethodTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SmsAuthenticationMethodTarget
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SmsAuthenticationMethodTarget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_target import AuthenticationMethodTarget

        from .authentication_method_target import AuthenticationMethodTarget

        fields: Dict[str, Callable[[Any], None]] = {
            "isUsableForSignIn": lambda n : setattr(self, 'is_usable_for_sign_in', n.get_bool_value()),
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
        writer.write_bool_value("isUsableForSignIn", self.is_usable_for_sign_in)
    

