# Troubleshooting

This guide helps you resolve common issues when using `types-confluent-kafka`.

## Installation Issues

### Package Not Found

**Problem**: `pip install --no-cache-dir types-confluent-kafka` fails with "package not found"

**Solutions**:
```bash
# Ensure you're using the correct package name
pip install --no-cache-dir types-confluent-kafka

# Try with explicit index
pip install --index-url https://pypi.org/simple/ types-confluent-kafka

# Clear pip cache if needed
pip cache purge
pip install --no-cache-dir types-confluent-kafka
```

### Version Conflicts

**Problem**: Dependency conflicts during installation

**Solutions**:
```bash
# Check current confluent-kafka version
pip show confluent-kafka

# Install compatible version
pip install --no-cache-dir "confluent-kafka>=2.5.0"

# Use virtual environment to avoid conflicts
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install --no-cache-dir types-confluent-kafka
```

## Type Checking Issues

### Types Not Recognized

**Problem**: IDE or type checker doesn't recognize the type hints

**Diagnosis**:
```bash
# Check if package is installed
pip show types-confluent-kafka

# Verify Python path
python -c "import sys; print(sys.path)"

# Check if stubs are found
python -c "import confluent_kafka; print(confluent_kafka.__file__)"
```

**Solutions**:

1. **Restart your IDE/Language Server**:
   - VS Code: Reload window (Ctrl/Cmd + Shift + P → "Developer: Reload Window")
   - PyCharm: File → Invalidate Caches and Restart

2. **Check Python interpreter**:
   ```bash
   # Ensure same environment
   which python
   which pip

   # In VS Code, check Python interpreter path
   # Ctrl/Cmd + Shift + P → "Python: Select Interpreter"
   ```

3. **Force reinstall**:
   ```bash
   pip uninstall types-confluent-kafka
   pip install --no-cache-dir types-confluent-kafka
   ```

### Mypy Errors

**Problem**: `mypy` reports errors with confluent-kafka types

**Common Error**: `Module has no attribute`
```bash
# Error example
error: Module "confluent_kafka" has no attribute "Producer"
```

**Solutions**:

1. **Check mypy configuration**:
   ```toml
   # pyproject.toml
   [tool.mypy]
   python_version = "3.9"
   ignore_missing_imports = false
   ```

2. **Explicit type checking**:
   ```python
   # Add at top of file
   from typing import TYPE_CHECKING

   if TYPE_CHECKING:
       from confluent_kafka import Producer, Consumer
   else:
       import confluent_kafka
       Producer = confluent_kafka.Producer
       Consumer = confluent_kafka.Consumer
   ```

3. **Update mypy**:
   ```bash
   pip install --no-cache-dir --upgrade mypy
   ```

### Pyright/Pylance Issues

**Problem**: Pyright/Pylance doesn't find types

**Solutions**:

1. **Check pyrightconfig.json**:
   ```json
   {
     "include": ["src"],
     "stubPath": "./typings",
     "typeCheckingMode": "basic"
   }
   ```

2. **Update Pylance**:
   - VS Code → Extensions → Python → Update

3. **Clear cache**:
   ```bash
   # Clear Pylance cache
   # VS Code: Ctrl/Cmd + Shift + P → "Python: Clear Cache"
   ```

## Runtime Issues

### Import Errors

**Problem**: `ImportError` when importing confluent_kafka

**Error**:
```python
ImportError: No module named 'confluent_kafka'
```

**Solution**:
```bash
# Install the runtime library
pip install --no-cache-dir confluent-kafka

# Or with Avro support
pip install --no-cache-dir "confluent-kafka[avro]"

# Verify installation
python -c "import confluent_kafka; print('Success')"
```

### Version Mismatch

**Problem**: Type hints don't match your confluent-kafka version

**Diagnosis**:
```python
import confluent_kafka
print(f"confluent-kafka version: {confluent_kafka.__version__}")

import types_confluent_kafka  # This will fail, it's just type stubs
# Check pip show instead
```

```bash
pip show confluent-kafka types-confluent-kafka
```

**Solutions**:

