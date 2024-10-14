"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
from io import BytesIO
from typing import Any, Callable

from ..schema_registry import Schema as Schema
from ..schema_registry import topic_subject_name_strategy as topic_subject_name_strategy
from ..schema_registry.schema_registry_client import SchemaRegistryClient
from ..serialization import Deserializer as Deserializer
from ..serialization import SerializationContext
from ..serialization import SerializationError as SerializationError
from ..serialization import Serializer as Serializer

class _ContextStringIO(BytesIO):
    def __enter__(self) -> _ContextStringIO: ...
    def __exit__(self, *args): ...

class JSONSerializer(Serializer):
    def __init__(
        self,
        schema_str: str | Schema,
        schema_registry_client: SchemaRegistryClient,
        to_dict: Callable[[object, SerializationContext], dict[Any, Any]] | None = None,
        conf: dict | None = None,
    ) -> None: ...
    def __call__(self, obj: object, ctx: SerializationContext) -> bytes | None: ...  # type: ignore # issue: https://github.com/confluentinc/confluent-kafka-python/issues/1631

class JSONDeserializer(Deserializer):
    def __init__(
        self,
        schema_str: str | Schema,
        from_dict: Callable[[dict[Any, Any], SerializationContext], object] | None = None,
        schema_registry_client: SchemaRegistryClient | None = None,
    ) -> None: ...
    def __call__(self, data: bytes, ctx: SerializationContext) -> object | dict | None: ...  # type: ignore # issue: https://github.com/confluentinc/confluent-kafka-python/issues/1631
