"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""
from __future__ import annotations

# standard library
from typing import Any, ClassVar

from .._model import ConsumerGroupState as ConsumerGroupState
from ..error import KafkaError as KafkaError

class ClusterMetadata:
    cluster_id: ClassVar[str]
    controller_id: ClassVar[int] = -1
    brokers: ClassVar[dict[int, "BrokerMetadata"] | None] = None
    topics: ClassVar[dict[str, "TopicMetadata"] | None] = None
    orig_broker_id: ClassVar[int] = -1
    orig_broker_name: ClassVar[str] = ""

    def __init__(self) -> None: ...

class BrokerMetadata:
    id: ClassVar[int] = -1
    host: ClassVar[str | None] = None
    port: ClassVar[int] = -1

    def __init__(self) -> None: ...

class TopicMetadata:
    topic: ClassVar[str | None] = None
    partitions: ClassVar[dict[int, "PartitionMetadata"] | None] = None
    error: ClassVar["KafkaError" | None] = None

    def __init__(self) -> None: ...

class PartitionMetadata:
    id: ClassVar[int]
    leader: ClassVar[int]
    replicas: ClassVar[list[int] | None] = None
    isrs: ClassVar[list[int] | None] = None
    error: ClassVar["KafkaError" | None] = None

    def __init__(self) -> None: ...

class GroupMember:
    id: ClassVar[int | None] = None
    client_id: ClassVar[str | None] = None
    client_host: ClassVar[str | None] = None
    metadata: ClassVar[Any | None] = None
    assignment: ClassVar[Any | None] = None

    def __init__(self) -> None: ...

class GroupMetadata:
    broker: ClassVar["BrokerMetadata" | None] = None
    id: ClassVar[str | None] = None
    error: ClassVar["KafkaError" | None] = None
    state: ClassVar["ConsumerGroupState" | None] = None
    protocol_type: ClassVar[Any | None] = None
    protocol: ClassVar[Any] = None
    members: ClassVar[list | None] = None

    def __init__(self) -> None: ...
