from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .on_premises_directory_synchronization_configuration import OnPremisesDirectorySynchronizationConfiguration
    from .on_premises_directory_synchronization_feature import OnPremisesDirectorySynchronizationFeature

from .entity import Entity

@dataclass
class OnPremisesDirectorySynchronization(Entity):
    # Consists of configurations that can be fine-tuned and impact the on-premises directory synchronization process for a tenant.
    configuration: Optional[OnPremisesDirectorySynchronizationConfiguration] = None
    # The features property
    features: Optional[OnPremisesDirectorySynchronizationFeature] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesDirectorySynchronization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesDirectorySynchronization
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OnPremisesDirectorySynchronization()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .on_premises_directory_synchronization_configuration import OnPremisesDirectorySynchronizationConfiguration
        from .on_premises_directory_synchronization_feature import OnPremisesDirectorySynchronizationFeature

        from .entity import Entity
        from .on_premises_directory_synchronization_configuration import OnPremisesDirectorySynchronizationConfiguration
        from .on_premises_directory_synchronization_feature import OnPremisesDirectorySynchronizationFeature

        fields: Dict[str, Callable[[Any], None]] = {
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(OnPremisesDirectorySynchronizationConfiguration)),
            "features": lambda n : setattr(self, 'features', n.get_object_value(OnPremisesDirectorySynchronizationFeature)),
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
        writer.write_object_value("configuration", self.configuration)
        writer.write_object_value("features", self.features)
    

