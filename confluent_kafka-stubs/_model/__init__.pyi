"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""
from __future__ import annotations

# standard library
from enum import Enum
from typing import TYPE_CHECKING, ClassVar, Literal

if TYPE_CHECKING:
    from ..cimpl import TopicPartition

class Node:
    id_string: ClassVar[str]

    def __init__(self, id: int, host: str, port: int, rack: str | None = None) -> None: ...

class ConsumerGroupTopicPartitions:
    def __init__(self, group_id: str, topic_partitions: list["TopicPartition"] | None = None) -> None: ...

class ConsumerGroupState(Enum):
    UNKNOWN = Literal["CONSUMER_GROUP_STATE_UNKNOWN"]
    UNKOWN = Literal["UNKNOWN"]
    PREPARING_REBALANCING = Literal["CONSUMER_GROUP_STATE_PREPARING_REBALANCE"]
    COMPLETING_REBALANCING = Literal["CONSUMER_GROUP_STATE_COMPLETING_REBALANCE"]
    STABLE = Literal["CONSUMER_GROUP_STATE_STABLE"]
    DEAD = Literal["CONSUMER_GROUP_STATE_DEAD"]
    EMPTY = Literal["CONSUMER_GROUP_STATE_EMPTY"]
    def __lt__(self, other) -> bool: ...
