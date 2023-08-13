"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

# pypi/conda library
import admin
import kafkatest

from ._model import ConsumerGroupState, ConsumerGroupTopicPartitions, Node
from .cimpl import version  # pyright: ignore
from .cimpl import (
    OFFSET_BEGINNING,
    OFFSET_END,
    OFFSET_INVALID,
    OFFSET_STORED,
    TIMESTAMP_CREATE_TIME,
    TIMESTAMP_LOG_APPEND_TIME,
    TIMESTAMP_NOT_AVAILABLE,
    Consumer,
    KafkaError,
    KafkaException,
    Message,
    Producer,
    TopicPartition,
    libversion,
)
from .deserializing_consumer import DeserializingConsumer
from .serializing_producer import SerializingProducer

__all__ = [
    "admin",
    "Consumer",
    "KafkaError",
    "KafkaException",
    "kafkatest",
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
    "TopicPartition",
    "Node",
    "ConsumerGroupTopicPartitions",
    "ConsumerGroupState",
]

__version__: str
