"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
import asyncio
from typing import Any, Dict, NamedTuple, Optional, Sequence

from ...cimpl import Message

class MessageBatch(NamedTuple):
    topic: str
    messages: Sequence[Dict[str, Any]]
    futures: Sequence[asyncio.Future[Message]]
    partition: int = -1

    @property
    def size(self) -> int: ...
    @property
    def info(self) -> str: ...

def create_message_batch(
    topic: str,
    messages: Sequence[Dict[str, Any]],
    futures: Sequence[asyncio.Future[Message]],
    callbacks: Optional[Any] = None,
    partition: int = -1,
) -> MessageBatch: ...
