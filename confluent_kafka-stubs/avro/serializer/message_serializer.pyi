"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""
# standard library
from io import BytesIO
from logging import Logger
from typing import TYPE_CHECKING, Any, Callable

# pypi/conda library
from confluent_kafka.avro import ClientError as ClientError
from confluent_kafka.avro.serializer import KeySerializerError as KeySerializerError
from confluent_kafka.avro.serializer import SerializerError as SerializerError
from confluent_kafka.avro.serializer import ValueSerializerError as ValueSerializerError
from confluent_kafka.schema_registry.schema_registry_client import SchemaRegistryClient

log: Logger
MAGIC_BYTE: int
HAS_FAST: bool

if TYPE_CHECKING:
    """Helping users who installed avro package can get type hints"""
    try:
        # pypi/conda library
        from avro.schema import Schema  # type: ignore # this cannot be resolved if avro isn't installed
    except ImportError:
        # standard library
        from typing import Any as Schema  # type: ignore

class ContextStringIO(BytesIO):
    def __enter__(self): ...
    def __exit__(self, *args): ...

class MessageSerializer:
    registry_client: SchemaRegistryClient
    id_to_decoder_func: dict[int, Callable]
    id_to_writers: dict[int, bytes]
    reader_key_schema: str | bytes | None = None
    reader_value_schema: str | bytes | None = None

    def __init__(
        self,
        registry_client,
        reader_key_schema: Any | None = None,
        reader_value_schema: Any | None = None,
    ) -> None: ...
    def encode_record_with_schema(self, topic: str, schema: "Schema", record: dict, is_key: bool = ...) -> bytes: ...
    def encode_record_with_schema_id(self, schema_id: int, record: dict, is_key: bool = ...) -> Callable: ...
    def decode_message(self, message: str | bytes | None = None, is_key: bool = ...) -> dict[str, Any]: ...
