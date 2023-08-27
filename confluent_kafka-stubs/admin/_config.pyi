"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""
from __future__ import annotations

# standard library
from enum import Enum
from typing import ClassVar
from typing import Type as _type

from ..cimpl import KafkaError as KafkaError
from ._resource import ResourceType as ResourceType

class AlterConfigOpType(Enum):
    SET: int
    DELETE: int
    APPEND: int
    SUBTRACT: int

AlterConfigOpType.APPEND

class ConfigSource(Enum):
    UNKNOWN_CONFIG: int
    DYNAMIC_TOPIC_CONFIG: int
    DYNAMIC_BROKER_CONFIG: int
    DYNAMIC_DEFAULT_BROKER_CONFIG: int
    STATIC_BROKER_CONFIG: int
    DEFAULT_CONFIG: int

class ConfigEntry:
    name: ClassVar[str]
    value: ClassVar[str]
    source: ClassVar[ConfigSource]
    is_read_only: ClassVar[bool]
    is_default: ClassVar[bool]
    is_sensitive: ClassVar[bool]
    is_synonym: ClassVar[bool]
    synonyms: ClassVar[ConfigEntry]
    incremental_operation: ClassVar[AlterConfigOpType]

    def __init__(
        self,
        name: str,
        value,
        source: ConfigSource = ConfigSource.UNKNOWN_CONFIG,
        is_read_only: bool = False,
        is_default: bool = False,
        is_sensitive: bool = False,
        is_synonym: bool = False,
        synonyms: list[ConfigEntry] | None = None,
        incremental_operation: AlterConfigOpType | None = None,
    ) -> None: ...

class ConfigResource:
    Type = _type[ResourceType]

    restype: ClassVar[ConfigResource]
    restype_int: ClassVar[int]
    name: ClassVar[str]
    set_config_dict: ClassVar[dict[str, str]]
    incremental_configs: ClassVar[list[ConfigEntry]]
    configs: ClassVar[dict]
    error: ClassVar[KafkaError]

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
