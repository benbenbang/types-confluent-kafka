"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

# standard library
from pathlib import Path
from typing import TYPE_CHECKING

# pypi/conda library
from confluent_kafka.avro.error import ClientError as ClientError

if TYPE_CHECKING:
    """Helping users who installed avro package can get type hints"""
    try:
        # pypi/conda library
        from avro.schema import Schema
    except ImportError:
        # standard library
        from typing import Any as Schema

def loads(schema_str: str) -> "Schema":
    """Parse a schema given a schema string"""
    ...

def load(fp: str | Path) -> "Schema":
    """Parse a schema from a file path"""
    ...
