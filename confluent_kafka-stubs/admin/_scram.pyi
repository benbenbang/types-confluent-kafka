"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
from enum import Enum
from typing import ClassVar

from .. import cimpl as cimpl

class ScramMechanism(Enum):
    UNKNOWN = 0
    SCRAM_SHA_256 = 1
    SCRAM_SHA_512 = 2

    def __lt__(self, other: "ScramMechanism") -> bool: ...

class ScramCredentialInfo:
    mechanism: ScramMechanism
    iterations: int

    def __init__(self, mechanism: ScramMechanism, iterations: int) -> None: ...

class UserScramCredentialsDescription:
    user: ClassVar[str]
    scram_credential_info: ClassVar[ScramCredentialInfo]

    def __init__(self, user: str, scram_credential_infos: list[ScramCredentialInfo]) -> None: ...

class UserScramCredentialAlteration:
    user: str

    def __init__(self, user: str) -> None: ...

class UserScramCredentialUpsertion(UserScramCredentialAlteration):
    user: str
    scram_credential_info: ScramCredentialInfo
    password: bytes
    salt: bytes | None

    def __init__(
        self,
        user: str,
        scram_credential_info: ScramCredentialInfo,
        password: bytes,
        salt: bytes | None = None,
    ) -> None: ...

class UserScramCredentialDeletion(UserScramCredentialAlteration):
    user: str
    mechanism: ScramMechanism

    def __init__(self, user: str, mechanism: ScramMechanism) -> None: ...
