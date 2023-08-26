"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""
from __future__ import annotations

# standard library
import io

# pypi/conda library
from confluent_kafka.serialization import SerializationError as SerializationError

from . import reference_subject_name_strategy as reference_subject_name_strategy
from . import topic_subject_name_strategy as topic_subject_name_strategy
from .schema_registry_client import Schema as Schema
from .schema_registry_client import SchemaReference as SchemaReference
from .schema_registry_client import SchemaRegistryClient

class _ContextStringIO(io.BytesIO):
    def __enter__(self) -> _ContextStringIO: ...
    def __exit__(self, *args): ...

class ProtobufSerializer:
    def __init__(self, msg_type: "GeneratedProtocolMessageType", schema_registry_client: SchemaRegistryClient, conf: dict | None = None) -> None: ...  # type: ignore
    def __call__(self, message: "Message", ctx: "SerializationContext"): ...  # type: ignore

class ProtobufDeserializer:
    def __init__(self, message_type: "MessageType", conf: dict | None = None) -> None: ...  # type: ignore
    def __call__(self, data: bytes, ctx: "SerializationContext"): ...  # type: ignore
