"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""
from __future__ import annotations

# standard library
from asyncio import Future
from typing import Any

# pypi/conda library
from confluent_kafka._model import ConsumerGroupTopicPartitions

from .._model import ConsumerGroupState
from ..cimpl import (
    CONFIG_SOURCE_DEFAULT_CONFIG,
    CONFIG_SOURCE_DYNAMIC_BROKER_CONFIG,
    CONFIG_SOURCE_DYNAMIC_DEFAULT_BROKER_CONFIG,
    CONFIG_SOURCE_DYNAMIC_TOPIC_CONFIG,
    CONFIG_SOURCE_STATIC_BROKER_CONFIG,
    CONFIG_SOURCE_UNKNOWN_CONFIG,
    RESOURCE_ANY,
    RESOURCE_BROKER,
    RESOURCE_GROUP,
    RESOURCE_TOPIC,
    RESOURCE_UNKNOWN,
    KafkaException,
    NewPartitions,
    NewTopic,
    _AdminClientImpl,
)
from ._acl import AclBinding, AclBindingFilter, AclOperation, AclPermissionType
from ._config import AlterConfigOpType, ConfigEntry, ConfigResource, ConfigSource
from ._group import (
    ConsumerGroupDescription,
    ConsumerGroupListing,
    ListConsumerGroupsResult,
    MemberAssignment,
    MemberDescription,
)
from ._metadata import BrokerMetadata, ClusterMetadata, GroupMember, GroupMetadata, PartitionMetadata, TopicMetadata
from ._resource import ResourcePatternType, ResourceType
from ._scram import (
    ScramCredentialInfo,
    ScramMechanism,
    UserScramCredentialAlteration,
    UserScramCredentialDeletion,
    UserScramCredentialsDescription,
    UserScramCredentialUpsertion,
)

try:
    string_type = basestring  # type: ignore # pyright: ignore
except NameError:
    string_type = str

class AdminClient(_AdminClientImpl):
    def __init__(self, conf: dict[str, Any]) -> None: ...
    def create_topics(
        self,
        new_topics: list["NewTopic"],
        operation_timeout: float = 0,
        request_timeout: float = 1000.0,
        validate_only: bool = False,
    ) -> dict[str, "Future[NewTopic | None]"]: ...
    def delete_topics(
        self, topics: list[str], operation_timeout: float = 0, request_timeout: float = 1000.0
    ) -> dict[str, "Future[NewTopic | None]"]: ...
    def list_topics(self, *args, **kwargs) -> list["TopicMetadata | None"]: ...
    def list_groups(self, *args, **kwargs) -> "ListConsumerGroupsResult | None": ...
    def create_partitions(
        self, new_partitions: list["NewPartitions"], operation_timeout: float = 0, request_timeout: float = 1000.0
    ) -> dict[str, "Future[NewTopic | None]"]: ...
    def describe_configs(
        self, resources: list["ConfigResource"], request_timeout: float = 1000.0
    ) -> dict["ConfigResource", "Future[dict[str, ConfigEntry]]"]: ...
    def alter_configs(
        self, resources: list["ConfigResource"], request_timeout: float = 1000.0, validate_only: bool = False
    ) -> dict["ConfigResource", "Future[None | KafkaException]"]: ...
    def incremental_alter_configs(
        self,
        resources: list["ConfigResource"],
        request_timeout: float = 1000.0,
        validate_only: bool = False,
        broker: int = 0,
    ) -> dict["ConfigResource", "Future[None | KafkaException]"]: ...
    def create_acls(
        self, acls: list["AclBinding"], request_timeout: float = 1000.0, **kwargs
    ) -> dict["AclBinding", "Future[None | KafkaException]"]: ...
    def describe_acls(
        self, acl_binding_filter: "AclBindingFilter", request_timeout: float = 1000.0
    ) -> "Future[list[AclBinding]]": ...
    def delete_acls(
        self, acl_binding_filters: list["AclBindingFilter"], request_timeout: float = 1000.0
    ) -> dict["AclBindingFilter", "Future[dict[AclBindingFilter, list[AclBinding]]]"]: ...
    def list_consumer_groups(
        self, request_timeout: float = 1000.0, states: set["ConsumerGroupState"] | None = None
    ) -> "Future[ListConsumerGroupsResult]": ...
    def describe_consumer_groups(
        self, group_ids: list[str], request_timeout: float = 1000.0
    ) -> dict[str, "Future[dict[str, ConsumerGroupDescription]]"]: ...
    def delete_consumer_groups(
        self, group_ids: list[str], request_timeout: float = 1000.0
    ) -> dict[str, "Future[None]"]: ...
    def list_consumer_group_offsets(
        self,
        list_consumer_group_offsets_request: list["ConsumerGroupTopicPartitions"],
        require_stable: bool = False,
        request_timeout: float = 1000.0,
    ) -> dict[str, "Future[ListConsumerGroupsResult]"]: ...
    def alter_consumer_group_offsets(
        self,
        alter_consumer_group_offsets_request: list["ConsumerGroupTopicPartitions"],
        request_timeout: float = 1000.0,
    ) -> dict[str, "Future[ConsumerGroupTopicPartitions]"]: ...
    def set_sasl_credentials(self, username: str, password: str) -> None: ...
    def describe_user_scram_credentials(
        self, users: list[str], request_timeout: float = 1000.0
    ) -> dict[str, "Future[UserScramCredentialsDescription | KafkaException]"]: ...
    def alter_user_scram_credentials(
        self, alterations: list["UserScramCredentialAlteration"], request_timeout: float = 1000.0
    ) -> dict[str, "Future[None | KafkaException]"]: ...
