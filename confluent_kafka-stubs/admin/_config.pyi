"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
from enum import Enum
from typing import ClassVar
from typing import Type as _type

from ..cimpl import (
    ALTER_CONFIG_OP_TYPE_APPEND,
    ALTER_CONFIG_OP_TYPE_DELETE,
    ALTER_CONFIG_OP_TYPE_SET,
    ALTER_CONFIG_OP_TYPE_SUBTRACT,
    CONFIG_SOURCE_DEFAULT_CONFIG,
    CONFIG_SOURCE_DYNAMIC_BROKER_CONFIG,
    CONFIG_SOURCE_DYNAMIC_DEFAULT_BROKER_CONFIG,
    CONFIG_SOURCE_DYNAMIC_TOPIC_CONFIG,
    CONFIG_SOURCE_STATIC_BROKER_CONFIG,
    CONFIG_SOURCE_UNKNOWN_CONFIG,
)
from ..cimpl import KafkaError as KafkaError
from ._resource import ResourceType as ResourceType

class AlterConfigOpType(Enum):
    SET = ALTER_CONFIG_OP_TYPE_SET
    DELETE = ALTER_CONFIG_OP_TYPE_DELETE
    APPEND = ALTER_CONFIG_OP_TYPE_APPEND
    SUBTRACT = ALTER_CONFIG_OP_TYPE_SUBTRACT

class ConfigSource(Enum):
    UNKNOWN_CONFIG = CONFIG_SOURCE_UNKNOWN_CONFIG  #: Unknown
    DYNAMIC_TOPIC_CONFIG = CONFIG_SOURCE_DYNAMIC_TOPIC_CONFIG  #: Dynamic Topic
    DYNAMIC_BROKER_CONFIG = CONFIG_SOURCE_DYNAMIC_BROKER_CONFIG  #: Dynamic Broker
    DYNAMIC_DEFAULT_BROKER_CONFIG = CONFIG_SOURCE_DYNAMIC_DEFAULT_BROKER_CONFIG  #: Dynamic Default Broker
    STATIC_BROKER_CONFIG = CONFIG_SOURCE_STATIC_BROKER_CONFIG  #: Static Broker
    DEFAULT_CONFIG = CONFIG_SOURCE_DEFAULT_CONFIG  #: Default

class ConfigEntry:
    name: str
    value: str
    source: ConfigSource
    is_read_only: bool
    is_default: bool
    is_sensitive: bool
    is_synonym: bool
    synonyms: list[ConfigEntry]
    incremental_operation: AlterConfigOpType | None

    def __init__(
        self,
        name: str,
        value,
        source: ConfigSource | int = ConfigSource.DEFAULT_CONFIG.value,
        is_read_only: bool = False,
        is_default: bool = False,
        is_sensitive: bool = False,
        is_synonym: bool = False,
        synonyms: list[ConfigEntry] | None = None,
        incremental_operation: AlterConfigOpType | None = None,
    ) -> None: ...

class ConfigResource:
    Type = ClassVar[_type[ResourceType]]

    restype: ConfigResource
    restype_int: int
    name: str
    set_config_dict: dict[str, str]
    incremental_configs: list[ConfigEntry]
    configs: dict | None
    error: KafkaError

    def __init__(
        self,
        restype: ConfigResource,
        name: str,
        set_config: dict[str, str] | None = None,
        described_configs: dict | None = ...,
        error: "KafkaError" | None = None,
        incremental_configs: list[ConfigEntry] | None = None,
    ) -> None: ...
    def __hash__(self) -> int: ...
    def __lt__(self, other: ConfigResource) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __len__(self) -> int: ...
    def set_config(self, name: str, value, overwrite: bool = True) -> None: ...
    def add_incremental_config(self, config_entry: ConfigEntry) -> None: ...
