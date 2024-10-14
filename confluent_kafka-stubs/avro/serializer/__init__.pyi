"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

class SerializerError(Exception):
    message: str

    def __init__(self, message: str) -> None: ...

class KeySerializerError(SerializerError): ...
class ValueSerializerError(SerializerError): ...
