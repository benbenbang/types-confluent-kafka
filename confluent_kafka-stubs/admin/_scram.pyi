"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""
from __future__ import annotations

# standard library
from enum import Enum
from typing import Literal

from .. import cimpl as cimpl

class ScramMechanism(Enum):
    UNKNOWN: Literal["cimpl.SCRAM_MECHANISM_UNKNOWN"]
    SCRAM_SHA_256: Literal["cimpl.SCRAM_MECHANISM_SHA_256"]
    SCRAM_SHA_512: Literal["cimpl.SCRAM_MECHANISM_SHA_512"]
    def __lt__(self, other: "ScramMechanism") -> bool: ...

class ScramCredentialInfo:
    def __init__(self, mechanism: "ScramMechanism", iterations: int) -> None: ...

class UserScramCredentialsDescription:
    def __init__(self, user: str, scram_credential_infos: list["ScramCredentialInfo"]) -> None: ...

class UserScramCredentialAlteration:
    def __init__(self, user: str) -> None: ...

class UserScramCredentialUpsertion(UserScramCredentialAlteration):
    def __init__(
        self, user: str, scram_credential_info: "ScramCredentialInfo", password: bytes, salt: bytes | None = None
    ) -> None: ...

class UserScramCredentialDeletion(UserScramCredentialAlteration):
    def __init__(self, user: str, mechanism: "ScramMechanism") -> None: ...
