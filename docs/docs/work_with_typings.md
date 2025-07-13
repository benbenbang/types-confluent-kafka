# Working with Typings

This guide covers how to effectively use the type hints provided by `types-confluent-kafka` to write better, more reliable Kafka applications.

## Understanding the Type System

`types-confluent-kafka` provides comprehensive type annotations for all major confluent-kafka classes and functions. This includes:

- **Producer and Consumer classes** with their configuration options
- **Message objects** with proper typing for keys, values, headers, and metadata
- **Error classes** with specific error code types
- **Administrative client** types for cluster management
- **Serialization** interfaces and implementations

## Core Type Patterns

### Producer Types

```python
from confluent_kafka import Producer
from typing import Dict, Any, Optional, Callable

# Producer configuration is typed as a dictionary
producer_config: Dict[str, Any] = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'my-producer',
    'acks': 'all',
    'retries': 3
}

producer: Producer = Producer(producer_config)

# Delivery callback with proper typing
def delivery_callback(err: Optional[Exception], msg: 'Message') -> None:
    if err:
        print(f"Delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Produce with type safety
producer.produce(
    topic='my-topic',
    key='user-123',
    value=b'{"event": "user_login"}',
    on_delivery=delivery_callback
)
```

### Consumer Types

```python
from confluent_kafka import Consumer, Message, KafkaError
from typing import List, Optional

consumer_config: Dict[str, Any] = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-consumer-group',
    'auto.offset.reset': 'earliest'
}

consumer: Consumer = Consumer(consumer_config)

def process_message(msg: Message) -> None:
    """Process a Kafka message with full type safety."""

    # All message methods are properly typed
    topic: str = msg.topic()
    partition: int = msg.partition()
    offset: int = msg.offset()
    timestamp: tuple[int, int] = msg.timestamp()

    # Optional values are properly typed
    key: Optional[bytes] = msg.key()
    value: Optional[bytes] = msg.value()
    headers: Optional[List[tuple[str, bytes]]] = msg.headers()

    # Error handling with proper types
    error: Optional[KafkaError] = msg.error()
    if error:
        print(f"Message error: {error}")
        return

    if value:
        print(f"Processing: {value.decode('utf-8')}")

# Subscribe with proper typing
topics: List[str] = ['topic1', 'topic2']
consumer.subscribe(topics)

# Poll loop with type safety
while True:
    msg: Optional[Message] = consumer.poll(timeout=1.0)
    if msg is not None:
        process_message(msg)
```

### Error Handling Types

```python
from confluent_kafka import KafkaError, KafkaException
from confluent_kafka.error import ConsumeError, ProduceError

def handle_kafka_errors(error: KafkaError) -> None:
    """Handle different types of Kafka errors."""

    # Error codes are properly typed
    error_code: int = error.code()
    error_name: str = error.name()
    error_str: str = str(error)

    # Check for specific error conditions
    if error.code() == KafkaError._PARTITION_EOF:
        print("Reached end of partition")
    elif error.code() == KafkaError._UNKNOWN_TOPIC_OR_PART:
        print("Unknown topic or partition")
    else:
        print(f"Kafka error: {error_name} - {error_str}")

# Exception handling with proper types
try:
    producer.produce('topic', 'message')
except KafkaException as e:
    kafka_error: KafkaError = e.args[0]
    handle_kafka_errors(kafka_error)
```

## Advanced Typing Patterns

### Generic Message Processing

```python
from typing import TypeVar, Generic, Protocol, Callable
from confluent_kafka import Message

# Define a protocol for serializable data
class Serializable(Protocol):
    def serialize(self) -> bytes: ...
    @classmethod
    def deserialize(cls, data: bytes) -> 'Serializable': ...

T = TypeVar('T', bound=Serializable)

class TypedMessageProcessor(Generic[T]):
    """A generic message processor with type safety."""

    def __init__(self, data_class: type[T]):
        self.data_class = data_class

    def process_message(self, msg: Message) -> Optional[T]:
        """Process a message and return typed data."""
        if msg.error():
            return None

        value = msg.value()
        if not value:
            return None

        try:
            return self.data_class.deserialize(value)
        except Exception as e:
            print(f"Deserialization error: {e}")
            return None

# Usage with proper typing
from dataclasses import dataclass
import json

@dataclass
class UserEvent:
    user_id: str
    event_type: str
    timestamp: int

    def serialize(self) -> bytes:
        return json.dumps(self.__dict__).encode()

    @classmethod
    def deserialize(cls, data: bytes) -> 'UserEvent':
        return cls(**json.loads(data.decode()))

processor: TypedMessageProcessor[UserEvent] = TypedMessageProcessor(UserEvent)
```

### Configuration Type Safety

