"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""
from __future__ import annotations

# standard library
from typing import Callable

from .cimpl import KafkaError, Message
from .cimpl import Producer as _ProducerImpl
from .error import KeySerializationError as KeySerializationError
from .error import ValueSerializationError as ValueSerializationError
from .serialization import MessageField as MessageField
from .serialization import SerializationContext as SerializationContext

class SerializingProducer(_ProducerImpl):
    def __init__(self, conf) -> None: ...
    def produce(
        self,
        topic: str,
        key: object | None = None,
        value: object | None = None,
        partition: int = -1,  # type: ignore[override]
        on_delivery: Callable[[KafkaError], Message] | None = None,
        timestamp: float = 0,
        headers: dict[str, bytes | None] | None = None,  # type: ignore[override]
    ) -> None: ...
