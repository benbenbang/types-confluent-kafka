"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
import logging
from types import TracebackType
from typing import Any, Callable, ClassVar

from .admin._metadata import ClusterMetadata

def libversion() -> tuple[str, int]: ...
def version() -> tuple[str, int]: ...

# Constants
ACL_OPERATION_ALL: int
ACL_OPERATION_ALTER: int
ACL_OPERATION_ALTER_CONFIGS: int
ACL_OPERATION_ANY: int
ACL_OPERATION_CLUSTER_ACTION: int
ACL_OPERATION_CREATE: int
ACL_OPERATION_DELETE: int
ACL_OPERATION_DESCRIBE: int
ACL_OPERATION_DESCRIBE_CONFIGS: int
ACL_OPERATION_IDEMPOTENT_WRITE: int
ACL_OPERATION_READ: int
ACL_OPERATION_UNKNOWN: int
ACL_OPERATION_WRITE: int
ACL_PERMISSION_TYPE_ALLOW: int
ACL_PERMISSION_TYPE_ANY: int
ACL_PERMISSION_TYPE_DENY: int
ACL_PERMISSION_TYPE_UNKNOWN: int
CONFIG_SOURCE_DEFAULT_CONFIG: int
CONFIG_SOURCE_DYNAMIC_BROKER_CONFIG: int
CONFIG_SOURCE_DYNAMIC_DEFAULT_BROKER_CONFIG: int
CONFIG_SOURCE_DYNAMIC_TOPIC_CONFIG: int
CONFIG_SOURCE_STATIC_BROKER_CONFIG: int
CONFIG_SOURCE_UNKNOWN_CONFIG: int
CONSUMER_GROUP_STATE_COMPLETING_REBALANCE: int
CONSUMER_GROUP_STATE_DEAD: int
CONSUMER_GROUP_STATE_EMPTY: int
CONSUMER_GROUP_STATE_PREPARING_REBALANCE: int
CONSUMER_GROUP_STATE_STABLE: int
CONSUMER_GROUP_STATE_UNKNOWN: int
OFFSET_BEGINNING: int
OFFSET_END: int
OFFSET_INVALID: int
OFFSET_STORED: int
RESOURCE_ANY: int
RESOURCE_BROKER: int
RESOURCE_GROUP: int
RESOURCE_PATTERN_ANY: int
RESOURCE_PATTERN_LITERAL: int
RESOURCE_PATTERN_MATCH: int
RESOURCE_PATTERN_PREFIXED: int
RESOURCE_PATTERN_UNKNOWN: int
RESOURCE_TOPIC: int
RESOURCE_UNKNOWN: int
TIMESTAMP_CREATE_TIME: int
TIMESTAMP_LOG_APPEND_TIME: int
TIMESTAMP_NOT_AVAILABLE: int

