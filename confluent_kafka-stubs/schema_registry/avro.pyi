"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
from typing import Callable, Optional, Union

from ..serialization import SerializationContext
from .schema_registry_client import Schema, SchemaRegistryClient

class AvroSerializer:
    def __init__(
        self,
        schema_registry_client: SchemaRegistryClient,
        schema_str: Union[str, Schema, None] = None,
        to_dict: Optional[Callable[[object, SerializationContext], dict]] = None,
        conf: Optional[dict] = None,
        rule_conf: Optional[dict] = None,
    ) -> None: ...
    def __call__(
        self,
        obj: object,
        ctx: Optional[SerializationContext] = None,
    ) -> Optional[bytes]: ...

class AvroDeserializer:
    def __init__(
        self,
        schema_registry_client: SchemaRegistryClient,
        schema_str: Union[str, Schema, None] = None,
        from_dict: Optional[Callable[[dict, SerializationContext], object]] = None,
        return_record_name: bool = False,
        conf: Optional[dict] = None,
        rule_conf: Optional[dict] = None,
    ) -> None: ...
    def __call__(
        self,
        data: Optional[bytes],
        ctx: Optional[SerializationContext] = None,
    ) -> Union[dict, object, None]: ...
