"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""
from __future__ import annotations

# standard library
from typing import ClassVar

# pypi/conda library
from confluent_kafka.cimpl import Message

class ClientError(Exception):
    """Error thrown by Schema Registry clients"""

    message: ClassVar[Message]
    http_code: ClassVar[int]

    def __init__(self, message, http_code: int | None = None) -> None: ...
