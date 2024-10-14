"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
from pathlib import Path
from typing import TYPE_CHECKING

from ..avro.error import ClientError as ClientError

if TYPE_CHECKING:
    """Helping users who installed avro package can get type hints"""
    try:
        # pypi/conda library
        from avro.schema import Schema  # type: ignore # this cannot be resolved if avro isn't installed
    except ImportError:
        # standard library
        from typing import Any as Schema  # type: ignore

def loads(schema_str: str) -> "Schema": ...
def load(fp: str | Path) -> "Schema": ...
