from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_inactive_users_query_scope import AccessReviewInactiveUsersQueryScope
    from .access_review_query_scope import AccessReviewQueryScope
    from .principal_resource_memberships_scope import PrincipalResourceMembershipsScope

@dataclass
class AccessReviewScope(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewScope
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewInactiveUsersQueryScope".casefold():
            from .access_review_inactive_users_query_scope import AccessReviewInactiveUsersQueryScope

            return AccessReviewInactiveUsersQueryScope()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewQueryScope".casefold():
            from .access_review_query_scope import AccessReviewQueryScope

            return AccessReviewQueryScope()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.principalResourceMembershipsScope".casefold():
            from .principal_resource_memberships_scope import PrincipalResourceMembershipsScope

            return PrincipalResourceMembershipsScope()
        return AccessReviewScope()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_inactive_users_query_scope import AccessReviewInactiveUsersQueryScope
        from .access_review_query_scope import AccessReviewQueryScope
        from .principal_resource_memberships_scope import PrincipalResourceMembershipsScope

        from .access_review_inactive_users_query_scope import AccessReviewInactiveUsersQueryScope
        from .access_review_query_scope import AccessReviewQueryScope
        from .principal_resource_memberships_scope import PrincipalResourceMembershipsScope

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

