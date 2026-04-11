"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
from enum import Enum
from typing import Any, Dict, List, Literal, Optional, Union

from .error import SchemaRegistryError as SchemaRegistryError

# ---------------------------------------------------------------------------
# Enumerations
# ---------------------------------------------------------------------------

class RuleKind(str, Enum):
    CONDITION = "CONDITION"
    TRANSFORM = "TRANSFORM"

class RuleMode(str, Enum):
    UPGRADE = "UPGRADE"
    DOWNGRADE = "DOWNGRADE"
    UPDOWN = "UPDOWN"
    READ = "READ"
    WRITE = "WRITE"
    WRITEREAD = "WRITEREAD"

# ---------------------------------------------------------------------------
# Rule / metadata value objects
# ---------------------------------------------------------------------------

class RuleParams:
    params: Dict[str, str]

    def __init__(self, params: Dict[str, str] = ...) -> None: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @classmethod
    def from_dict(cls, src_dict: Dict[str, Any]) -> RuleParams: ...

class Rule:
    name: Optional[str]
    doc: Optional[str]
    kind: Optional[RuleKind]
    mode: Optional[RuleMode]
    type: Optional[str]
    tags: Optional[List[str]]
    params: Optional[RuleParams]
    expr: Optional[str]
    on_success: Optional[str]
    on_failure: Optional[str]
    disabled: Optional[bool]

    def __init__(
        self,
        name: Optional[str] = None,
        doc: Optional[str] = None,
        kind: Optional[RuleKind] = None,
        mode: Optional[RuleMode] = None,
        type: Optional[str] = None,
        tags: Optional[List[str]] = None,
        params: Optional[RuleParams] = None,
        expr: Optional[str] = None,
        on_success: Optional[str] = None,
        on_failure: Optional[str] = None,
        disabled: Optional[bool] = None,
    ) -> None: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @classmethod
    def from_dict(cls, src_dict: Dict[str, Any]) -> Rule: ...

class RuleSet:
    migration_rules: Optional[List[Rule]]
    domain_rules: Optional[List[Rule]]
    encoding_rules: Optional[List[Rule]]
    enable_at: Optional[str]

    def __init__(
        self,
        migration_rules: Optional[List[Rule]] = None,
        domain_rules: Optional[List[Rule]] = None,
        encoding_rules: Optional[List[Rule]] = None,
        enable_at: Optional[str] = None,
    ) -> None: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @classmethod
    def from_dict(cls, src_dict: Dict[str, Any]) -> RuleSet: ...

class MetadataTags:
    tags: Dict[str, List[str]]

    def __init__(self, tags: Dict[str, List[str]] = ...) -> None: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @classmethod
    def from_dict(cls, src_dict: Dict[str, Any]) -> MetadataTags: ...

class MetadataProperties:
    properties: Dict[str, str]

    def __init__(self, properties: Dict[str, str] = ...) -> None: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @classmethod
    def from_dict(cls, src_dict: Dict[str, Any]) -> MetadataProperties: ...

class Metadata:
    tags: Optional[MetadataTags]
    properties: Optional[MetadataProperties]
    sensitive: Optional[List[str]]

    def __init__(
        self,
        tags: Optional[MetadataTags] = None,
        properties: Optional[MetadataProperties] = None,
        sensitive: Optional[List[str]] = None,
    ) -> None: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @classmethod
    def from_dict(cls, src_dict: Dict[str, Any]) -> Metadata: ...

# ---------------------------------------------------------------------------
# Schema reference and core schema types
# ---------------------------------------------------------------------------

class SchemaReference:
    name: Optional[str]
    subject: Optional[str]
    version: Optional[int]

    def __init__(
        self,
        name: Optional[str] = None,
        subject: Optional[str] = None,
        version: Optional[int] = None,
    ) -> None: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @classmethod
    def from_dict(cls, src_dict: Dict[str, Any]) -> SchemaReference: ...

