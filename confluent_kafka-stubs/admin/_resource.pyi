"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""
from __future__ import annotations

# standard library
from enum import Enum

class ResourceType(Enum):
    UNKNOWN: int
    ANY: int
    TOPIC: int
    GROUP: int
    BROKER: int

    def __lt__(self, other: ResourceType) -> bool: ...

class ResourcePatternType(Enum):
    UNKNOWN: int
    ANY: int
    MATCH: int
    LITERAL: int
    PREFIXED: int

    def __lt__(self, other) -> bool: ...
