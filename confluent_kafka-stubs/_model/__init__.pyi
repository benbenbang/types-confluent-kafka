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
    id: ClassVar[int]
    id_string: ClassVar[str]
    host: ClassVar[str]
    port: ClassVar[int]
    rack: ClassVar[str]

    def __init__(self, id: int, host: str, port: int, rack: str | None = None) -> None: ...

class ConsumerGroupTopicPartitions:
    group_id: ClassVar[str]
    topic_partitions: ClassVar[list["TopicPartition"]]

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
