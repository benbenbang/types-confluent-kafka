"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
import io
from typing import Any, Optional

from ..serialization import SerializationContext
from .error import SchemaRegistryError as SchemaRegistryError
from .schema_registry_client import Association as Association
from .schema_registry_client import AssociationCreateOrUpdateInfo as AssociationCreateOrUpdateInfo
from .schema_registry_client import AssociationCreateOrUpdateRequest as AssociationCreateOrUpdateRequest
from .schema_registry_client import AssociationInfo as AssociationInfo
from .schema_registry_client import AssociationResponse as AssociationResponse
from .schema_registry_client import AsyncSchemaRegistryClient as AsyncSchemaRegistryClient
from .schema_registry_client import ConfigCompatibilityLevel as ConfigCompatibilityLevel
from .schema_registry_client import Metadata as Metadata
from .schema_registry_client import MetadataProperties as MetadataProperties
from .schema_registry_client import MetadataTags as MetadataTags
from .schema_registry_client import RegisteredSchema as RegisteredSchema
from .schema_registry_client import Rule as Rule
from .schema_registry_client import RuleKind as RuleKind
from .schema_registry_client import RuleMode as RuleMode
from .schema_registry_client import RuleParams as RuleParams
from .schema_registry_client import RuleSet as RuleSet
from .schema_registry_client import Schema as Schema
from .schema_registry_client import SchemaReference as SchemaReference
from .schema_registry_client import SchemaRegistryClient as SchemaRegistryClient
from .schema_registry_client import SchemaVersion as SchemaVersion
from .schema_registry_client import ServerConfig as ServerConfig

def topic_subject_name_strategy(
    ctx: Optional[SerializationContext],
    record_name: Optional[str],
) -> Optional[str]: ...
def topic_record_subject_name_strategy(
    ctx: Optional[SerializationContext],
    record_name: Optional[str],
) -> Optional[str]: ...
def record_subject_name_strategy(
    ctx: Optional[SerializationContext],
    record_name: Optional[str],
) -> Optional[str]: ...
def reference_subject_name_strategy(
    ctx: Optional[SerializationContext],
    schema_ref: SchemaReference,
) -> Optional[str]: ...
def header_schema_id_serializer(
    payload: bytes,
    ctx: Optional[SerializationContext],
    schema_id: Any,
) -> bytes: ...
def prefix_schema_id_serializer(
    payload: bytes,
    ctx: Any,
    schema_id: Any,
) -> bytes: ...
def dual_schema_id_deserializer(
    payload: bytes,
    ctx: Optional[SerializationContext],
    schema_id: Any,
) -> io.BytesIO: ...
def prefix_schema_id_deserializer(
    payload: bytes,
    ctx: Any,
    schema_id: Any,
) -> io.BytesIO: ...
