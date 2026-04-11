"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
from typing import Any, Optional

from ..serialization import SerializationContext
from .schema_registry_client import SchemaRegistryClient

class ProtobufSerializer:
    def __init__(
        self,
        msg_type: Any,
        schema_registry_client: SchemaRegistryClient,
        conf: Optional[dict] = None,
        rule_conf: Optional[dict] = None,
    ) -> None: ...
    def __call__(
        self,
        message: Any,
        ctx: Optional[SerializationContext] = None,
    ) -> Optional[bytes]: ...

class ProtobufDeserializer:
    def __init__(
        self,
        message_type: Any,
        conf: Optional[dict] = None,
        schema_registry_client: Optional[SchemaRegistryClient] = None,
        rule_conf: Optional[dict] = None,
    ) -> None: ...
    def __call__(
        self,
        data: Optional[bytes],
        ctx: Optional[SerializationContext] = None,
    ) -> Optional[bytes]: ...
