"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""
from __future__ import annotations

# standard library
from io import BytesIO
from typing import Callable

# pypi/conda library
from confluent_kafka.schema_registry.schema_registry_client import SchemaRegistryClient
from confluent_kafka.serialization import Deserializer as Deserializer
from confluent_kafka.serialization import SerializationError as SerializationError
from confluent_kafka.serialization import Serializer as Serializer

from . import Schema as Schema
from . import topic_subject_name_strategy as topic_subject_name_strategy

class _ContextStringIO(BytesIO):
    def __enter__(self) -> _ContextStringIO: ...
    def __exit__(self, *args): ...

class AvroSerializer(Serializer):
    def __init__(
        self,
        schema_registry_client: SchemaRegistryClient,
        schema_str: str,
        to_dict: Callable[[object], "SerializationContext"] | None = None,  # type: ignore
        conf: dict | None = None,
    ) -> None: ...
    def __call__(self, obj: object, ctx: "SerializationContext"): ...  # type: ignore

class AvroDeserializer(Deserializer):
    def __init__(
        self,
        schema_registry_client: SchemaRegistryClient,
        schema_str: str | None = None,
        from_dict: Callable[[dict], "SerializationContext"] | None = None,  # type: ignore
        return_record_name: bool = False,
    ) -> None: ...
    def __call__(self, data: bytes, ctx: "SerializationContext"): ...  # type: ignore
