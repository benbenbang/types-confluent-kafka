"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""
from __future__ import annotations

from .._model import ConsumerGroupState as ConsumerGroupState
from ..error import KafkaError as KafkaError

class ClusterMetadata:
    cluster_id: str
    controller_id: int
    brokers: dict[int, "BrokerMetadata"]
    topics: dict[str, "TopicMetadata"]
    orig_broker_id: int
    orig_broker_name: str | None

    def __init__(self) -> None: ...

class BrokerMetadata:
    id: int = -1
    host: str | None = None
    port: int = -1

    def __init__(self) -> None: ...

class TopicMetadata:
    topic: str | None
    partitions: dict[int, "PartitionMetadata"]
    error: "KafkaError" | None

    def __init__(self) -> None: ...

class PartitionMetadata:
    id: int
    leader: int
    replicas: list[int]
    isrs: list[int]
    error: "KafkaError" | None

    def __init__(self) -> None: ...

class GroupMember:
    id: str
    client_id: str | None
    client_host: str | None
    metadata: bytes | None
    assignment: bytes | None

    def __init__(self) -> None: ...

class GroupMetadata:
    broker: "BrokerMetadata" | None
    id: str | None
    error: "KafkaError" | None
    state: str | None
    protocol_type: str | None
    protocol: str | None
    members: list[GroupMember] | None

    def __init__(self) -> None: ...
