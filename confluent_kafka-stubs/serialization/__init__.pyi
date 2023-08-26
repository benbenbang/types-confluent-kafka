"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""
from __future__ import annotations

# standard library
from typing import ClassVar

from ..error import KafkaException

class MessageField:
    NONE: str
    KEY: str
    VALUE: str

class SerializationContext:
    topic: ClassVar[str]
    field: ClassVar[str]
    headers: ClassVar[str]

    def __init__(self, topic: str, field: str, headers: list[tuple] | None = None) -> None: ...

class SerializationError(KafkaException): ...

class Serializer:
    def __call__(self, obj: object, ctx: SerializationContext | None = None) -> None: ...

class Deserializer:
    def __call__(self, value: bytes, ctx: SerializationContext | None = None) -> None: ...

class DoubleSerializer(Serializer):
    def __call__(self, obj: object, ctx: SerializationContext | None = None) -> None: ...

class DoubleDeserializer(Deserializer):
    def __call__(self, value: bytes, ctx: SerializationContext | None = None) -> None: ...

class IntegerSerializer(Serializer):
    def __call__(self, obj, ctx: SerializationContext | None = None) -> None: ...

class IntegerDeserializer(Deserializer):
    def __call__(self, value: bytes, ctx: SerializationContext | None = None) -> None: ...

class StringSerializer(Serializer):
    codec: ClassVar[str]

    def __init__(self, codec: str = ...) -> None: ...
    def __call__(self, obj: object, ctx: SerializationContext | None = None) -> None: ...

class StringDeserializer(Deserializer):
    codec: ClassVar[str]

    def __init__(self, codec: str = "utf_8") -> None: ...
    def __call__(self, value: bytes, ctx: SerializationContext | None = None) -> None: ...