class SchemaVersion:
    subject: Optional[str]
    version: Optional[int]

    def __init__(self, subject: Optional[str] = None, version: Optional[int] = None) -> None: ...
    @classmethod
    def from_dict(cls, src_dict: Dict[str, Any]) -> SchemaVersion: ...

class ConfigCompatibilityLevel(str, Enum):
    BACKWARD = "BACKWARD"
    BACKWARD_TRANSITIVE = "BACKWARD_TRANSITIVE"
    FORWARD = "FORWARD"
    FORWARD_TRANSITIVE = "FORWARD_TRANSITIVE"
    FULL = "FULL"
    FULL_TRANSITIVE = "FULL_TRANSITIVE"
    NONE = "NONE"

class ServerConfig:
    compatibility: Optional[ConfigCompatibilityLevel]
    compatibility_level: Optional[ConfigCompatibilityLevel]
    compatibility_group: Optional[str]
    default_metadata: Optional[Metadata]
    override_metadata: Optional[Metadata]
    default_rule_set: Optional[RuleSet]
    override_rule_set: Optional[RuleSet]

    def __init__(
        self,
        compatibility: Optional[ConfigCompatibilityLevel] = None,
        compatibility_level: Optional[ConfigCompatibilityLevel] = None,
        compatibility_group: Optional[str] = None,
        default_metadata: Optional[Metadata] = None,
        override_metadata: Optional[Metadata] = None,
        default_rule_set: Optional[RuleSet] = None,
        override_rule_set: Optional[RuleSet] = None,
    ) -> None: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @classmethod
    def from_dict(cls, src_dict: Dict[str, Any]) -> ServerConfig: ...

class Schema:
    schema_str: Optional[str]
    schema_type: Optional[str]
    references: Optional[List[SchemaReference]]
    metadata: Optional[Metadata]
    rule_set: Optional[RuleSet]

    def __init__(
        self,
        schema_str: Optional[str],
        schema_type: Optional[str] = "AVRO",
        references: Optional[List[SchemaReference]] = None,
        metadata: Optional[Metadata] = None,
        rule_set: Optional[RuleSet] = None,
    ) -> None: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @classmethod
    def from_dict(cls, src_dict: Dict[str, Any]) -> Schema: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class RegisteredSchema:
    subject: Optional[str]
    version: Optional[int]
    schema_id: Optional[int]
    guid: Optional[str]
    schema: Schema

    def __init__(
        self,
        subject: Optional[str],
        version: Optional[int],
        schema_id: Optional[int],
        guid: Optional[str],
        schema: Schema,
    ) -> None: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @classmethod
    def from_dict(cls, src_dict: Dict[str, Any]) -> RegisteredSchema: ...

# ---------------------------------------------------------------------------
# Association types
# ---------------------------------------------------------------------------

class Association:
    subject: Optional[str]
    guid: Optional[str]
    resource_name: Optional[str]
    resource_namespace: Optional[str]
    resource_id: Optional[str]
    resource_type: Optional[str]
    association_type: Optional[str]
    frozen: bool

    def __init__(
        self,
        subject: Optional[str] = None,
        guid: Optional[str] = None,
        resource_name: Optional[str] = None,
        resource_namespace: Optional[str] = None,
        resource_id: Optional[str] = None,
        resource_type: Optional[str] = None,
        association_type: Optional[str] = None,
        frozen: bool = False,
    ) -> None: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @classmethod
    def from_dict(cls, src_dict: Dict[str, Any]) -> Association: ...

class AssociationInfo:
    subject: Optional[str]
    association_type: Optional[str]
    lifecycle: Optional[str]
    frozen: bool
    schema: Optional[Schema]

    def __init__(
        self,
        subject: Optional[str] = None,
        association_type: Optional[str] = None,
        lifecycle: Optional[str] = None,
        frozen: bool = False,
        schema: Optional[Schema] = None,
    ) -> None: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @classmethod
    def from_dict(cls, src_dict: Dict[str, Any]) -> AssociationInfo: ...

