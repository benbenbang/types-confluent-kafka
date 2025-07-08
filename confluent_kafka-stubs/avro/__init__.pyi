"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

# This module is going to be deprecated

# standard library
from typing import Any, Callable

from ..avro.cached_schema_registry_client import CachedSchemaRegistryClient as CachedSchemaRegistryClient
from ..avro.error import ClientError as ClientError
from ..avro.load import load as load
from ..avro.load import loads as loads
from ..avro.serializer import KeySerializerError as KeySerializerError
from ..avro.serializer import SerializerError as SerializerError
from ..avro.serializer import ValueSerializerError as ValueSerializerError
from ..avro.serializer.message_serializer import MessageSerializer as MessageSerializer
from ..cimpl import Consumer as Consumer
from ..cimpl import Message
from ..cimpl import Producer as Producer

class AvroProducer(Producer):
    def __init__(
        self,
        config,
        default_key_schema: Any = None,
        default_value_schema: Any = None,
        schema_registry: Any = None,
        **kwargs,
    ) -> None: ...
    def produce(
        self,
        topic: str,
        value: str | bytes | None = None,
        key: str | bytes | None = None,
        partition: int | None = None,
        callback: Callable | None = None,
        on_delivery: Callable | None = None,  # Alias
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
        **kwargs,
    ) -> None: ...
    def poll(self, timeout: int | float | None = None) -> Message: ...