```python
from typing import TypedDict, Literal

# Define typed configuration dictionaries
class ProducerConfig(TypedDict, total=False):
    bootstrap_servers: str
    client_id: str
    acks: Literal['0', '1', 'all']
    retries: int
    batch_size: int
    linger_ms: int
    compression_type: Literal['none', 'gzip', 'snappy', 'lz4', 'zstd']

class ConsumerConfig(TypedDict, total=False):
    bootstrap_servers: str
    group_id: str
    client_id: str
    auto_offset_reset: Literal['earliest', 'latest', 'none']
    enable_auto_commit: bool
    auto_commit_interval_ms: int
    session_timeout_ms: int

# Type-safe configuration
def create_typed_producer(config: ProducerConfig) -> Producer:
    """Create a producer with type-safe configuration."""
    # Convert snake_case to kafka's dot notation
    kafka_config = {
        key.replace('_', '.'): value
        for key, value in config.items()
    }
    return Producer(kafka_config)

# Usage
producer_config: ProducerConfig = {
    'bootstrap_servers': 'localhost:9092',
    'client_id': 'my-producer',
    'acks': 'all',  # Type checker ensures only valid values
    'compression_type': 'gzip'
}

producer = create_typed_producer(producer_config)
```

### Admin Client Types

```python
from confluent_kafka.admin import AdminClient, NewTopic, ConfigResource
from typing import Dict, List

# Admin client with proper typing
admin_config: Dict[str, Any] = {
    'bootstrap.servers': 'localhost:9092'
}

admin: AdminClient = AdminClient(admin_config)

# Topic creation with type safety
def create_topics(topic_names: List[str], num_partitions: int = 1) -> None:
    """Create topics with proper type annotations."""

    new_topics: List[NewTopic] = [
        NewTopic(
            topic=name,
            num_partitions=num_partitions,
            replication_factor=1
        )
        for name in topic_names
    ]

    # Create topics operation returns a dict with futures
    futures = admin.create_topics(new_topics)

    # Wait for operations to complete
    for topic_name, future in futures.items():
        try:
            future.result()  # The result() call blocks until completion
            print(f"Topic {topic_name} created successfully")
        except Exception as e:
            print(f"Failed to create topic {topic_name}: {e}")
```

## Type Checking Best Practices

### Use Type Checkers

Enable strict type checking in your development workflow:

```bash
# mypy configuration in pyproject.toml
[tool.mypy]
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

### Type Annotations in Function Signatures

Always annotate function parameters and return types:

```python
from confluent_kafka import Producer, Consumer, Message
from typing import Optional, List, Dict, Any

def create_producer(
    bootstrap_servers: str,
    client_id: Optional[str] = None,
    **kwargs: Any
) -> Producer:
    """Create a Kafka producer with type-safe parameters."""
    config: Dict[str, Any] = {
        'bootstrap.servers': bootstrap_servers,
        **kwargs
    }
    if client_id:
        config['client.id'] = client_id

    return Producer(config)

def batch_consume(
    consumer: Consumer,
    batch_size: int = 100,
    timeout: float = 1.0
) -> List[Message]:
    """Consume messages in batches with proper typing."""
    messages: List[Message] = []

    for _ in range(batch_size):
        msg: Optional[Message] = consumer.poll(timeout)
        if msg is None:
            break
        messages.append(msg)

    return messages
```

### Handling Optional Values

Many Kafka operations return optional values. Handle them explicitly:

```python
def safe_message_processing(msg: Message) -> Optional[str]:
    """Safely process a message, handling all optional values."""

    # Check for errors first
    if msg.error():
        return None

    # Handle optional value
    value: Optional[bytes] = msg.value()
    if value is None:
        return None

    try:
        return value.decode('utf-8')
    except UnicodeDecodeError:
        return None

def process_with_headers(msg: Message) -> Dict[str, str]:
    """Process message headers safely."""
    result: Dict[str, str] = {}

    headers: Optional[List[tuple[str, bytes]]] = msg.headers()
    if headers:
        for key, value in headers:
            try:
                result[key] = value.decode('utf-8')
            except UnicodeDecodeError:
                result[key] = f"<binary data: {len(value)} bytes>"

    return result
```

## Common Type Patterns

### Callback Functions

```python
from typing import Callable

# Type alias for delivery callback
DeliveryCallback = Callable[[Optional[Exception], Message], None]

def create_logging_callback(logger_name: str) -> DeliveryCallback:
    """Create a delivery callback with proper typing."""
    import logging
    logger = logging.getLogger(logger_name)

    def callback(err: Optional[Exception], msg: Message) -> None:
        if err:
            logger.error(f"Message delivery failed: {err}")
        else:
            logger.info(f"Message delivered to {msg.topic()}[{msg.partition()}]")

    return callback

# Usage
callback: DeliveryCallback = create_logging_callback('kafka.producer')
producer.produce('topic', 'message', on_delivery=callback)
```

This comprehensive typing approach ensures that your Kafka applications are robust, maintainable, and benefit from excellent IDE support and static analysis.
