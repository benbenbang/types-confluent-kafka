"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""
from __future__ import annotations

# standard library
from io import BytesIO
from typing import Any, Callable

from ..serialization import Deserializer as Deserializer
from ..serialization import SerializationContext
from ..serialization import SerializationError as SerializationError
from ..serialization import Serializer as Serializer
from . import Schema as Schema
from . import topic_subject_name_strategy as topic_subject_name_strategy
from .schema_registry_client import SchemaRegistryClient

class _ContextStringIO(BytesIO):
    def __enter__(self) -> _ContextStringIO: ...
    def __exit__(self, *args): ...

class AvroSerializer(Serializer):
    def __init__(
        self,
        schema_registry_client: SchemaRegistryClient,
        schema_str: str | Schema,
        to_dict: Callable[[object, SerializationContext], dict[Any, Any]] | None = None,
        conf: dict | None = None,
    ) -> None: ...
    def __call__(self, obj: object, ctx: SerializationContext) -> None: ...  # type: ignore # issue: https://github.com/confluentinc/confluent-kafka-python/issues/1631

class AvroDeserializer(Deserializer):
    def __init__(
        self,
        schema_registry_client: SchemaRegistryClient,
        schema_str: str | Schema | None = None,
        from_dict: Callable[[dict[Any, Any], SerializationContext], object] | None = None,
        return_record_name: bool = False,
    ) -> None: ...
    def __call__(self, data: bytes, ctx: SerializationContext) -> None: ...  # type: ignore # issue: https://github.com/confluentinc/confluent-kafka-python/issues/1631
