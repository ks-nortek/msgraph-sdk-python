from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_configuration_setting_item import AppConfigurationSettingItem
    from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration

from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration

@dataclass
class IosMobileAppConfiguration(ManagedDeviceMobileAppConfiguration):
    """
    Contains properties, inherited properties and actions for iOS mobile app configurations.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosMobileAppConfiguration"
    # mdm app configuration Base64 binary.
    encoded_setting_xml: Optional[bytes] = None
    # app configuration setting items.
    settings: Optional[List[AppConfigurationSettingItem]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosMobileAppConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosMobileAppConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IosMobileAppConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .app_configuration_setting_item import AppConfigurationSettingItem
        from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration

        from .app_configuration_setting_item import AppConfigurationSettingItem
        from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "encodedSettingXml": lambda n : setattr(self, 'encoded_setting_xml', n.get_bytes_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_collection_of_object_values(AppConfigurationSettingItem)),
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
        writer.write_bytes_value("encodedSettingXml", self.encoded_setting_xml)
        writer.write_collection_of_object_values("settings", self.settings)
    