class AssociationCreateOrUpdateInfo:
    subject: Optional[str]
    association_type: Optional[str]
    lifecycle: Optional[str]
    frozen: Optional[bool]
    schema: Optional[Schema]
    normalize: Optional[bool]

    def __init__(
        self,
        subject: Optional[str] = None,
        association_type: Optional[str] = None,
        lifecycle: Optional[str] = None,
        frozen: Optional[bool] = None,
        schema: Optional[Schema] = None,
        normalize: Optional[bool] = None,
    ) -> None: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @classmethod
    def from_dict(cls, src_dict: Dict[str, Any]) -> AssociationCreateOrUpdateInfo: ...

class AssociationCreateOrUpdateRequest:
    resource_name: Optional[str]
    resource_namespace: Optional[str]
    resource_id: Optional[str]
    resource_type: Optional[str]
    associations: Optional[List[AssociationCreateOrUpdateInfo]]

    def __init__(
        self,
        resource_name: Optional[str] = None,
        resource_namespace: Optional[str] = None,
        resource_id: Optional[str] = None,
        resource_type: Optional[str] = None,
        associations: Optional[List[AssociationCreateOrUpdateInfo]] = None,
    ) -> None: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @classmethod
    def from_dict(cls, src_dict: Dict[str, Any]) -> AssociationCreateOrUpdateRequest: ...

class AssociationResponse:
    resource_name: Optional[str]
    resource_namespace: Optional[str]
    resource_id: Optional[str]
    resource_type: Optional[str]
    associations: Optional[List[AssociationInfo]]

    def __init__(
        self,
        resource_name: Optional[str] = None,
        resource_namespace: Optional[str] = None,
        resource_id: Optional[str] = None,
        resource_type: Optional[str] = None,
        associations: Optional[List[AssociationInfo]] = None,
    ) -> None: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @classmethod
    def from_dict(cls, src_dict: Dict[str, Any]) -> AssociationResponse: ...

# ---------------------------------------------------------------------------
# Schema Registry Client (sync)
# ---------------------------------------------------------------------------

