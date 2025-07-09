# types-confluent-kafka

 [![PyPI version](https://badge.fury.io/py/types-confluent-kafka.svg)](https://badge.fury.io/py/types-confluent-kafka) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/types-confluent-kafka) [![GitHub issues](https://img.shields.io/github/issues/benbenbang/types-confluent-kafka)](https://github.com/benbenbang/types-confluent-kafka/issues) ![pre-commit enable](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white) [![main](https://github.com/benbenbang/types-confluent-kafka/actions/workflows/main.yml/badge.svg)](https://github.com/benbenbang/types-confluent-kafka/actions/workflows/main.yml) [![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://semver.org/)

`types-confluent-kafka` is a package that provides type hints for the `confluent-kafka` Python package. It's designed to enhance your development experience by enabling type checking with tools like `mypy` and providing auto-completion support in your LSP (language server).



**Important Note:** Confluent **does not** officially endorse this package.



## Compatibility
please check the [table](https://github.com/benbenbang/types-confluent-kafka/blob/main/compatibility.md)

## Installation

The package can be installed from [PyPI](https://pypi.org/project/types-confluent-kafka/)

```bash
pip install --no-cache-dir types-confluent-kafka
```

alternatively, if you use `uv`, for example,

```bash
uv add --group dev types-confluent-kafka
```


## Semantic versioning

`types-confluent-kafka` follows [Semantic Versioning 2.0.0](https://semver.org/). This means that we use version numbers like `MAJOR.MINOR.PATCH` to indicate changes in the package:

- `MAJOR` version for incompatible API changes,
- `MINOR` version for adding new features in a backward-compatible manner,
- `PATCH` version for backward-compatible bug fixes.

This package will be released as frequently as possible to iterate faster and provide you with the latest features and improvements. Frequent releases also allow us to quickly address and release bug fixes to ensure the stability of the package.

The commit follows [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/), which is the driver of how the versioning works.



## Contribution

Contributions to `types-confluent-kafka` are welcome and encouraged! If you want to contribute, please follow these steps:

1. Fork this repository.
2. Create a new branch for your contribution: `git checkout -b feature/your-feature-name`.
3. Make your changes and ensure that the tests are passing.
4. Open a pull request describing your changes and their purpose.
5. The PR needs to link to an issue.

Please note that this project follows the Contributor Covenant Code of Conduct. By participating, you are expected to uphold this code.



## Development

please check the [development guide](https://github.com/benbenbang/types-confluent-kafka/blob/main/.github/CONTRIBUTING.md)



## License

This project is licensed under the [Apache 2.0 License](https://chat.openai.com/c/LICENSE). You are free to use, modify, and distribute the code according to the terms of this license.