class KafkaError:
    # Class Private Vars
    _ALL_BROKERS_DOWN: ClassVar[int]
    _APPLICATION: ClassVar[int]
    _ASSIGNMENT_LOST: ClassVar[int]
    _ASSIGN_PARTITIONS: ClassVar[int]
    _AUTHENTICATION: ClassVar[int]
    _AUTO_OFFSET_RESET: ClassVar[int]
    _BAD_COMPRESSION: ClassVar[int]
    _BAD_MSG: ClassVar[int]
    _CONFLICT: ClassVar[int]
    _CRIT_SYS_RESOURCE: ClassVar[int]
    _DESTROY: ClassVar[int]
    _EXISTING_SUBSCRIPTION: ClassVar[int]
    _FAIL: ClassVar[int]
    _FATAL: ClassVar[int]
    _FENCED: ClassVar[int]
    _FS: ClassVar[int]
    _GAPLESS_GUARANTEE: ClassVar[int]
    _INCONSISTENT: ClassVar[int]
    _INTR: ClassVar[int]
    _INVALID_ARG: ClassVar[int]
    _INVALID_TYPE: ClassVar[int]
    _IN_PROGRESS: ClassVar[int]
    _ISR_INSUFF: ClassVar[int]
    _KEY_DESERIALIZATION: ClassVar[int]
    _KEY_SERIALIZATION: ClassVar[int]
    _LOG_TRUNCATION: ClassVar[int]
    _MAX_POLL_EXCEEDED: ClassVar[int]
    _MSG_TIMED_OUT: ClassVar[int]
    _NODE_UPDATE: ClassVar[int]
    _NOENT: ClassVar[int]
    _NOOP: ClassVar[int]
    _NOT_CONFIGURED: ClassVar[int]
    _NOT_IMPLEMENTED: ClassVar[int]
    _NO_OFFSET: ClassVar[int]
    _OUTDATED: ClassVar[int]
    _PARTIAL: ClassVar[int]
    _PARTITION_EOF: ClassVar[int]
    _PREV_IN_PROGRESS: ClassVar[int]
    _PURGE_INFLIGHT: ClassVar[int]
    _PURGE_QUEUE: ClassVar[int]
    _QUEUE_FULL: ClassVar[int]
    _READ_ONLY: ClassVar[int]
    _RESOLVE: ClassVar[int]
    _RETRY: ClassVar[int]
    _REVOKE_PARTITIONS: ClassVar[int]
    _SSL: ClassVar[int]
    _STATE: ClassVar[int]
    _TIMED_OUT: ClassVar[int]
    _TIMED_OUT_QUEUE: ClassVar[int]
    _TRANSPORT: ClassVar[int]
    _UNDERFLOW: ClassVar[int]
    _UNKNOWN_BROKER: ClassVar[int]
    _UNKNOWN_GROUP: ClassVar[int]
    _UNKNOWN_PARTITION: ClassVar[int]
    _UNKNOWN_PROTOCOL: ClassVar[int]
    _UNKNOWN_TOPIC: ClassVar[int]
    _UNSUPPORTED_FEATURE: ClassVar[int]
    _VALUE_DESERIALIZATION: ClassVar[int]
    _VALUE_SERIALIZATION: ClassVar[int]
    _WAIT_CACHE: ClassVar[int]
    _WAIT_COORD: ClassVar[int]

    # Class Vars
    BROKER_NOT_AVAILABLE: ClassVar[int]
    CLUSTER_AUTHORIZATION_FAILED: ClassVar[int]
    CONCURRENT_TRANSACTIONS: ClassVar[int]
    COORDINATOR_LOAD_IN_PROGRESS: ClassVar[int]
    COORDINATOR_NOT_AVAILABLE: ClassVar[int]
    DELEGATION_TOKEN_AUTH_DISABLED: ClassVar[int]
    DELEGATION_TOKEN_AUTHORIZATION_FAILED: ClassVar[int]
    DELEGATION_TOKEN_EXPIRED: ClassVar[int]
    DELEGATION_TOKEN_NOT_FOUND: ClassVar[int]
    DELEGATION_TOKEN_OWNER_MISMATCH: ClassVar[int]
    DELEGATION_TOKEN_REQUEST_NOT_ALLOWED: ClassVar[int]
    DUPLICATE_RESOURCE: ClassVar[int]
    DUPLICATE_SEQUENCE_NUMBER: ClassVar[int]
    ELECTION_NOT_NEEDED: ClassVar[int]
    ELIGIBLE_LEADERS_NOT_AVAILABLE: ClassVar[int]
    FEATURE_UPDATE_FAILED: ClassVar[int]
    FENCED_INSTANCE_ID: ClassVar[int]
    FENCED_LEADER_EPOCH: ClassVar[int]
    FETCH_SESSION_ID_NOT_FOUND: ClassVar[int]
    GROUP_AUTHORIZATION_FAILED: ClassVar[int]
    GROUP_ID_NOT_FOUND: ClassVar[int]
    GROUP_MAX_SIZE_REACHED: ClassVar[int]
    GROUP_SUBSCRIBED_TO_TOPIC: ClassVar[int]
    ILLEGAL_GENERATION: ClassVar[int]
    ILLEGAL_SASL_STATE: ClassVar[int]
    INCONSISTENT_GROUP_PROTOCOL: ClassVar[int]
    INCONSISTENT_VOTER_SET: ClassVar[int]
    INVALID_COMMIT_OFFSET_SIZE: ClassVar[int]
    INVALID_CONFIG: ClassVar[int]
    INVALID_FETCH_SESSION_EPOCH: ClassVar[int]
    INVALID_GROUP_ID: ClassVar[int]
    INVALID_MSG: ClassVar[int]
    INVALID_MSG_SIZE: ClassVar[int]
    INVALID_PARTITIONS: ClassVar[int]
    INVALID_PRINCIPAL_TYPE: ClassVar[int]
    INVALID_PRODUCER_EPOCH: ClassVar[int]
    INVALID_PRODUCER_ID_MAPPING: ClassVar[int]
    INVALID_RECORD: ClassVar[int]
    INVALID_REPLICA_ASSIGNMENT: ClassVar[int]
    INVALID_REPLICATION_FACTOR: ClassVar[int]
    INVALID_REQUEST: ClassVar[int]
    INVALID_REQUIRED_ACKS: ClassVar[int]
    INVALID_SESSION_TIMEOUT: ClassVar[int]
    INVALID_TIMESTAMP: ClassVar[int]
    INVALID_TRANSACTION_TIMEOUT: ClassVar[int]
    INVALID_TXN_STATE: ClassVar[int]
    INVALID_UPDATE_VERSION: ClassVar[int]
    KAFKA_STORAGE_ERROR: ClassVar[int]
    LEADER_NOT_AVAILABLE: ClassVar[int]
    LISTENER_NOT_FOUND: ClassVar[int]
    LOG_DIR_NOT_FOUND: ClassVar[int]
    MEMBER_ID_REQUIRED: ClassVar[int]
    MSG_SIZE_TOO_LARGE: ClassVar[int]
    NETWORK_EXCEPTION: ClassVar[int]
    NO_ERROR: ClassVar[int]
    NON_EMPTY_GROUP: ClassVar[int]
    NO_REASSIGNMENT_IN_PROGRESS: ClassVar[int]
    NOT_CONTROLLER: ClassVar[int]
    NOT_COORDINATOR: ClassVar[int]
    NOT_ENOUGH_REPLICAS: ClassVar[int]
    NOT_ENOUGH_REPLICAS_AFTER_APPEND: ClassVar[int]
    NOT_LEADER_FOR_PARTITION: ClassVar[int]
    OFFSET_METADATA_TOO_LARGE: ClassVar[int]
    OFFSET_NOT_AVAILABLE: ClassVar[int]
    OFFSET_OUT_OF_RANGE: ClassVar[int]
    OPERATION_NOT_ATTEMPTED: ClassVar[int]
    OUT_OF_ORDER_SEQUENCE_NUMBER: ClassVar[int]
    POLICY_VIOLATION: ClassVar[int]
    PREFERRED_LEADER_NOT_AVAILABLE: ClassVar[int]
    PRINCIPAL_DESERIALIZATION_FAILURE: ClassVar[int]
    PRODUCER_FENCED: ClassVar[int]
    REASSIGNMENT_IN_PROGRESS: ClassVar[int]
    REBALANCE_IN_PROGRESS: ClassVar[int]
    RECORD_LIST_TOO_LARGE: ClassVar[int]
    REPLICA_NOT_AVAILABLE: ClassVar[int]
    REQUEST_TIMED_OUT: ClassVar[int]
    RESOURCE_NOT_FOUND: ClassVar[int]
    SASL_AUTHENTICATION_FAILED: ClassVar[int]
    SECURITY_DISABLED: ClassVar[int]
    STALE_BROKER_EPOCH: ClassVar[int]
    STALE_CTRL_EPOCH: ClassVar[int]
    THROTTLING_QUOTA_EXCEEDED: ClassVar[int]
    TOPIC_ALREADY_EXISTS: ClassVar[int]
    TOPIC_AUTHORIZATION_FAILED: ClassVar[int]
    TOPIC_DELETION_DISABLED: ClassVar[int]
    TOPIC_EXCEPTION: ClassVar[int]
    TRANSACTIONAL_ID_AUTHORIZATION_FAILED: ClassVar[int]
    TRANSACTION_COORDINATOR_FENCED: ClassVar[int]
    UNACCEPTABLE_CREDENTIAL: ClassVar[int]
    UNKNOWN: ClassVar[int]
    UNKNOWN_LEADER_EPOCH: ClassVar[int]
    UNKNOWN_MEMBER_ID: ClassVar[int]
    UNKNOWN_PRODUCER_ID: ClassVar[int]
    UNKNOWN_TOPIC_OR_PART: ClassVar[int]
    UNSTABLE_OFFSET_COMMIT: ClassVar[int]
    UNSUPPORTED_COMPRESSION_TYPE: ClassVar[int]
    UNSUPPORTED_FOR_MESSAGE_FORMAT: ClassVar[int]
    UNSUPPORTED_SASL_MECHANISM: ClassVar[int]
    UNSUPPORTED_VERSION: ClassVar[int]

    def __init__(
        self,
        error_code: int,
        reason: str | None = None,
        fatal: bool = False,
        retriable: bool = False,
        txn_requires_abort: bool = False,
    ) -> None:
        """
        Note:
            - doc: https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html#kafkaerror
        """
        ...
    def code(self) -> int: ...
    def fatal(self) -> bool: ...
    def name(self) -> str: ...
    def retriable(self) -> bool: ...
    def str(self) -> str: ...
    def txn_requires_abort(self) -> bool: ...
    def __eq__(self, other: "object") -> bool: ...
    def __ge__(self, other: "KafkaError") -> bool: ...
    def __gt__(self, other: "KafkaError") -> bool: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: "KafkaError") -> bool: ...
    def __lt__(self, other: "KafkaError") -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class KafkaException(Exception):
    # Attributes
    args: tuple[str | KafkaError]

    # Methods
    def __init__(self, error: KafkaError | None = None, *args, **kwargs) -> None:
        """
        Note:
            - doc: https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html#kafkaexception
            - Kafka exception that wraps the KafkaError class. Use `exception.args[0]` to extract the `KafkaError` object
        """
        ...
    def add_note(self, note: str) -> None: ...
    def with_traceback(self, traceback: TracebackType | None) -> Any: ...

