"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
from typing import Optional

# pypi/conda library
from fastavro.schema import SchemaParseException as SchemaParseException
from fastavro.schema import UnknownType as UnknownType

class SchemaRegistryError(Exception):
    http_status_code: int
    error_code: int
    error_message: str

    UNKNOWN: int

    def __init__(self, http_status_code: int, error_code: int, error_message: str) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...

class OAuthTokenError(Exception):
    message: str
    status_code: Optional[int]
    response_text: Optional[str]

    def __init__(
        self,
        message: str,
        status_code: Optional[int] = None,
        response_text: Optional[str] = None,
    ) -> None: ...
