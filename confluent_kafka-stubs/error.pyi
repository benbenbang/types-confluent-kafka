"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

# standard library
from typing import ClassVar

# pypi/conda library
from confluent_kafka.cimpl import KafkaError as KafkaError
from confluent_kafka.cimpl import KafkaException as KafkaException
from confluent_kafka.serialization import SerializationError as SerializationError

from .cimpl import KafkaError as KafkaError
from .cimpl import KafkaException as KafkaException
from .cimpl import Message

class _KafkaClientError(KafkaException):
    """
    Wraps all errors encountered by a Kafka Client

    Args:
        kafka_error (KafkaError): KafkaError instance.

        exception(Exception, optional): The original exception

        kafka_message (Message, optional): The Kafka Message returned
        by the broker.
    """

    exception: ClassVar[KafkaException]
    kafka_message: ClassVar[Message]

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
    """
    Wraps all errors encountered during the deserialization of a Kafka
    Message's key.

    Args:
        exception(Exception, optional): The original exception

        kafka_message (Message, optional): The Kafka Message returned
        by the broker.

    """

    def __init__(
        self,
        exception: Exception | None = None,
        kafka_message: Message | None = None,
    ) -> None: ...

class ValueDeserializationError(ConsumeError, SerializationError):
    """
    Wraps all errors encountered during the deserialization of a Kafka
    Message's value.

    Args:
        exception(Exception, optional): The original exception

        kafka_message (Message, optional): The Kafka Message returned
        by the broker.

    """

    def __init__(
        self,
        exception: Exception | None = None,
        kafka_message: Message | None = None,
    ) -> None: ...

class ProduceError(_KafkaClientError):
    """
    Wraps all errors encountered when Producing messages.

    Args:
        kafka_error (KafkaError): KafkaError instance.

        exception(Exception, optional): The original exception.
    """

    def __init__(
        self,
        kafka_error: KafkaError,
        exception: Exception | None = None,
    ) -> None: ...

class KeySerializationError(ProduceError, SerializationError):
    """
    Wraps all errors encountered during the serialization of a Message key.

    Args:
        exception (Exception): The exception that occurred during serialization.
    """

    def __init__(self, exception: Exception | None = None) -> None: ...

class ValueSerializationError(ProduceError, SerializationError):
    """
    Wraps all errors encountered during the serialization of a Message value.

    Args:
        exception (Exception): The exception that occurred during serialization.
    """

    def __init__(self, exception: Exception | None = None) -> None: ...