class _AdminClientImpl:
    """
    Note:
        - doc: https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html#module-confluent_kafka.admin
    """

    def __init__(self, *args, **kwargs) -> None: ...
    def alter_configs(self, *args, **kwargs) -> Any: ...
    def alter_consumer_group_offsets(self, *args, **kwargs) -> Any: ...
    def alter_user_scram_credentials(self, *args, **kwargs) -> Any: ...
    def create_acls(self, *args, **kwargs) -> Any: ...
    def create_partitions(self, *args, **kwargs) -> Any: ...
    def create_topics(self, *args, **kwargs) -> Any: ...
    def delete_acls(self, *args, **kwargs) -> Any: ...
    def delete_consumer_groups(self, *args, **kwargs) -> Any: ...
    def delete_topics(self, *args, **kwargs) -> Any: ...
    def describe_acls(self, *args, **kwargs) -> Any: ...
    def describe_configs(self, *args, **kwargs) -> Any: ...
    def describe_consumer_groups(self, *args, **kwargs) -> Any: ...
    def describe_user_scram_credentials(self, *args, **kwargs) -> Any: ...
    def incremental_alter_configs(self, *args, **kwargs) -> Any: ...
    def list_consumer_group_offsets(self, *args, **kwargs) -> Any: ...
    def list_consumer_groups(self, *args, **kwargs) -> Any: ...
    def list_groups(self, *args, **kwargs) -> Any: ...
    def list_topics(self, *args, **kwargs) -> Any: ...
    def poll(self, *args, **kwargs) -> Any: ...
    def set_sasl_credentials(self, username, password) -> Any: ...
    def __len__(self) -> int: ...

