from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teamwork_notification_recipient import TeamworkNotificationRecipient

from .teamwork_notification_recipient import TeamworkNotificationRecipient

@dataclass
class AadUserNotificationRecipient(TeamworkNotificationRecipient):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.aadUserNotificationRecipient"
    # Azure AD user identifier. Use the List users method to get this ID.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AadUserNotificationRecipient:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AadUserNotificationRecipient
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AadUserNotificationRecipient()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .teamwork_notification_recipient import TeamworkNotificationRecipient

        from .teamwork_notification_recipient import TeamworkNotificationRecipient

        fields: Dict[str, Callable[[Any], None]] = {
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_str_value("userId", self.user_id)
    

