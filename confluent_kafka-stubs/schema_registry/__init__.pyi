"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

from ..serialization import SerializationContext
from .schema_registry_client import RegisteredSchema as RegisteredSchema
from .schema_registry_client import Schema as Schema
from .schema_registry_client import SchemaReference as SchemaReference
from .schema_registry_client import SchemaRegistryClient as SchemaRegistryClient
from .schema_registry_client import SchemaRegistryError as SchemaRegistryError

def topic_subject_name_strategy(ctx: SerializationContext, record_name: str): ...
def topic_record_subject_name_strategy(ctx: SerializationContext, record_name: str): ...
def record_subject_name_strategy(ctx: SerializationContext, record_name: str): ...
def reference_subject_name_strategy(ctx: SerializationContext, schema_ref: SchemaReference): ...