class SchemaRegistryClient:
    def __init__(self, conf: dict) -> None: ...
    def __enter__(self) -> SchemaRegistryClient: ...
    def __exit__(self, *args: Any) -> None: ...
    def config(self) -> dict: ...
    def register_schema(
        self,
        subject_name: str,
        schema: Schema,
        normalize_schemas: bool = False,
    ) -> int: ...
    def register_schema_full_response(
        self,
        subject_name: str,
        schema: Schema,
        normalize_schemas: bool = False,
    ) -> RegisteredSchema: ...
    def get_schema(
        self,
        schema_id: int,
        subject_name: Optional[str] = None,
        fmt: Optional[str] = None,
        reference_format: Optional[str] = None,
    ) -> Schema: ...
    def get_schema_by_guid(self, guid: str, fmt: Optional[str] = None) -> Schema: ...
    def get_schema_types(self) -> List[str]: ...
    def get_subjects_by_schema_id(
        self,
        schema_id: int,
        subject_name: Optional[str] = None,
        deleted: bool = False,
        offset: int = 0,
        limit: int = -1,
    ) -> List[str]: ...
    def get_schema_versions(
        self,
        schema_id: int,
        subject_name: Optional[str] = None,
        deleted: bool = False,
        offset: int = 0,
        limit: int = -1,
    ) -> List[SchemaVersion]: ...
    def lookup_schema(
        self,
        subject_name: str,
        schema: Schema,
        normalize_schemas: bool = False,
        fmt: Optional[str] = None,
        deleted: bool = False,
    ) -> RegisteredSchema: ...
    def get_subjects(
        self,
        subject_prefix: Optional[str] = None,
        deleted: bool = False,
        deleted_only: bool = False,
        offset: int = 0,
        limit: int = -1,
    ) -> List[str]: ...
    def delete_subject(self, subject_name: str, permanent: bool = False) -> List[int]: ...
    def get_latest_version(self, subject_name: str, fmt: Optional[str] = None) -> RegisteredSchema: ...
    def get_latest_with_metadata(
        self,
        subject_name: str,
        metadata: Dict[str, str],
        deleted: bool = False,
        fmt: Optional[str] = None,
    ) -> RegisteredSchema: ...
    def get_version(
        self,
        subject_name: str,
        version: Union[int, Literal["latest"]] = "latest",
        deleted: bool = False,
        fmt: Optional[str] = None,
    ) -> RegisteredSchema: ...
    def get_referenced_by(
        self,
        subject_name: str,
        version: Union[int, Literal["latest"]] = "latest",
        offset: int = 0,
        limit: int = -1,
    ) -> List[int]: ...
    def get_versions(
        self,
        subject_name: str,
        deleted: bool = False,
        deleted_only: bool = False,
        offset: int = 0,
        limit: int = -1,
    ) -> List[int]: ...
    def delete_version(self, subject_name: str, version: int, permanent: bool = False) -> int: ...
    def set_compatibility(self, subject_name: Optional[str] = None, level: Optional[str] = None) -> str: ...
    def get_compatibility(self, subject_name: Optional[str] = None) -> str: ...
    def test_compatibility(
        self,
        subject_name: str,
        schema: Schema,
        version: Union[int, str] = "latest",
        normalize: bool = False,
        verbose: bool = False,
    ) -> bool: ...
    def test_compatibility_all_versions(
        self,
        subject_name: str,
        schema: Schema,
        normalize: bool = False,
        verbose: bool = False,
    ) -> bool: ...
    def set_config(
        self,
        subject_name: Optional[str] = None,
        config: Optional[ServerConfig] = None,
    ) -> ServerConfig: ...
    def delete_config(self, subject_name: Optional[str] = None) -> ServerConfig: ...
    def get_config(self, subject_name: Optional[str] = None) -> ServerConfig: ...
    def get_mode(self, subject_name: str) -> str: ...
    def update_mode(self, subject_name: str, mode: str, force: bool = False) -> str: ...
    def delete_mode(self, subject_name: str) -> str: ...
    def get_global_mode(self) -> str: ...
    def update_global_mode(self, mode: str, force: bool = False) -> str: ...
    def get_contexts(self, offset: int = 0, limit: int = -1) -> List[str]: ...
    def clear_latest_caches(self) -> None: ...
    def clear_caches(self) -> None: ...
    def get_associations_by_resource_name(
        self,
        resource_name: str,
        resource_namespace: str,
        resource_type: Optional[str] = None,
        association_types: Optional[List[str]] = None,
        offset: int = 0,
        limit: int = -1,
    ) -> List[Association]: ...
    def create_association(self, request: AssociationCreateOrUpdateRequest) -> AssociationResponse: ...
    def delete_associations(
        self,
        resource_id: str,
        resource_type: Optional[str] = None,
        association_types: Optional[List[str]] = None,
        cascade_lifecycle: bool = False,
    ) -> None: ...
    @staticmethod
    def new_client(conf: dict) -> SchemaRegistryClient: ...

# ---------------------------------------------------------------------------
# Schema Registry Client (async)
# ---------------------------------------------------------------------------

