"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""
from __future__ import annotations

# standard library
from typing import ClassVar

class SerializerError(Exception):
    message: ClassVar[str]

    def __init__(self, message: str) -> None: ...

class KeySerializerError(SerializerError): ...
class ValueSerializerError(SerializerError): ...
