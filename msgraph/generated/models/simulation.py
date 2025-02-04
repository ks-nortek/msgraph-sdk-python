from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_identity import EmailIdentity
    from .entity import Entity
    from .payload_delivery_platform import PayloadDeliveryPlatform
    from .simulation_attack_technique import SimulationAttackTechnique
    from .simulation_attack_type import SimulationAttackType
    from .simulation_report import SimulationReport
    from .simulation_status import SimulationStatus

from .entity import Entity

@dataclass
class Simulation(Entity):
    # The social engineering technique used in the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, credentialHarvesting, attachmentMalware, driveByUrl, linkInAttachment, linkToMalwareFile, unknownFutureValue. For more information on the types of social engineering attack techniques, see simulations.
    attack_technique: Optional[SimulationAttackTechnique] = None
    # Attack type of the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, social, cloud, endpoint, unknownFutureValue.
    attack_type: Optional[SimulationAttackType] = None
    # Unique identifier for the attack simulation automation.
    automation_id: Optional[str] = None
    # Date and time of completion of the attack simulation and training campaign. Supports $filter and $orderby.
    completion_date_time: Optional[datetime.datetime] = None
    # Identity of the user who created the attack simulation and training campaign.
    created_by: Optional[EmailIdentity] = None
    # Date and time of creation of the attack simulation and training campaign.
    created_date_time: Optional[datetime.datetime] = None
    # Description of the attack simulation and training campaign.
    description: Optional[str] = None
    # Display name of the attack simulation and training campaign. Supports $filter and $orderby.
    display_name: Optional[str] = None
    # Flag that represents if the attack simulation and training campaign was created from a simulation automation flow. Supports $filter and $orderby.
    is_automated: Optional[bool] = None
    # Identity of the user who most recently modified the attack simulation and training campaign.
    last_modified_by: Optional[EmailIdentity] = None
    # Date and time of the most recent modification of the attack simulation and training campaign.
    last_modified_date_time: Optional[datetime.datetime] = None
    # Date and time of the launch/start of the attack simulation and training campaign. Supports $filter and $orderby.
    launch_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Method of delivery of the phishing payload used in the attack simulation and training campaign. Possible values are: unknown, sms, email, teams, unknownFutureValue.
    payload_delivery_platform: Optional[PayloadDeliveryPlatform] = None
    # Report of the attack simulation and training campaign.
    report: Optional[SimulationReport] = None
    # Status of the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, draft, running, scheduled, succeeded, failed, cancelled, excluded, unknownFutureValue.
    status: Optional[SimulationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Simulation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Simulation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Simulation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .email_identity import EmailIdentity
        from .entity import Entity
        from .payload_delivery_platform import PayloadDeliveryPlatform
        from .simulation_attack_technique import SimulationAttackTechnique
        from .simulation_attack_type import SimulationAttackType
        from .simulation_report import SimulationReport
        from .simulation_status import SimulationStatus

        from .email_identity import EmailIdentity
        from .entity import Entity
        from .payload_delivery_platform import PayloadDeliveryPlatform
        from .simulation_attack_technique import SimulationAttackTechnique
        from .simulation_attack_type import SimulationAttackType
        from .simulation_report import SimulationReport
        from .simulation_status import SimulationStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "attackTechnique": lambda n : setattr(self, 'attack_technique', n.get_enum_value(SimulationAttackTechnique)),
            "attackType": lambda n : setattr(self, 'attack_type', n.get_enum_value(SimulationAttackType)),
            "automationId": lambda n : setattr(self, 'automation_id', n.get_str_value()),
            "completionDateTime": lambda n : setattr(self, 'completion_date_time', n.get_datetime_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(EmailIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isAutomated": lambda n : setattr(self, 'is_automated', n.get_bool_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(EmailIdentity)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "launchDateTime": lambda n : setattr(self, 'launch_date_time', n.get_datetime_value()),
            "payloadDeliveryPlatform": lambda n : setattr(self, 'payload_delivery_platform', n.get_enum_value(PayloadDeliveryPlatform)),
            "report": lambda n : setattr(self, 'report', n.get_object_value(SimulationReport)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SimulationStatus)),
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
        writer.write_enum_value("attackTechnique", self.attack_technique)
        writer.write_enum_value("attackType", self.attack_type)
        writer.write_str_value("automationId", self.automation_id)
        writer.write_datetime_value("completionDateTime", self.completion_date_time)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isAutomated", self.is_automated)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_datetime_value("launchDateTime", self.launch_date_time)
        writer.write_enum_value("payloadDeliveryPlatform", self.payload_delivery_platform)
        writer.write_object_value("report", self.report)
        writer.write_enum_value("status", self.status)
    

