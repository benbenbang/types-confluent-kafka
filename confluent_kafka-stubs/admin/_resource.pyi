"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
from enum import Enum

from ..cimpl import (
    RESOURCE_ANY,
    RESOURCE_BROKER,
    RESOURCE_GROUP,
    RESOURCE_PATTERN_ANY,
    RESOURCE_PATTERN_LITERAL,
    RESOURCE_PATTERN_MATCH,
    RESOURCE_PATTERN_PREFIXED,
    RESOURCE_PATTERN_UNKNOWN,
    RESOURCE_TOPIC,
    RESOURCE_TRANSACTIONAL_ID,
    RESOURCE_UNKNOWN,
)

class ResourceType(Enum):
    UNKNOWN = RESOURCE_UNKNOWN
    ANY = RESOURCE_ANY
    TOPIC = RESOURCE_TOPIC
    GROUP = RESOURCE_GROUP
    BROKER = RESOURCE_BROKER
    TRANSACTIONAL_ID = RESOURCE_TRANSACTIONAL_ID

    def __lt__(self, other: ResourceType) -> bool: ...

class ResourcePatternType(Enum):
    UNKNOWN = RESOURCE_PATTERN_UNKNOWN
    ANY = RESOURCE_PATTERN_ANY
    MATCH = RESOURCE_PATTERN_MATCH
    LITERAL = RESOURCE_PATTERN_LITERAL
    PREFIXED = RESOURCE_PATTERN_PREFIXED

    def __lt__(self, other: ResourcePatternType) -> bool: ...
