from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .action_state import ActionState
    from .delete_user_from_shared_apple_device_action_result import DeleteUserFromSharedAppleDeviceActionResult
    from .locate_device_action_result import LocateDeviceActionResult
    from .remote_lock_action_result import RemoteLockActionResult
    from .reset_passcode_action_result import ResetPasscodeActionResult
    from .windows_defender_scan_action_result import WindowsDefenderScanActionResult

@dataclass
class DeviceActionResult(AdditionalDataHolder, BackedModel, Parsable):
    """
    Device action result
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Action name
    action_name: Optional[str] = None
    # State of the action on the device
    action_state: Optional[ActionState] = None
    # Time the action state was last updated
    last_updated_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Time the action was initiated
    start_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceActionResult
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deleteUserFromSharedAppleDeviceActionResult".casefold():
            from .delete_user_from_shared_apple_device_action_result import DeleteUserFromSharedAppleDeviceActionResult

            return DeleteUserFromSharedAppleDeviceActionResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.locateDeviceActionResult".casefold():
            from .locate_device_action_result import LocateDeviceActionResult

            return LocateDeviceActionResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.remoteLockActionResult".casefold():
            from .remote_lock_action_result import RemoteLockActionResult

            return RemoteLockActionResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.resetPasscodeActionResult".casefold():
            from .reset_passcode_action_result import ResetPasscodeActionResult

            return ResetPasscodeActionResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDefenderScanActionResult".casefold():
            from .windows_defender_scan_action_result import WindowsDefenderScanActionResult

            return WindowsDefenderScanActionResult()
        return DeviceActionResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .action_state import ActionState
        from .delete_user_from_shared_apple_device_action_result import DeleteUserFromSharedAppleDeviceActionResult
        from .locate_device_action_result import LocateDeviceActionResult
        from .remote_lock_action_result import RemoteLockActionResult
        from .reset_passcode_action_result import ResetPasscodeActionResult
        from .windows_defender_scan_action_result import WindowsDefenderScanActionResult

        from .action_state import ActionState
        from .delete_user_from_shared_apple_device_action_result import DeleteUserFromSharedAppleDeviceActionResult
        from .locate_device_action_result import LocateDeviceActionResult
        from .remote_lock_action_result import RemoteLockActionResult
        from .reset_passcode_action_result import ResetPasscodeActionResult
        from .windows_defender_scan_action_result import WindowsDefenderScanActionResult

        fields: Dict[str, Callable[[Any], None]] = {
            "actionName": lambda n : setattr(self, 'action_name', n.get_str_value()),
            "actionState": lambda n : setattr(self, 'action_state', n.get_enum_value(ActionState)),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
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
        writer.write_str_value("actionName", self.action_name)
        writer.write_enum_value("actionState", self.action_state)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_additional_data_value(self.additional_data)
    

