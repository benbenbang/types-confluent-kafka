"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
from enum import EnumMeta

class ConversionUtil:
    @staticmethod
    def convert_to_enum(val: object, enum_clazz: "EnumMeta") -> "EnumMeta": ...
