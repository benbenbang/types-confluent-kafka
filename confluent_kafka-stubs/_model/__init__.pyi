"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
from enum import Enum

from ..cimpl import TopicPartition

class Node:
    id: int
    id_string: str
    host: str
    port: int
    rack: str

    def __init__(self, id: int, host: str, port: int, rack: str | None = None) -> None: ...
    def __str__(self) -> str: ...

class ConsumerGroupTopicPartitions:
    group_id: str
    topic_partitions: list["TopicPartition"]

    def __init__(self, group_id: str, topic_partitions: list["TopicPartition"] | None = None) -> None: ...

class ConsumerGroupState(Enum):
    UNKNOWN = 0
    UNKOWN = 1
    PREPARING_REBALANCING = 2
    COMPLETING_REBALANCING = 3
    STABLE = 4
    DEAD = 5
    EMPTY = 6

    def __lt__(self, other) -> bool: ...

class TopicCollection:
    topic_names: list[str]

    def __init__(self, topic_names: list[str]): ...

class TopicPartitionInfo:
    id: int
    leader: Node
    replicas: list[Node]
    isr: list[Node]

    def __init__(self, id: int, leader: Node, replicas: list[Node], isr: list[Node]): ...

class IsolationLevel(Enum):
    READ_UNCOMMITTED = 0
    READ_COMMITTED = 1

    def __lt__(self, other) -> bool: ...
