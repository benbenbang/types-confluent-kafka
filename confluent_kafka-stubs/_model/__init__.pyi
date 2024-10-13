"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
from enum import Enum
from typing import ClassVar

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
    UNKNOWN: int
    UNKOWN: int
    PREPARING_REBALANCING: int
    COMPLETING_REBALANCING: int
    STABLE: int
    DEAD: int
    EMPTY: int

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
    READ_UNCOMMITTED: ClassVar[int]
    READ_COMMITTED: ClassVar[int]

    def __lt__(self, other) -> bool: ...
