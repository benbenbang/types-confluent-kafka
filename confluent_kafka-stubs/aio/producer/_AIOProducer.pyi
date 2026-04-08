"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
import asyncio
import concurrent.futures
from typing import Any

from ...cimpl import Message, TopicPartition

class AIOProducer:
    def __init__(
        self,
        producer_conf: dict[str, Any],
        max_workers: int = 4,
        executor: concurrent.futures.Executor | None = None,
        batch_size: int = 1000,
        buffer_timeout: float = 1.0,
    ) -> None: ...
    async def __aenter__(self) -> AIOProducer: ...
    async def __aexit__(self, *_: Any) -> None: ...
    async def close(self) -> None: ...
    def __del__(self) -> None: ...
    def __len__(self) -> int: ...
    async def poll(self, timeout: float = 0) -> int: ...
    async def produce(
        self,
        topic: str,
        value: str | bytes | None = None,
        key: str | bytes | None = None,
        *,
        partition: int | None = None,
        timestamp: int = 0,
    ) -> asyncio.Future[Message]:
        """
        Note:
            - This is a double-await pattern: ``await produce(...)`` enqueues the message
              and returns an ``asyncio.Future``; awaiting that Future waits for delivery::

                  future = await producer.produce("topic", b"value")
                  message = await future  # blocks until broker confirms delivery

            - Headers are not supported in batch mode; use the synchronous
              ``Producer.produce()`` if headers are required.
        """
        ...
    async def flush(self) -> int: ...
    async def purge(self, in_queue: bool = True, in_flight: bool = True, blocking: bool = True) -> None: ...
    async def list_topics(self, topic: str | None = None, timeout: float = -1) -> Any: ...
    async def init_transactions(self, timeout: float | None = None) -> None: ...
    async def begin_transaction(self) -> None: ...
    async def send_offsets_to_transaction(
        self,
        positions: list[TopicPartition],
        group_metadata: object,
        timeout: float | None = None,
    ) -> None: ...
    async def commit_transaction(self, timeout: float | None = None) -> None: ...
    async def abort_transaction(self, timeout: float | None = None) -> None: ...
    async def set_sasl_credentials(self, username: str, password: str) -> None: ...