class AsyncSchemaRegistryClient:
    def __init__(self, conf: dict) -> None: ...
    async def __aenter__(self) -> AsyncSchemaRegistryClient: ...
    async def __aexit__(self, *args: Any) -> None: ...
    def config(self) -> dict: ...
    async def register_schema(
        self,
        subject_name: str,
        schema: Schema,
        normalize_schemas: bool = False,
    ) -> int: ...
    async def register_schema_full_response(
        self,
        subject_name: str,
        schema: Schema,
        normalize_schemas: bool = False,
    ) -> RegisteredSchema: ...
    async def get_schema(
        self,
        schema_id: int,
        subject_name: Optional[str] = None,
        fmt: Optional[str] = None,
        reference_format: Optional[str] = None,
    ) -> Schema: ...
    async def get_schema_by_guid(self, guid: str, fmt: Optional[str] = None) -> Schema: ...
    async def get_schema_types(self) -> List[str]: ...
    async def get_subjects_by_schema_id(
        self,
        schema_id: int,
        subject_name: Optional[str] = None,
        deleted: bool = False,
        offset: int = 0,
        limit: int = -1,
    ) -> List[str]: ...
    async def get_schema_versions(
        self,
        schema_id: int,
        subject_name: Optional[str] = None,
        deleted: bool = False,
        offset: int = 0,
        limit: int = -1,
    ) -> List[SchemaVersion]: ...
    async def lookup_schema(
        self,
        subject_name: str,
        schema: Schema,
        normalize_schemas: bool = False,
        fmt: Optional[str] = None,
        deleted: bool = False,
    ) -> RegisteredSchema: ...
    async def get_subjects(
        self,
        subject_prefix: Optional[str] = None,
        deleted: bool = False,
        deleted_only: bool = False,
        offset: int = 0,
        limit: int = -1,
    ) -> List[str]: ...
    async def delete_subject(self, subject_name: str, permanent: bool = False) -> List[int]: ...
    async def get_latest_version(self, subject_name: str, fmt: Optional[str] = None) -> RegisteredSchema: ...
    async def get_latest_with_metadata(
        self,
        subject_name: str,
        metadata: Dict[str, str],
        deleted: bool = False,
        fmt: Optional[str] = None,
    ) -> RegisteredSchema: ...
    async def get_version(
        self,
        subject_name: str,
        version: Union[int, Literal["latest"]] = "latest",
        deleted: bool = False,
        fmt: Optional[str] = None,
    ) -> RegisteredSchema: ...
    async def get_referenced_by(
        self,
        subject_name: str,
        version: Union[int, Literal["latest"]] = "latest",
        offset: int = 0,
        limit: int = -1,
    ) -> List[int]: ...
    async def get_versions(
        self,
        subject_name: str,
        deleted: bool = False,
        deleted_only: bool = False,
        offset: int = 0,
        limit: int = -1,
    ) -> List[int]: ...
    async def delete_version(self, subject_name: str, version: int, permanent: bool = False) -> int: ...
    async def set_compatibility(self, subject_name: Optional[str] = None, level: Optional[str] = None) -> str: ...
    async def get_compatibility(self, subject_name: Optional[str] = None) -> str: ...
    async def test_compatibility(
        self,
        subject_name: str,
        schema: Schema,
        version: Union[int, str] = "latest",
        normalize: bool = False,
        verbose: bool = False,
    ) -> bool: ...
    async def test_compatibility_all_versions(
        self,
        subject_name: str,
        schema: Schema,
        normalize: bool = False,
        verbose: bool = False,
    ) -> bool: ...
    async def set_config(
        self,
        subject_name: Optional[str] = None,
        config: Optional[ServerConfig] = None,
    ) -> ServerConfig: ...
    async def delete_config(self, subject_name: Optional[str] = None) -> ServerConfig: ...
    async def get_config(self, subject_name: Optional[str] = None) -> ServerConfig: ...
    async def get_mode(self, subject_name: str) -> str: ...
    async def update_mode(self, subject_name: str, mode: str, force: bool = False) -> str: ...
    async def delete_mode(self, subject_name: str) -> str: ...
    async def get_global_mode(self) -> str: ...
    async def update_global_mode(self, mode: str, force: bool = False) -> str: ...
    async def get_contexts(self, offset: int = 0, limit: int = -1) -> List[str]: ...
    def clear_latest_caches(self) -> None: ...
    def clear_caches(self) -> None: ...
    async def get_associations_by_resource_name(
        self,
        resource_name: str,
        resource_namespace: str,
        resource_type: Optional[str] = None,
        association_types: Optional[List[str]] = None,
        offset: int = 0,
        limit: int = -1,
    ) -> List[Association]: ...
    async def create_association(self, request: AssociationCreateOrUpdateRequest) -> AssociationResponse: ...
    async def delete_associations(
        self,
        resource_id: str,
        resource_type: Optional[str] = None,
        association_types: Optional[List[str]] = None,
        cascade_lifecycle: bool = False,
    ) -> None: ...
    @staticmethod
    def new_client(conf: dict) -> AsyncSchemaRegistryClient: ...
