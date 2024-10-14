"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

from ..cimpl import Message

class ClientError(Exception):
    message: Message
    http_code: int

    def __init__(self, message, http_code: int | None = None) -> None: ...
