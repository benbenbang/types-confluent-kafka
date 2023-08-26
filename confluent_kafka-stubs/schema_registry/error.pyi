"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""
from __future__ import annotations

# standard library
from typing import ClassVar

# pypi/conda library
from fastavro.schema import SchemaParseException as SchemaParseException
from fastavro.schema import UnknownType as UnknownType

class SchemaRegistryError(Exception):
    http_status_code: ClassVar[int]
    error_code: ClassVar[int]
    error_message: ClassVar[str]

    UNKNOWN: int = -1

    def __init__(self, http_status_code, error_code, error_message) -> None: ...