class Message:
    """
    Note:
        doc: https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html#message
    """

    # Methods
    def error(self) -> KafkaError | None: ...
    def headers(self) -> list[tuple[str, bytes]] | None: ...
    def key(self) -> bytes | None: ...
    def latency(self) -> float | None: ...
    def leader_epoch(self) -> int | None: ...
    def offset(self) -> int | None: ...
    def partition(self) -> int | None: ...
    def set_headers(self, value: list[tuple[str, bytes]]) -> None: ...
    def set_key(self, value: bytes | None) -> None: ...
    def set_value(self, value: bytes | None) -> None: ...
    def timestamp(self) -> tuple[int, int]: ...
    def topic(self) -> str | None: ...
    def value(self) -> bytes | None: ...
    def __len__(self) -> int: ...

class NewTopic:
    topic: ClassVar[str]
    num_partitions: ClassVar[int]
    replication_factor: ClassVar[int]
    replica_assignment: ClassVar[list[list[str]]]
    config: ClassVar[dict[str, str] | None]

    def __init__(
        self,
        topic: str,
        num_partitions: int = -1,
        replication_factor: int = -1,
        replica_assignment: list[list[str]] | None = None,
        config: dict[str, str] | None = None,
    ) -> None:
        """
        Note:
            - doc: https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html#newtopic
            - config reference: http://kafka.apache.org/documentation.html#topicconfigs
        """
        def __eq__(self, other: "NewTopic") -> bool: ...
        def __ge__(self, other: "NewTopic") -> bool: ...
        def __gt__(self, other: "NewTopic") -> bool: ...
        def __hash__(self) -> int: ...
        def __le__(self, other: "NewTopic") -> bool: ...
        def __lt__(self, other: "NewTopic") -> bool: ...
        def __ne__(self, other: "NewTopic") -> bool: ...

