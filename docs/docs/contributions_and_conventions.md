# Contributions & Conventions

We welcome contributions to `types-confluent-kafka`! This guide outlines how to contribute effectively and the conventions we follow.

## Getting Started

### Prerequisites

Before contributing, make sure you have:

- Python 3.9 or higher
- Git for version control
- A GitHub account

### Development Setup

1. **Fork and clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/types-confluent-kafka.git
   cd types-confluent-kafka
   ```

2. **Set up the development environment**:
   ```bash
   # Using uv (recommended)
   uv sync --group dev --group lint --group docs

   # Or using pip (install dev dependencies manually)
   pip install --no-cache-dir -e .
   pip install --no-cache-dir confluent-kafka[avro] mypy pyright pre-commit ruff mkdocs mkdocs-material
   ```

3. **Install pre-commit hooks**:
   ```bash
   pre-commit install && pre-commit install --hook-type commit-msg
   ```

4. **Verify the setup**:
   ```bash
   # Run type checking
   mypy confluent_kafka-stubs
   pyright confluent_kafka-stubs

   # Run linting
   ruff check .
   ruff format --check .
   ```

## Contribution Workflow

### 1. Create an Issue First

Before making any changes:

1. Check if an issue already exists for your proposed change
2. If not, create a new issue describing:
   - The problem you're solving
   - Your proposed solution
   - Any breaking changes

### 2. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 3. Make Your Changes

Follow the coding conventions outlined below and ensure your changes:

- Are focused and atomic
- Include appropriate type annotations
- Follow existing patterns in the codebase
- Don't break existing functionality

### 4. Test Your Changes

```bash
# Run type checking
mypy confluent_kafka-stubs
pyright confluent_kafka-stubs

# Run formatting and linting
ruff format .
ruff check .

# Test with actual confluent-kafka if needed
python -c "import confluent_kafka; print('Import successful')"
```

### 5. Commit Your Changes

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```bash
git commit -m "feat: add type hints for AdminClient.describe_configs"
git commit -m "fix: correct return type for Consumer.poll"
git commit -m "docs: update installation instructions"
```

**Commit Types:**
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `test`: Adding missing tests
- `chore`: Changes to the build process or auxiliary tools

### 6. Open a Pull Request

1. Push your branch: `git push origin feature/your-feature-name`
2. Open a PR on GitHub
3. Fill out the PR template completely
4. Link to the related issue
5. Request review from maintainers

## Coding Conventions

### Type Stub Conventions

#### File Organization

```
confluent_kafka-stubs/
   __init__.pyi              # Main module exports
   _version.pyi              # Version information
   admin/
      __init__.pyi         # Admin client types
      _admin.pyi           # Internal admin types
   avro/
      __init__.pyi         # Avro serializer types
      serializer.pyi       # Avro serializer implementation
   error.pyi                # Error classes
   producer.pyi             # Producer types
   consumer.pyi             # Consumer types
   message.pyi              # Message types
```

#### Type Annotation Style

**Class Definitions:**
```python
class Producer:
    def __init__(self, config: Dict[str, Any]) -> None: ...

    def produce(
        self,
        topic: str,
        value: Optional[Union[str, bytes]] = ...,
        key: Optional[Union[str, bytes]] = ...,
        partition: int = ...,
        on_delivery: Optional[Callable[[Optional[KafkaError], Message], None]] = ...,
        timestamp: int = ...,
        headers: Optional[Dict[str, Union[str, bytes]]] = ...,
    ) -> None: ...

    def poll(self, timeout: float = ...) -> int: ...
    def flush(self, timeout: float = ...) -> int: ...
```

**Function Signatures:**
```python
# Use specific types over Any when possible
def good_function(config: Dict[str, Union[str, int, bool]]) -> Producer: ...

# Avoid generic Any unless necessary
def avoid_this(config: Any) -> Any: ...

# Use Union for multiple acceptable types
def flexible_input(
    value: Union[str, bytes, int, None]
) -> Optional[str]: ...
```

**Optional vs Required Parameters:**
```python
# Use ellipsis (...) for parameters with default values
def method(
    required_param: str,
    optional_param: Optional[str] = ...,
    default_value_param: int = ...,
) -> None: ...
```

#### Documentation in Stubs

While stub files don't include implementation, you can add docstrings for complex types:

```python
class ComplexConfig(TypedDict, total=False):
    """Configuration dictionary for Kafka clients.

    This TypedDict defines the structure for configuration
    options passed to Kafka clients.
    """
    bootstrap_servers: str
    client_id: str
    # ... other fields
