"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

from .._model import TopicPartitionInfo
from ..cimpl import Uuid
from ._acl import AclOperation

class TopicDescription:
    name: str
    topic_id: Uuid
    is_internal: bool
    partitions: list[TopicPartitionInfo]
    authorized_operations = list[AclOperation] | None

    def __init__(
        self,
        name: str,
        topic_id: Uuid,
        is_internal: bool,
        partitions: list[TopicPartitionInfo],
        authorized_operations: list[AclOperation] | None,
    ): ...
