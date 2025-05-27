"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
from concurrent.futures import Future
from typing import Any

from .._model import ConsumerGroupState, ConsumerGroupTopicPartitions, IsolationLevel
from .._model import TopicCollection as TopicCollection
from ..cimpl import CONFIG_SOURCE_DEFAULT_CONFIG as CONFIG_SOURCE_DEFAULT_CONFIG
from ..cimpl import CONFIG_SOURCE_DYNAMIC_BROKER_CONFIG as CONFIG_SOURCE_DYNAMIC_BROKER_CONFIG
from ..cimpl import CONFIG_SOURCE_DYNAMIC_DEFAULT_BROKER_CONFIG as CONFIG_SOURCE_DYNAMIC_DEFAULT_BROKER_CONFIG
from ..cimpl import CONFIG_SOURCE_DYNAMIC_TOPIC_CONFIG as CONFIG_SOURCE_DYNAMIC_TOPIC_CONFIG
from ..cimpl import CONFIG_SOURCE_STATIC_BROKER_CONFIG as CONFIG_SOURCE_STATIC_BROKER_CONFIG
from ..cimpl import CONFIG_SOURCE_UNKNOWN_CONFIG as CONFIG_SOURCE_UNKNOWN_CONFIG
from ..cimpl import RESOURCE_ANY as RESOURCE_ANY
from ..cimpl import RESOURCE_BROKER as RESOURCE_BROKER
from ..cimpl import RESOURCE_GROUP as RESOURCE_GROUP
from ..cimpl import RESOURCE_TOPIC as RESOURCE_TOPIC
from ..cimpl import RESOURCE_UNKNOWN as RESOURCE_UNKNOWN
from ..cimpl import KafkaException as KafkaException
from ..cimpl import NewPartitions as NewPartitions
from ..cimpl import NewTopic as NewTopic
from ..cimpl import TopicPartition as TopicPartition
from ..cimpl import _AdminClientImpl as _AdminClientImpl
from ._acl import AclBinding as AclBinding
from ._acl import AclBindingFilter as AclBindingFilter
from ._acl import AclOperation as AclOperation
from ._acl import AclPermissionType as AclPermissionType
from ._cluster import DescribeClusterResult as DescribeClusterResult
from ._config import AlterConfigOpType as AlterConfigOpType
from ._config import ConfigEntry as ConfigEntry
from ._config import ConfigResource as ConfigResource
from ._config import ConfigSource as ConfigSource
from ._group import ConsumerGroupDescription as ConsumerGroupDescription
from ._group import ConsumerGroupListing as ConsumerGroupListing
from ._group import ListConsumerGroupsResult as ListConsumerGroupsResult
from ._group import MemberAssignment as MemberAssignment
from ._group import MemberDescription as MemberDescription
from ._listoffsets import ListOffsetsResultInfo as ListOffsetsResultInfo
from ._listoffsets import OffsetSpec as OffsetSpec
from ._metadata import BrokerMetadata as BrokerMetadata
from ._metadata import ClusterMetadata as ClusterMetadata
from ._metadata import GroupMember as GroupMember
from ._metadata import GroupMetadata as GroupMetadata
from ._metadata import PartitionMetadata as PartitionMetadata
from ._metadata import TopicMetadata as TopicMetadata
from ._records import DeletedRecords as DeletedRecords
from ._resource import ResourcePatternType as ResourcePatternType
from ._resource import ResourceType as ResourceType
from ._scram import ScramCredentialInfo as ScramCredentialInfo
from ._scram import ScramMechanism as ScramMechanism
from ._scram import UserScramCredentialAlteration as UserScramCredentialAlteration
from ._scram import UserScramCredentialDeletion as UserScramCredentialDeletion
from ._scram import UserScramCredentialsDescription as UserScramCredentialsDescription
from ._scram import UserScramCredentialUpsertion as UserScramCredentialUpsertion
from ._topic import TopicDescription as TopicDescription

class AdminClient(_AdminClientImpl):
    def __init__(self, conf: dict[str, Any], **kwargs) -> None: ...
    def create_topics(
        self,
        new_topics: list["NewTopic"],
        operation_timeout: float = 0,
        request_timeout: float = 1000.0,
        validate_only: bool = False,
    ) -> dict[str, "Future[None]"]: ...
    def delete_topics(
        self, topics: list[str], operation_timeout: float = 0, request_timeout: float = 1000.0
    ) -> dict[str, "Future[None]"]: ...
    def list_topics(self, topic: str | None = None, timeout: float = -1) -> "ClusterMetadata": ...
    def describe_topics(
        self, topics: TopicCollection, include_authorized_operations: bool = False, request_timeout: float = 1000.0
    ) -> dict[str, Future[TopicDescription]]: ...
    def list_groups(self, *args, **kwargs) -> "ListConsumerGroupsResult | None": ...
    def create_partitions(
        self,
        new_partitions: list["NewPartitions"],
        operation_timeout: float = 0,
        request_timeout: float = 1000.0,
        validate_only: bool = False,
    ) -> dict[str, "Future[None]"]: ...
    def describe_configs(
        self, resources: list["ConfigResource"], request_timeout: float = 1000.0
    ) -> dict["ConfigResource", "Future[dict[str, ConfigEntry]]"]: ...
    def alter_configs(
        self, resources: list["ConfigResource"], request_timeout: float = 1000.0, validate_only: bool = False
    ) -> dict["ConfigResource", "Future[None]"]: ...
    def incremental_alter_configs(
        self,
        resources: list["ConfigResource"],
        request_timeout: float = 1000.0,
        validate_only: bool = False,
        broker: int = 0,
    ) -> dict["ConfigResource", "Future[None]"]: ...
    def create_acls(
        self, acls: list["AclBinding"], request_timeout: float = 1000.0, **kwargs
    ) -> dict["AclBinding", "Future[None]"]: ...
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
    ) -> dict[str, "Future[ConsumerGroupTopicPartitions]"]: ...
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
    ) -> dict[str, "Future[None]"]: ...
    def describe_cluster(
        self, include_authorized_operations: bool = False, request_timeout: float = 1000.0
    ) -> dict[str, Future[DescribeClusterResult]]: ...
    def list_offsets(
        self,
        topic_partition_offsets: dict[TopicPartition, OffsetSpec],
        isolation_level: IsolationLevel,
        request_timeout: float = 1000.0,
    ) -> dict[TopicPartition, Future[ListOffsetsResultInfo]]: ...
    def delete_records(
        self,
        topic_partition_offsets: list[TopicPartition],
        request_timeout: float = 1000.0,
        operation_timeout: float = 1000.0,
    ) -> dict[TopicPartition, Future[DeletedRecords]]: ...
