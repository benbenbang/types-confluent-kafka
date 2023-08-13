"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from ..cimpl import KafkaError as KafkaError

try:
    string_type = basestring  # type: ignore
except NameError:
    string_type = str

class ValidationUtil:
    @staticmethod
    def check_multiple_not_none(obj, vars_to_check) -> None: ...
    @staticmethod
    def check_not_none(obj, param) -> None: ...
    @staticmethod
    def check_multiple_is_string(obj, vars_to_check) -> None: ...
    @staticmethod
    def check_is_string(obj, param) -> None: ...
    @staticmethod
    def check_kafka_errors(errors) -> None: ...
    @staticmethod
    def check_kafka_error(error) -> None: ...
