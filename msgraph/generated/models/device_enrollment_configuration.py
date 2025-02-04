from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_enrollment_limit_configuration import DeviceEnrollmentLimitConfiguration
    from .device_enrollment_platform_restrictions_configuration import DeviceEnrollmentPlatformRestrictionsConfiguration
    from .device_enrollment_windows_hello_for_business_configuration import DeviceEnrollmentWindowsHelloForBusinessConfiguration
    from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceEnrollmentConfiguration(Entity):
    """
    The Base Class of Device Enrollment Configuration
    """
    # The list of group assignments for the device configuration profile
    assignments: Optional[List[EnrollmentConfigurationAssignment]] = None
    # Created date time in UTC of the device enrollment configuration
    created_date_time: Optional[datetime.datetime] = None
    # The description of the device enrollment configuration
    description: Optional[str] = None
    # The display name of the device enrollment configuration
    display_name: Optional[str] = None
    # Last modified date time in UTC of the device enrollment configuration
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Priority is used when a user exists in multiple groups that are assigned enrollment configuration. Users are subject only to the configuration with the lowest priority value.
    priority: Optional[int] = None
    # The version of the device enrollment configuration
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceEnrollmentConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceEnrollmentConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceEnrollmentLimitConfiguration".casefold():
            from .device_enrollment_limit_configuration import DeviceEnrollmentLimitConfiguration

            return DeviceEnrollmentLimitConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceEnrollmentPlatformRestrictionsConfiguration".casefold():
            from .device_enrollment_platform_restrictions_configuration import DeviceEnrollmentPlatformRestrictionsConfiguration

            return DeviceEnrollmentPlatformRestrictionsConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceEnrollmentWindowsHelloForBusinessConfiguration".casefold():
            from .device_enrollment_windows_hello_for_business_configuration import DeviceEnrollmentWindowsHelloForBusinessConfiguration

            return DeviceEnrollmentWindowsHelloForBusinessConfiguration()
        return DeviceEnrollmentConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_enrollment_limit_configuration import DeviceEnrollmentLimitConfiguration
        from .device_enrollment_platform_restrictions_configuration import DeviceEnrollmentPlatformRestrictionsConfiguration
        from .device_enrollment_windows_hello_for_business_configuration import DeviceEnrollmentWindowsHelloForBusinessConfiguration
        from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment
        from .entity import Entity

        from .device_enrollment_limit_configuration import DeviceEnrollmentLimitConfiguration
        from .device_enrollment_platform_restrictions_configuration import DeviceEnrollmentPlatformRestrictionsConfiguration
        from .device_enrollment_windows_hello_for_business_configuration import DeviceEnrollmentWindowsHelloForBusinessConfiguration
        from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(EnrollmentConfigurationAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_int_value("priority", self.priority)
        writer.write_int_value("version", self.version)
    