1. **Check compatibility table**: See our [compatibility documentation](https://github.com/benbenbang/types-confluent-kafka/blob/main/compatibility.md)

2. **Update to compatible versions**:
   ```bash
   # Update confluent-kafka
   pip install --no-cache-dir --upgrade confluent-kafka

   # Update types
   pip install --no-cache-dir --upgrade types-confluent-kafka
   ```

## IDE-Specific Issues

### VS Code

**Problem**: Auto-completion not working

**Solutions**:
1. **Check Python extension**:
   - Ensure Python extension is installed and enabled
   - Update to latest version

2. **Verify interpreter**:
   - Ctrl/Cmd + Shift + P → "Python: Select Interpreter"
   - Choose the environment where types-confluent-kafka is installed

3. **Enable Pylance**:
   ```json
   // settings.json
   {
     "python.languageServer": "Pylance",
     "python.analysis.typeCheckingMode": "basic"
   }
   ```

### PyCharm

**Problem**: Type hints not showing

**Solutions**:
1. **Check interpreter**: File → Settings → Project → Python Interpreter

2. **Enable type checking**: Settings → Editor → Inspections → Python → Type checker

3. **Rebuild index**: File → Invalidate Caches and Restart

### Vim/Neovim

**Problem**: LSP not recognizing types

**Solutions**:
1. **Check LSP server**: Ensure pyright or pylsp is installed
   ```bash
   # For pyright
   npm install -g pyright

   # For pylsp
   pip install --no-cache-dir python-lsp-server
   ```

2. **LSP configuration**: Verify your LSP is configured to use the correct Python environment

## Performance Issues

### Slow Type Checking

**Problem**: Type checking is very slow

**Solutions**:

1. **Exclude unnecessary files**:
   ```toml
   # pyproject.toml
   [tool.mypy]
   exclude = [
       "build/",
       "dist/",
       ".venv/",
       "tests/",
   ]
   ```

2. **Use incremental checking**:
   ```toml
   [tool.mypy]
   incremental = true
   cache_dir = ".mypy_cache"
   ```

3. **Limit scope**:
   ```bash
   # Check specific files only
   mypy src/my_kafka_app.py
   ```

## Configuration Issues

### Type Checking Configuration

**Problem**: Type checker reports false positives

**Example Configuration**:
```toml
# pyproject.toml
[tool.mypy]
python_version = "3.9"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
ignore_missing_imports = false

# Specific to confluent-kafka
[[tool.mypy.overrides]]
module = "confluent_kafka.*"
ignore_missing_imports = false
```

### Pyright Configuration

```json
{
  "include": ["src"],
  "exclude": ["**/node_modules", "**/__pycache__", "**/.*"],
  "reportMissingImports": "warning",
  "reportMissingTypeStubs": "information",
  "pythonVersion": "3.9",
  "typeCheckingMode": "basic"
}
```

## Common Patterns and Workarounds

### Working with Optional Types

**Problem**: Dealing with Optional return types

```python
from confluent_kafka import Consumer
from typing import Optional

consumer = Consumer({'bootstrap.servers': 'localhost:9092'})

# This might be None
msg: Optional[Message] = consumer.poll(1.0)

# Type-safe handling
if msg is not None:
    # Now mypy knows msg is not None
    if not msg.error():
        value = msg.value()
        if value is not None:
            print(value.decode('utf-8'))
```

### Configuration Typing

**Problem**: Configuration dictionaries are not type-safe

**Solution**: Use TypedDict

```python
from typing import TypedDict, Literal

class ProducerConfig(TypedDict, total=False):
    bootstrap_servers: str
    client_id: str
    acks: Literal['0', '1', 'all']

config: ProducerConfig = {
    'bootstrap_servers': 'localhost:9092',
    'acks': 'all'  # Type-safe: only accepts valid values
}
```

## Getting Help

### Before Asking for Help

1. **Check this troubleshooting guide**
2. **Search existing GitHub issues**: [Issues page](https://github.com/benbenbang/types-confluent-kafka/issues)
3. **Verify versions**: Ensure compatibility between confluent-kafka and types-confluent-kafka
4. **Minimal reproduction**: Create a minimal example that demonstrates the issue

### Reporting Issues

When reporting issues, include:

1. **Environment information**:
   ```bash
   python --version
   pip show confluent-kafka types-confluent-kafka

   # For type checker issues
   mypy --version
   # or
   pyright --version
   ```

2. **Minimal code example**:
   ```python
   from confluent_kafka import Producer

   # Code that demonstrates the issue
   producer = Producer({'bootstrap.servers': 'localhost:9092'})
   ```

3. **Error messages**: Full error output and stack traces

4. **IDE/Editor**: Name and version if relevant

### Community Support

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and general help
- **Stack Overflow**: Tag with `confluent-kafka` and `python-typing`

### When All Else Fails

If you've checked everything in this guide and still have issues, there might be something missing or wrong in this typing package itself! In that case:

1. **Report an Issue**: [Create a GitHub issue](https://github.com/benbenbang/types-confluent-kafka/issues/new) with:
   - Your environment details (Python version, package versions)
   - Minimal code example that reproduces the problem
   - Expected vs actual behavior

2. **Contribute a Fix**: Even better, if you know how to fix it:
   - Fork the repository
   - Create a fix following our [contribution guidelines](contributions_and_conventions.md)
   - Submit a pull request with the solution

Remember: `types-confluent-kafka` only provides type hints. Runtime issues with Kafka operations should be directed to the [confluent-kafka-python](https://github.com/confluentinc/confluent-kafka-python) project.
