# Getting Started

This guide will help you get up and running with `types-confluent-kafka` in your Python projects.

## Installation

### Using pip

The recommended way to install `types-confluent-kafka` is from [PyPI](https://pypi.org/project/types-confluent-kafka/):

```bash
pip install --no-cache-dir types-confluent-kafka
```

### Using uv

If you're using [uv](https://github.com/astral-sh/uv) as your package manager:

```bash
# Add to development dependencies
uv add --group dev types-confluent-kafka

# Or add to regular dependencies
uv add types-confluent-kafka
```

### Using Poetry

For Poetry users:

```bash
# Add to development dependencies
poetry add --group dev types-confluent-kafka

# Or add to regular dependencies
poetry add types-confluent-kafka
```

## Requirements

- Python 3.9 or higher
- `confluent-kafka` package (the actual runtime library)

## Verifying Installation

After installation, verify everything is working correctly:

```bash
# Check that packages are installed
pip list | grep confluent

# Verify no dependency conflicts
pip check
```

You can also verify that the types are working by creating a simple test file:

```python
# test_types.py
from confluent_kafka import Producer, Consumer, KafkaError

# These should now have proper type hints in your IDE
producer: Producer = Producer({'bootstrap.servers': 'localhost:9092'})
consumer: Consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'test-group',
    'auto.offset.reset': 'earliest'
})

# Type checker should understand the return types
def handle_kafka_error(error: KafkaError) -> None:
    print(f"Kafka error: {error}")
```

## IDE Configuration

### VS Code

If you're using VS Code with the Python extension, type hints should work automatically. Make sure you have:

1. Python extension installed
2. Pylance language server enabled (default)
3. Type checking mode set to "basic" or "strict" in settings

### PyCharm

PyCharm should automatically recognize the type hints. You can enable stricter type checking by:

1. Going to Settings → Editor → Inspections
2. Enabling "Python → Type checker" inspections

### Zed

Zed has built-in Python LSP support that automatically recognizes type hints:

1. Install Zed from [zed.dev](https://zed.dev)
2. Open your Python project
3. The Python LSP is included with Zed - no additional setup needed
4. Type hints should work automatically

### Other IDEs

Most modern Python IDEs with LSP support will automatically pick up the type hints.

## Type Checker Integration

### mypy

Add mypy to your development dependencies and run it on your code:

```bash
pip install --no-cache-dir mypy
mypy your_kafka_code.py
```

### pyright

If you prefer pyright:

```bash
pip install --no-cache-dir pyright
pyright your_kafka_code.py
```

## Basic Usage Example

Here's a simple producer/consumer example with full type safety:

```python
from confluent_kafka import Producer, Consumer, KafkaError, KafkaException
from typing import Optional

def create_producer() -> Producer:
    """Create a Kafka producer with type safety."""
    config = {
        'bootstrap.servers': 'localhost:9092',
        'client.id': 'my-producer'
    }
    return Producer(config)

def create_consumer() -> Consumer:
    """Create a Kafka consumer with type safety."""
    config = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'my-consumer-group',
        'auto.offset.reset': 'earliest'
    }
    return Consumer(config)

def produce_message(producer: Producer, topic: str, message: str) -> None:
    """Produce a message with proper error handling."""
    try:
        producer.produce(topic, value=message.encode('utf-8'))
        producer.flush()
    except KafkaException as e:
        print(f"Failed to produce message: {e}")

def consume_messages(consumer: Consumer, topics: list[str]) -> None:
    """Consume messages with proper type hints."""
    consumer.subscribe(topics)

    try:
        while True:
            msg = consumer.poll(timeout=1.0)

            if msg is None:
                continue

            if msg.error():
                error: KafkaError = msg.error()
                if error.code() == KafkaError._PARTITION_EOF:
                    print("End of partition reached")
                else:
                    print(f"Consumer error: {error}")
            else:
                value: Optional[bytes] = msg.value()
                if value:
                    print(f"Received: {value.decode('utf-8')}")

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

# Usage
if __name__ == "__main__":
    producer = create_producer()
    consumer = create_consumer()

    # Your IDE will provide auto-completion and type checking
    produce_message(producer, "test-topic", "Hello, Kafka!")
    consume_messages(consumer, ["test-topic"])
```

## Next Steps

Now that you have `types-confluent-kafka` installed and working:

- Learn more about [Working with Typings](work_with_typings.md)
- Check out [Troubleshooting](troubleshooting.md) if you encounter any issues
- Consider [contributing](contributions_and_conventions.md) to the project

## Common Issues

### Type hints not showing up

1. Make sure you've installed `types-confluent-kafka` in the same environment as your project
2. Restart your IDE/language server
3. Check that your Python interpreter is correctly configured

### Import errors

If you get import errors, ensure that both `confluent-kafka` and `types-confluent-kafka` are installed:

```bash
pip list | grep confluent
pip check
```

You should see both packages listed and `pip check` should report no dependency conflicts.
