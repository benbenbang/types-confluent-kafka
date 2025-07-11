"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
from logging import Logger
from pathlib import Path
from typing import TYPE_CHECKING, DefaultDict, Literal

from .error import ClientError as ClientError
from .load import loads as loads

if TYPE_CHECKING:
    """Helping users who installed avro package can get type hints"""
    try:
        # pypi/conda library
        from avro.schema import Schema  # type: ignore # this cannot be resolved if avro isn't installed
    except ImportError:
        # standard library
        from typing import Any as Schema  # type: ignore

VALID_LEVELS = Literal["NONE", "FULL", "FORWARD", "BACKWARD"]
VALID_METHODS = Literal["GET", "POST", "PUT", "DELETE"]
VALID_AUTH_PROVIDERS = Literal["URL", "USER_INFO", "SASL_INHERIT"]
ACCEPT_HDR: str
log: Logger

class CachedSchemaRegistryClient:
    url: str | dict
    subject_to_schema_ids: DefaultDict[str, dict]
    id_to_schema: DefaultDict[str, dict]
    subject_to_schema_versions: DefaultDict[str, dict]
    auto_register_schemas: bool

    def __init__(
        self,
        url: str | dict,
        max_schemas_per_subject: int = 1000,
        ca_location: str | Path | None = None,
        cert_location: str | Path | None = None,
        key_location: str | Path | None = None,
    ) -> None: ...
    def __del__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def close(self) -> None: ...
    def register(self, subject: str, avro_schema: "Schema") -> int: ...
    def check_registration(self, subject: str, avro_schema: "Schema") -> int: ...
    def delete_subject(self, subject: str) -> int: ...
    def get_by_id(self, schema_id: int) -> "Schema": ...
    def get_latest_schema(self, subject: str) -> tuple[str, "Schema", int]: ...
    def get_by_version(self, subject: str, version) -> tuple[str, "Schema", int]: ...
    def get_version(self, subject: str, avro_schema: "Schema") -> int: ...
    def test_compatibility(self, subject: str, avro_schema: "Schema", version: str = "latest") -> bool: ...
    def update_compatibility(self, level: VALID_LEVELS, subject: str | None = None) -> None: ...
    def get_compatibility(self, subject: str | None = None) -> VALID_LEVELS: ...
