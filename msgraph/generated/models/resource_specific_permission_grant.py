from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_object import DirectoryObject

from .directory_object import DirectoryObject

@dataclass
class ResourceSpecificPermissionGrant(DirectoryObject):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.resourceSpecificPermissionGrant"
    # ID of the service principal of the Azure AD app that has been granted access. Read-only.
    client_app_id: Optional[str] = None
    # ID of the Azure AD app that has been granted access. Read-only.
    client_id: Optional[str] = None
    # The name of the resource-specific permission. Read-only.
    permission: Optional[str] = None
    # The type of permission. Possible values are: Application, Delegated. Read-only.
    permission_type: Optional[str] = None
    # ID of the Azure AD app that is hosting the resource. Read-only.
    resource_app_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ResourceSpecificPermissionGrant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ResourceSpecificPermissionGrant
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ResourceSpecificPermissionGrant()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject

        from .directory_object import DirectoryObject

        fields: Dict[str, Callable[[Any], None]] = {
            "clientAppId": lambda n : setattr(self, 'client_app_id', n.get_str_value()),
            "clientId": lambda n : setattr(self, 'client_id', n.get_str_value()),
            "permission": lambda n : setattr(self, 'permission', n.get_str_value()),
            "permissionType": lambda n : setattr(self, 'permission_type', n.get_str_value()),
            "resourceAppId": lambda n : setattr(self, 'resource_app_id', n.get_str_value()),
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
        writer.write_str_value("clientAppId", self.client_app_id)
        writer.write_str_value("clientId", self.client_id)
        writer.write_str_value("permission", self.permission)
        writer.write_str_value("permissionType", self.permission_type)
        writer.write_str_value("resourceAppId", self.resource_app_id)
    

