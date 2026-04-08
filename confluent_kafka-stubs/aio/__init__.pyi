"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from ._AIOConsumer import AIOConsumer as AIOConsumer
from .producer import AIOProducer as AIOProducer

__all__ = ["AIOConsumer", "AIOProducer"]
