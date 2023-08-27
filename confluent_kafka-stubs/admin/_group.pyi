"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""
from __future__ import annotations

# standard library
from typing import ClassVar

from .._model import ConsumerGroupState as ConsumerGroupState
from .._model import Node as Node
from .._util import ConversionUtil as ConversionUtil
from ..cimpl import TopicPartition as TopicPartition
from ..error import KafkaException as KafkaException

class ConsumerGroupListing:
    group_id: ClassVar[str]
    is_simple_consumer_group: ClassVar[bool]
    state: ClassVar[ConsumerGroupState]

    def __init__(
        self,
        group_id: str,
        is_simple_consumer_group: bool,
        state: ConsumerGroupState | None = None,
    ) -> None: ...

class ListConsumerGroupsResult:
    valid: ClassVar[list[ConsumerGroupListing]]
    errors: ClassVar[list[KafkaException]]

    def __init__(
        self,
        valid: list["ConsumerGroupListing"] | None = None,
        errors: list[KafkaException] | None = None,
    ) -> None: ...

class MemberAssignment:
    topic_partitions: ClassVar[list[TopicPartition]]

    def __init__(self, topic_partitions: list[TopicPartition] | None = None) -> None: ...

class MemberDescription:
    member_id: ClassVar[str]
    client_id: ClassVar[str]
    host: ClassVar[str]
    assignment: ClassVar[MemberAssignment]
    group_instance_id: ClassVar[str]

    def __init__(
        self,
        member_id: str,
        client_id: str,
        host: str,
        assignment: MemberAssignment,
        group_instance_id: str | None = None,
    ) -> None: ...

class ConsumerGroupDescription:
    group_id: ClassVar[str]
    is_simple_consumer_group: ClassVar[bool]
    members: ClassVar[list[MemberDescription]]
    partition_assignor: ClassVar[str]
    state: ClassVar[ConsumerGroupState]
    coordinator: ClassVar[Node]

    def __init__(
        self,
        group_id: str,
        is_simple_consumer_group: bool,
        members: list[MemberDescription],
        partition_assignor: str,
        state: ConsumerGroupState,
        coordinator: Node,
    ) -> None: ...