```

### Code Quality Standards

#### Type Checking

All stub files must pass both mypy and pyright:

```bash
# Must pass without errors
mypy confluent_kafka-stubs
pyright confluent_kafka-stubs
```

#### Formatting

We use Ruff for formatting and linting:

```bash
# Format code
ruff format .

# Check for issues
ruff check .
```

#### Import Organization

Organize imports in this order:

```python
# 1. Standard library imports
from typing import Any, Dict, List, Optional, Union, Callable
from typing_extensions import TypedDict  # For Python < 3.8 compat

# 2. Related third party imports (if any)

# 3. Local application/library specific imports
from . import _error
from ._version import __version__
```

## Testing Conventions

### Type Checking Tests

Create test files to verify type annotations work correctly:

```python
# tests/test_producer_types.py
from confluent_kafka import Producer
from typing import Dict, Any

def test_producer_creation() -> None:
    config: Dict[str, Any] = {'bootstrap.servers': 'localhost:9092'}
    producer: Producer = Producer(config)

    # Test method calls with proper types
    producer.produce('topic', value='message')
    producer.produce('topic', value=b'binary_message', key='key')
```

### Real-world Usage Tests

Test with actual confluent-kafka library when possible:

```python
# tests/test_integration.py
def test_types_with_real_library() -> None:
    """Test that our types work with the actual library."""
    try:
        import confluent_kafka

        # Verify our types match reality
        producer = confluent_kafka.Producer({'bootstrap.servers': 'test'})

        # This should not raise type errors
        producer.produce('topic', 'value')

    except ImportError:
        pytest.skip("confluent-kafka not available")
```

## Documentation Conventions

### Docstring Style

For complex types or configurations, provide clear documentation:

```python
class ConsumerConfig(TypedDict, total=False):
    """Configuration options for Kafka Consumer.

    Args:
        bootstrap_servers: Comma-separated list of broker addresses
        group_id: Consumer group identifier
        auto_offset_reset: What to do when there is no initial offset
        enable_auto_commit: Whether to automatically commit offsets
    """
    bootstrap_servers: str
    group_id: str
    auto_offset_reset: Literal['earliest', 'latest', 'none']
    enable_auto_commit: bool
```

### README Updates

When adding significant features, update relevant documentation:

- Update the main README.md if needed
- Add examples to demonstrate new functionality
- Update compatibility information

## Version Compatibility

### Maintaining Compatibility

- **Backward Compatibility**: New type hints should not break existing code
- **Forward Compatibility**: Consider future confluent-kafka versions
- **Python Compatibility**: Support Python 3.9+ as defined in pyproject.toml

### Version Testing

Test against multiple confluent-kafka versions when possible:

```bash
# Test with minimum supported version
pip install confluent-kafka==2.5.0
python -c "import confluent_kafka"

# Test with latest version
pip install --upgrade confluent-kafka
python -c "import confluent_kafka"
```

## Release Process

### Semantic Versioning

We follow [SemVer](https://semver.org/):

- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality in a backward-compatible manner
- **PATCH**: Backward-compatible bug fixes

### Automated Releases

Releases are automated through semantic-release based on conventional commits:

1. Merge PR to main branch
2. CI validates all checks pass
3. semantic-release analyzes commits and creates release
4. Package is automatically published to PyPI

## Community Guidelines

### Code of Conduct

This project follows the Contributor Covenant Code of Conduct. Be respectful and inclusive in all interactions.

### Getting Help

- **Issues**: Use GitHub issues for bug reports and feature requests
- **Discussions**: Use GitHub Discussions for questions and general discussion
- **Pull Requests**: Use PR reviews for code-specific discussions

### Recognition

Contributors are recognized in:
- Release notes for their contributions
- GitHub contributor graph
- Acknowledgments in major releases

Thank you for contributing to `types-confluent-kafka`! Your efforts help make Kafka development in Python more reliable and enjoyable for everyone.
