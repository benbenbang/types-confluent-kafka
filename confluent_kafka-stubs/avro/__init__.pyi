"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

# This module is going to be deprecated

# standard library
from typing import Any, Callable, overload

# pypi/conda library
from confluent_kafka import Consumer as Consumer
from confluent_kafka import Producer as Producer
from confluent_kafka.avro.cached_schema_registry_client import CachedSchemaRegistryClient as CachedSchemaRegistryClient
from confluent_kafka.avro.error import ClientError as ClientError
from confluent_kafka.avro.load import load as load
from confluent_kafka.avro.load import loads as loads
from confluent_kafka.avro.serializer import KeySerializerError as KeySerializerError
from confluent_kafka.avro.serializer import SerializerError as SerializerError
from confluent_kafka.avro.serializer import ValueSerializerError as ValueSerializerError
from confluent_kafka.avro.serializer.message_serializer import MessageSerializer as MessageSerializer
from confluent_kafka.cimpl import Message

class AvroProducer(Producer):
    def __init__(
        self,
        config,
        default_key_schema: Any = None,
        default_value_schema: Any = None,
        schema_registry: Any = None,
        **kwargs
    ) -> None: ...
    def produce(
        self,
        topic: str,
        value: str | bytes | None = None,
        key: str | bytes | None = None,
        partition: int | None = None,
        on_delivery: Callable | None = None,
        timestamp: int = 0,
        headers: dict[str, str | bytes] | list[tuple[str, str | bytes]] | None = None,
    ) -> None: ...

class AvroConsumer(Consumer):
    def __init__(
        self,
        config,
        schema_registry: Any = None,
        reader_key_schema: Any = None,
        reader_value_schema: Any = None,
        **kwargs
    ) -> None: ...
    def poll(self, timeout: int | float | None = None) -> Message: ...
