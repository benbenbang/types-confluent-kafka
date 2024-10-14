"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
from typing import Any

from .cimpl import Consumer as _ConsumerImpl
from .cimpl import Message
from .error import ConsumeError as ConsumeError
from .error import KeyDeserializationError as KeyDeserializationError
from .error import ValueDeserializationError as ValueDeserializationError
from .serialization import MessageField as MessageField
from .serialization import SerializationContext as SerializationContext

class DeserializingConsumer(_ConsumerImpl):
    def __init__(self, conf: dict[str, Any]) -> None: ...
    def poll(self, timeout: int | float = -1) -> Message | None: ...  # type: ignore[override]
    def consume(self, num_messages: int = -1, timeout: int | float = -1) -> None: ...  # type: ignore[override]
