"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
from typing import Callable, Optional, Union

from ..serialization import SerializationContext
from .schema_registry_client import Schema, SchemaRegistryClient

class JSONSerializer:
    def __init__(
        self,
        schema_str: Union[str, Schema, None],
        schema_registry_client: SchemaRegistryClient,
        to_dict: Optional[Callable[[object, SerializationContext], dict]] = None,
        conf: Optional[dict] = None,
        rule_conf: Optional[dict] = None,
    ) -> None: ...
    def __call__(
        self,
        obj: object,
        ctx: Optional[SerializationContext] = None,
    ) -> Optional[bytes]: ...

class JSONDeserializer:
    def __init__(
        self,
        schema_str: Union[str, Schema, None],
        from_dict: Optional[Callable[[dict, SerializationContext], object]] = None,
        schema_registry_client: Optional[SchemaRegistryClient] = None,
        conf: Optional[dict] = None,
        rule_conf: Optional[dict] = None,
    ) -> None: ...
    def __call__(
        self,
        data: Optional[bytes],
        ctx: Optional[SerializationContext] = None,
    ) -> Optional[bytes]: ...
