"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""
from __future__ import annotations

# standard library
from enum import Enum
from typing import Literal, Type

from ..cimpl import KafkaError as KafkaError
from ._resource import ResourceType as ResourceType

class AlterConfigOpType(Enum):
    SET: Literal["ALTER_CONFIG_OP_TYPE_SET"]
    DELETE: Literal["ALTER_CONFIG_OP_TYPE_DELETE"]
    APPEND: Literal["ALTER_CONFIG_OP_TYPE_APPEND"]
    SUBTRACT: Literal["ALTER_CONFIG_OP_TYPE_SUBTRACT"]

class ConfigSource(Enum):
    UNKNOWN_CONFIG: Literal["CONFIG_SOURCE_UNKNOWN_CONFIG"]
    DYNAMIC_TOPIC_CONFIG: Literal["CONFIG_SOURCE_DYNAMIC_TOPIC_CONFIG"]
    DYNAMIC_BROKER_CONFIG: Literal["CONFIG_SOURCE_DYNAMIC_BROKER_CONFIG"]
    DYNAMIC_DEFAULT_BROKER_CONFIG: Literal["CONFIG_SOURCE_DYNAMIC_DEFAULT_BROKER_CONFIG"]
    STATIC_BROKER_CONFIG: Literal["CONFIG_SOURCE_STATIC_BROKER_CONFIG"]
    DEFAULT_CONFIG: Literal["CONFIG_SOURCE_DEFAULT_CONFIG"]

class ConfigEntry:
    def __init__(
        self,
        name: str,
        value,
        source=Literal["UNKNOWN_CONFIG"],
        is_read_only: bool = False,
        is_default: bool = False,
        is_sensitive: bool = False,
        is_synonym: bool = False,
        synonyms: list["ConfigEntry"] | None = None,
        incremental_operation: "AlterConfigOpType" | None = None,
    ) -> None: ...

class ConfigResource:
    def __init__(
        self,
        restype: Type["ResourceType"],
        name: str,
        set_config: dict[str, str] | None = None,
        described_configs: dict | None = ...,
        error: "KafkaError" | None = None,
        incremental_configs: list["ConfigEntry"] | None = None,
    ) -> None: ...
    def __hash__(self) -> int: ...
    def __lt__(self, other: "ConfigResource") -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __len__(self) -> int: ...
    def set_config(self, name: str, value, overwrite: bool = True) -> None: ...
    def add_incremental_config(self, config_entry: "ConfigEntry") -> None: ...
