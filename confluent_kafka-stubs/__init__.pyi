"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

from ._model import ConsumerGroupState as ConsumerGroupState
from ._model import ConsumerGroupTopicPartitions as ConsumerGroupTopicPartitions
from ._model import IsolationLevel as IsolationLevel
from ._model import Node as Node
from ._model import TopicCollection as TopicCollection
from ._model import TopicPartitionInfo as TopicPartitionInfo
from .cimpl import OFFSET_BEGINNING as OFFSET_BEGINNING
from .cimpl import OFFSET_END as OFFSET_END
from .cimpl import OFFSET_INVALID as OFFSET_INVALID
from .cimpl import OFFSET_STORED as OFFSET_STORED
from .cimpl import TIMESTAMP_CREATE_TIME as TIMESTAMP_CREATE_TIME
from .cimpl import TIMESTAMP_LOG_APPEND_TIME as TIMESTAMP_LOG_APPEND_TIME
from .cimpl import TIMESTAMP_NOT_AVAILABLE as TIMESTAMP_NOT_AVAILABLE
from .cimpl import Consumer as Consumer
from .cimpl import Message as Message
from .cimpl import Producer as Producer
from .cimpl import TopicPartition as TopicPartition
from .cimpl import libversion as libversion
from .deserializing_consumer import DeserializingConsumer as DeserializingConsumer
from .error import KafkaError as KafkaError
from .error import KafkaException as KafkaException
from .serializing_producer import SerializingProducer as SerializingProducer

__all__ = [
    "admin",  # type: ignore
    "Consumer",
    "KafkaError",
    "KafkaException",
    "kafkatest",  # type: ignore
    "libversion",
    "Message",
    "OFFSET_BEGINNING",
    "OFFSET_END",
    "OFFSET_INVALID",
    "OFFSET_STORED",
    "Producer",
    "DeserializingConsumer",
    "SerializingProducer",
    "TIMESTAMP_CREATE_TIME",
    "TIMESTAMP_LOG_APPEND_TIME",
    "TIMESTAMP_NOT_AVAILABLE",
    "Node",
    "ConsumerGroupTopicPartitions",
    "ConsumerGroupState",
    "TopicPartition",
    "TopicCollection",
    "TopicPartitionInfo",
    "IsolationLevel",
]

__version__: str

class ThrottleEvent:
    def __init__(self, broker_name: str, broker_id: int, throttle_time: float) -> None: ...
