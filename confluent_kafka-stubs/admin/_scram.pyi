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
    UNKNOWN: ClassVar[int]
    SCRAM_SHA_256: ClassVar[int]
    SCRAM_SHA_512: ClassVar[int]

    def __lt__(self, other: "ScramMechanism") -> bool: ...

class ScramCredentialInfo:
    mechanism: ClassVar[ScramMechanism]
    iterations: int

    def __init__(self, mechanism: ScramMechanism, iterations: int) -> None: ...

class UserScramCredentialsDescription:
    user: ClassVar[str]
    scram_credential_info: ClassVar[ScramCredentialInfo]

    def __init__(self, user: str, scram_credential_infos: list[ScramCredentialInfo]) -> None: ...

class UserScramCredentialAlteration:
    user: ClassVar[str]

    def __init__(self, user: str) -> None: ...

class UserScramCredentialUpsertion(UserScramCredentialAlteration):
    user: ClassVar[str]
    scram_credential_info: ClassVar[ScramCredentialInfo]
    password: ClassVar[bytes]
    salt: ClassVar[bytes | None]

    def __init__(
        self,
        user: str,
        scram_credential_info: ScramCredentialInfo,
        password: bytes,
        salt: bytes | None = None,
    ) -> None: ...

class UserScramCredentialDeletion(UserScramCredentialAlteration):
    user: ClassVar[str]
    mechanism: ClassVar[ScramMechanism]

    def __init__(self, user: str, mechanism: ScramMechanism) -> None: ...
