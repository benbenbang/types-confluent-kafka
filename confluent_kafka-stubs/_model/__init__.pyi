from __future__ import annotations

# standard library
from enum import Enum
from typing import ClassVar

from ..cimpl import (
    CONSUMER_GROUP_STATE_COMPLETING_REBALANCE,
    CONSUMER_GROUP_STATE_DEAD,
    CONSUMER_GROUP_STATE_EMPTY,
    CONSUMER_GROUP_STATE_PREPARING_REBALANCE,
    CONSUMER_GROUP_STATE_STABLE,
    CONSUMER_GROUP_STATE_UNKNOWN,
    TopicPartition,
)

class Node:
    id_string: ClassVar[str]

    def __init__(self, id: int, host: str, port: int, rack: str | None = None) -> None: ...

class ConsumerGroupTopicPartitions:
    def __init__(self, group_id: str, topic_partitions: list[TopicPartition] | None = None) -> None: ...

class ConsumerGroupState(Enum):
    UNKNOWN = CONSUMER_GROUP_STATE_UNKNOWN
    UNKOWN = UNKNOWN
    PREPARING_REBALANCING = CONSUMER_GROUP_STATE_PREPARING_REBALANCE
    COMPLETING_REBALANCING = CONSUMER_GROUP_STATE_COMPLETING_REBALANCE
    STABLE = CONSUMER_GROUP_STATE_STABLE
    DEAD = CONSUMER_GROUP_STATE_DEAD
    EMPTY = CONSUMER_GROUP_STATE_EMPTY
    def __lt__(self, other): ...
