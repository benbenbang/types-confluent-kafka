# Types Confluent Kafka Documentation

[![PyPI version](https://badge.fury.io/py/types-confluent-kafka.svg)](https://badge.fury.io/py/types-confluent-kafka) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/types-confluent-kafka) [![GitHub issues](https://img.shields.io/github/issues/benbenbang/types-confluent-kafka)](https://github.com/benbenbang/types-confluent-kafka/issues) ![pre-commit enable](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white) [![main](https://github.com/benbenbang/types-confluent-kafka/actions/workflows/main.yml/badge.svg)](https://github.com/benbenbang/types-confluent-kafka/actions/workflows/main.yml) [![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://semver.org/)

Welcome to the `types-confluent-kafka` documentation! This package provides comprehensive type hints for the `confluent-kafka` Python package, enabling better development experience with type checking and auto-completion support.

## What is types-confluent-kafka?

`types-confluent-kafka` is a package that provides type hints for the `confluent-kafka` Python package. It's designed to enhance your development experience by enabling type checking with tools like `mypy` and providing auto-completion support in your LSP (language server).

!!! note "Important Note"
    Confluent **does not** officially endorse this package.

## Key Features

- **Complete Type Coverage**: Comprehensive type hints for all confluent-kafka APIs
- **IDE Support**: Enhanced auto-completion and IntelliSense in your favorite IDE
- **Type Safety**: Catch type-related errors at development time with mypy and other type checkers
- **LSP Integration**: Works seamlessly with Language Server Protocol implementations
- **Regular Updates**: Frequent releases to stay up-to-date with confluent-kafka changes

## Quick Start

Get started with `types-confluent-kafka` in just a few steps:

1. **Install the package**:
   ```bash
   pip install --no-cache-dir types-confluent-kafka
   ```

2. **Import and use with type hints**:
   ```python
   from confluent_kafka import Producer, Consumer

   # Your IDE and type checker now understand the types!
   producer: Producer = Producer({'bootstrap.servers': 'localhost:9092'})
   consumer: Consumer = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'my-group'})
   ```

3. **Enable type checking**:
   ```bash
   mypy your_kafka_application.py
   ```

## Compatibility

For detailed compatibility information with different versions of confluent-kafka, please check the [compatibility table](https://github.com/benbenbang/types-confluent-kafka/blob/main/compatibility.md).

## Versioning

`types-confluent-kafka` follows [Semantic Versioning 2.0.0](https://semver.org/):

- **MAJOR** version for incompatible API changes
- **MINOR** version for adding new features in a backward-compatible manner
- **PATCH** version for backward-compatible bug fixes

We release frequently to provide you with the latest features and improvements. All commits follow [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) standard.

## Next Steps

- [Getting Started](getting_started.md) - Detailed installation and setup guide
- [Working with Typings](work_with_typings.md) - Learn how to effectively use the type hints
- [Contributions & Conventions](contributions_and_conventions.md) - Contribute to the project
- [Troubleshooting](troubleshooting.md) - Common issues and solutions

## License

This project is licensed under the [Apache 2.0 License](https://github.com/benbenbang/types-confluent-kafka/blob/main/LICENSE). You are free to use, modify, and distribute the code according to the terms of this license.
