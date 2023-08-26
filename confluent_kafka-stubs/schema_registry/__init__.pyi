"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from .schema_registry_client import RegisteredSchema as RegisteredSchema
from .schema_registry_client import Schema as Schema
from .schema_registry_client import SchemaReference as SchemaReference
from .schema_registry_client import SchemaRegistryClient as SchemaRegistryClient
from .schema_registry_client import SchemaRegistryError as SchemaRegistryError

def topic_subject_name_strategy(ctx, record_name): ...
def topic_record_subject_name_strategy(ctx, record_name): ...
def record_subject_name_strategy(ctx, record_name): ...
