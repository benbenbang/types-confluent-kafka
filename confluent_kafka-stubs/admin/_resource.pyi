"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""
from __future__ import annotations

# standard library
from enum import Enum
from typing import Literal

class ResourceType(Enum):
    """
    UNKNOWN = RESOURCE_UNKNOWN  #: Resource type is not known or not set.
    ANY = RESOURCE_ANY  #: Match any resource, used for lookups.
    TOPIC = RESOURCE_TOPIC  #: Topic resource. Resource name is topic name.
    GROUP = RESOURCE_GROUP  #: Group resource. Resource name is group.id.
    BROKER = RESOURCE_BROKER  #: Broker resource. Resource name is broker id.
    """

    UNKNOWN: Literal["RESOURCE_UNKNOWN"]
    ANY: Literal["RESOURCE_ANY"]
    TOPIC: Literal["RESOURCE_TOPIC"]
    GROUP: Literal["RESOURCE_GROUP"]
    BROKER: Literal["RESOURCE_BROKER"]
    def __lt__(self, other: "ResourceType") -> bool: ...

class ResourcePatternType(Enum):
    """
    UNKNOWN = RESOURCE_PATTERN_UNKNOWN  #: Resource pattern type is not known or not set.
    ANY = RESOURCE_PATTERN_ANY  #: Match any resource, used for lookups.
    MATCH = RESOURCE_PATTERN_MATCH  #: Match: will perform pattern matching
    LITERAL = RESOURCE_PATTERN_LITERAL  #: Literal: A literal resource name
    PREFIXED = RESOURCE_PATTERN_PREFIXED  #: Prefixed: A prefixed resource name
    """

    UNKNOWN: Literal["RESOURCE_PATTERN_UNKNOWN"]
    ANY: Literal["RESOURCE_PATTERN_ANY"]
    MATCH: Literal["RESOURCE_PATTERN_MATCH"]
    LITERAL: Literal["RESOURCE_PATTERN_LITERAL"]
    PREFIXED: Literal["RESOURCE_PATTERN_PREFIXED"]
    def __lt__(self, other: "ResourcePatternType") -> bool: ...
