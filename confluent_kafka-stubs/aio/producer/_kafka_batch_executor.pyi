"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
import concurrent.futures
from typing import Any, Dict, Sequence

from ...cimpl import Producer

class ProducerBatchExecutor:
    def __init__(self, producer: Producer, executor: concurrent.futures.Executor) -> None: ...
    async def execute_batch(
        self,
        topic: str,
        batch_messages: Sequence[Dict[str, Any]],
        partition: int = -1,
    ) -> int: ...
    async def flush_librdkafka_queue(self, timeout: float = -1) -> int: ...