class NewPartitions:
    def __init__(self, topic: str, new_total_count: int, replica_assignment: list[list[str]] | None = None) -> None:
        """
        Note:
            - doc: https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html#newpartitions
        """
        def __eq__(self, other: "NewPartitions") -> bool: ...
        def __ge__(self, other: "NewPartitions") -> bool: ...
        def __gt__(self, other: "NewPartitions") -> bool: ...
        def __hash__(self) -> int: ...
        def __le__(self, other: "NewPartitions") -> bool: ...
        def __lt__(self, other: "NewPartitions") -> bool: ...
        def __ne__(self, other: "NewPartitions") -> bool: ...

class TopicPartition:
    topic: ClassVar[str]
    partition: ClassVar[int]
    offset: ClassVar[int]
    metadata: ClassVar[str | None]
    leader_epoch: ClassVar[int | None]
    error: ClassVar[KafkaError | None]

    def __init__(
        self,
        topic: str,
        partition: int = -1,
        offset: int = -1001,
        metadata: str | None = None,
        leader_epoch: int | None = None,
    ) -> None:
        """
        Note:
            - doc: https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html#topicpartition
        """
        def __eq__(self, other: "TopicPartition") -> bool: ...
        def __ge__(self, other: "TopicPartition") -> bool: ...
        def __gt__(self, other: "TopicPartition") -> bool: ...
        def __hash__(self) -> int: ...
        def __le__(self, other: "TopicPartition") -> bool: ...
        def __lt__(self, other: "TopicPartition") -> bool: ...
        def __ne__(self, other: "TopicPartition") -> bool: ...

