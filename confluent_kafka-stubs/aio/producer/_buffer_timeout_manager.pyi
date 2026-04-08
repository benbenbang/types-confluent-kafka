"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

from ._kafka_batch_executor import ProducerBatchExecutor
from ._producer_batch_processor import ProducerBatchManager

class BufferTimeoutManager:
    def __init__(
        self,
        batch_processor: ProducerBatchManager,
        kafka_executor: ProducerBatchExecutor,
        timeout: float,
    ) -> None: ...
    def start_timeout_monitoring(self) -> None: ...
    def stop_timeout_monitoring(self) -> None: ...
    def mark_activity(self) -> None: ...
