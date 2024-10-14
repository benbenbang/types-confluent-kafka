"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
from typing import Any

from .._model import ConsumerGroupState as ConsumerGroupState
from ..error import KafkaError as KafkaError

class ClusterMetadata:
    cluster_id: str
    controller_id: int
    brokers: dict[int, "BrokerMetadata"]
    topics: dict[str, "TopicMetadata"]
    orig_broker_id: int = -1
    orig_broker_name: str | None

    def __init__(self) -> None: ...

class BrokerMetadata:
    id: int = -1
    host: str | None
    port: int = -1

    def __init__(self) -> None: ...

class TopicMetadata:
    topic: str | None = None
    partitions: dict[int, "PartitionMetadata"]
    error: "KafkaError" | None

    def __init__(self) -> None: ...

class PartitionMetadata:
    id: int
    leader: int
    replicas: list[int]
    isrs: list[int]
    error: "KafkaError | None"

    def __init__(self) -> None: ...

class GroupMember:
    id: str | None
    client_id: str | None
    client_host: str | None
    metadata: bytes | None
    assignment: bytes | None

    def __init__(self) -> None: ...

class GroupMetadata:
    broker: "BrokerMetadata | None"
    id: str | None
    error: "KafkaError | None"
    state: "ConsumerGroupState | None"
    protocol_type: Any | None
    protocol: Any
    members: list | None

    def __init__(self) -> None: ...
