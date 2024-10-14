"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
from enum import Enum
from typing import ClassVar

class ResourceType(Enum):
    UNKNOWN = ClassVar[int]
    ANY = ClassVar[int]
    TOPIC = ClassVar[int]
    GROUP = ClassVar[int]
    BROKER = ClassVar[int]

    def __lt__(self, other: ResourceType) -> bool: ...

class ResourcePatternType(Enum):
    UNKNOWN = ClassVar[int]
    ANY = ClassVar[int]
    MATCH = ClassVar[int]
    LITERAL = ClassVar[int]
    PREFIXED = ClassVar[int]

    def __lt__(self, other) -> bool: ...
