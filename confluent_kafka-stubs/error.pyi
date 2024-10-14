"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

from .cimpl import KafkaError as KafkaError
from .cimpl import KafkaException as KafkaException
from .cimpl import Message
from .serialization import SerializationError as SerializationError

class _KafkaClientError(KafkaException):
    """
    Wraps all errors encountered by a Kafka Client

    Args:
        kafka_error (KafkaError): KafkaError instance.

        exception(Exception, optional): The original exception

        kafka_message (Message, optional): The Kafka Message returned
        by the broker.
    """

    exception: KafkaException
    kafka_message: Message

    def __init__(
        self,
        kafka_error: KafkaError,
        exception: Exception | None = None,
        kafka_message: Message | None = None,
    ) -> None: ...
    @property
    def code(self): ...
    @property
    def name(self): ...

class ConsumeError(_KafkaClientError):
    """
    Wraps all errors encountered during the consumption of a message.

    Note:
        In the event of a serialization error the original message
        contents may be retrieved from the ``kafka_message`` attribute.

    Args:
        kafka_error (KafkaError): KafkaError instance.

        exception(Exception, optional): The original exception

        kafka_message (Message, optional): The Kafka Message
        returned by the broker.

    """

    def __init__(
        self,
        kafka_error: KafkaError,
        exception: Exception | None = None,
        kafka_message: Message | None = None,
    ) -> None: ...

class KeyDeserializationError(ConsumeError, SerializationError):
    def __init__(self, exception: Exception | None = None, kafka_message: Message | None = None) -> None: ...

class ValueDeserializationError(ConsumeError, SerializationError):
    def __init__(self, exception: Exception | None = None, kafka_message: Message | None = None) -> None: ...

class ProduceError(_KafkaClientError):
    def __init__(
        self,
        kafka_error: KafkaError,
        exception: Exception | None = None,
    ) -> None: ...

class KeySerializationError(ProduceError, SerializationError):
    def __init__(self, exception: Exception | None = None) -> None: ...

class ValueSerializationError(ProduceError, SerializationError):
    def __init__(self, exception: Exception | None = None) -> None: ...
