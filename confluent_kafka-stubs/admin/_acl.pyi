"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
from enum import Enum, EnumMeta
from typing import Any, Literal

from .._util import ConversionUtil as ConversionUtil
from .._util import ValidationUtil as ValidationUtil
from ._resource import ResourcePatternType as ResourcePatternType
from ._resource import ResourceType as ResourceType

class AclOperation(Enum):
    UNKNOWN = 0
    ANY = 1
    ALL = 2
    READ = 3
    WRITE = 4
    CREATE = 5
    DELETE = 6
    ALTER = 7
    DESCRIBE = 8
    CLUSTER_ACTION = 9
    DESCRIBE_CONFIGS = 10
    ALTER_CONFIGS = 11
    IDEMPOTENT_WRITE = 12

    def __lt__(self, other: AclOperation) -> bool: ...

class AclPermissionType(Enum):
    UNKNOWN = 0
    ANY = 1
    DENY = 2
    ALLOW = 3

    def __lt__(self, other: AclPermissionType) -> bool: ...

class AclBinding:
    restype: ResourceType
    name: str
    resource_pattern_type: ResourcePatternType
    principal: str
    host: str
    operation: AclOperation
    permission_type: AclPermissionType
    restype_int: int
    resource_pattern_type_int: int
    operation_int: int
    permission_type_int: int

    def __init__(
        self,
        restype: ResourceType,
        name: str,
        resource_pattern_type: ResourcePatternType,
        principal: str,
        host: str,
        operation: AclOperation,
        permission_type: AclPermissionType,
    ) -> None: ...
    def _convert_enums(self) -> None: ...
    def _check_forbidden_enums(self, forbidden_enums: "EnumMeta") -> None: ...
    def _not_none_args(
        self,
    ) -> Literal["restype", "name", "resource_pattern_type", "principal", "host", "operation", "permission_type"]: ...
    def _string_args(self) -> Literal["name", "principal", "host"]: ...
    def _forbidden_enums(
        self,
    ) -> dict[
        str,
        Literal[
            "RESOURCE_ANY",
            "RESOURCE_PATTERN_ANY",
            "RESOURCE_PATTERN_MATCH",
            "ACL_OPERATION_ANY",
            "ACL_PERMISSION_TYPE_ANY",
        ],
    ]: ...
    def _convert_args(self) -> None: ...
    def _to_tuple(self) -> tuple[Any]: ...
    def __repr__(self) -> str: ...
    def __hash__(self) -> int: ...
    def __lt__(self, other: "AclBinding") -> bool: ...
    def __eq__(self, other: object) -> bool: ...

class AclBindingFilter(AclBinding):
    def __init__(
        self,
        restype: ResourceType,
        name: str,
        resource_pattern_type: ResourcePatternType,
        principal: str,
        host: str,
        operation: AclOperation,
        permission_type: AclPermissionType,
    ) -> None: ...
    def _not_none_args(self) -> Literal["restype", "resource_pattern_type", "operation", "permission_type"]: ...
    def _forbidden_enums(  # type: ignore[override]
        self,
    ) -> dict[
        str,
        Literal["RESOURCE_UNKNOWN", "RESOURCE_PATTERN_UNKNOWN", "ACL_OPERATION_UNKNOWN", "ACL_PERMISSION_TYPE_UNKNOWN"],
    ]: ...