class Producer:
    """
    Note:
        - doc: https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html#producer
        - Asynchronous Kafka Producer
    """

    # Methods
    def __init__(self, config: dict[str, Any], *, logger: logging.Logger = ...) -> None: ...
    def abort_transaction(self, timeout: float | None = None) -> None: ...
    def begin_transaction(self) -> None: ...
    def commit_transaction(self, timeout: float | None = None) -> None:
        """
        Note:
            - timeout unit - second
        """
        ...
    def flush(self, timeout: float | None = None) -> int:
        """
        Note:
            - timeout unit - second
        """
        ...
    def init_transactions(self, timeout: float | None = None) -> None:
        """
        Note:
            - timeout unit - second
        """
        ...
    def list_topics(self, topic: str | None = None, timeout: float = -1) -> Any: ...
    def poll(self, timeout: float | None = None) -> int:
        """
        Note:
            - timeout unit - second
        """
        ...
    def produce(
        self,
        topic: str,
        value: str | bytes | None = None,
        key: str | bytes | None = None,
        partition: int | None = None,
        callback: Callable[[KafkaError | None, Message], None] | None = None,
        on_delivery: Callable[[KafkaError | None, Message], None] | None = None,  # Alias
        timestamp: int = 0,
        headers: dict[str, str | bytes] | list[tuple[str, str | bytes]] | None = None,
    ) -> None: ...
    def purge(self, in_queue: bool = True, in_flight: bool = True, blocking: bool = True) -> None: ...
    def send_offsets_to_transaction(
        self, positions: list[TopicPartition], group_metadata: object, timeout: float | None = None
    ) -> None:
        """
        Note:
            - timeout unit - second
        """
        ...
    def set_sasl_credentials(self, username: str, password: str) -> None: ...
    def __len__(self) -> int: ...

class Consumer:
    def __init__(self, config: dict[str, Any], *, logger: logging.Logger = ...) -> None: ...
    def assign(self, partitions: list[TopicPartition]) -> None: ...
    def assignment(self) -> list[TopicPartition]: ...
    def close(self) -> None: ...
    def commit(
        self,
        message: Message | None = None,
        offsets: list[TopicPartition] | None = None,
        asynchronous: bool = True,
    ) -> list[TopicPartition] | None: ...
    def committed(
        self, partitions: list[TopicPartition], timeout: float | int | None = None
    ) -> list[TopicPartition]: ...
    def consume(self, num_messages: int = 1, timeout: float | int = -1) -> list[Message]: ...
    def consumer_group_metadata(self) -> bytes: ...
    def get_watermark_offsets(
        self, partition: TopicPartition, timeout: float | int | None = None, cached: bool = False
    ) -> tuple[int, int]: ...
    def incremental_assign(self, partitions: list[TopicPartition]) -> None: ...
    def incremental_unassign(self, partitions: list[TopicPartition]) -> None: ...
    def list_topics(self, topic: str | None = None, timeout: float | int = -1) -> ClusterMetadata: ...
    def memberid(self) -> str | None: ...
    def offsets_for_times(
        self, partitions: list[TopicPartition], timeout: float | int | None = None
    ) -> list[TopicPartition]: ...
    def pause(self, partitions: list[TopicPartition]) -> None: ...
    def poll(self, timeout: float | int | None = None) -> Message | None: ...
    def position(self, partitions: list[TopicPartition]) -> list[TopicPartition]: ...
    def resume(self, partitions: list[TopicPartition]) -> None: ...
    def seek(self, partition: TopicPartition) -> None: ...
    def set_sasl_credentials(self, username: str, password: str) -> None: ...
    def store_offsets(self, message: Message | None = None, offsets: list[TopicPartition] | None = None) -> None: ...
    def subscribe(
        self,
        topics: list[str],
        on_assign: Callable[[Consumer, list[TopicPartition]], None] | None = None,
        on_revoke: Callable[[Consumer, list[TopicPartition]], None] | None = None,
        on_lost: Callable[[Consumer, list[TopicPartition]], None] | None = None,
    ) -> None: ...
    def unassign(self) -> None: ...
    def unsubscribe(self) -> None: ...

class Uuid:
    def __repr__(self) -> str: ...
    def __hash__(self) -> int: ...
    def __init__(self, most_significant_bits: int, least_significant_bits: int) -> None: ...
    def get_most_significant_bits(self) -> int: ...
    def get_least_significant_bits(self) -> int: ...
