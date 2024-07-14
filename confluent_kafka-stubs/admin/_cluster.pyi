"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from .._model import Node
from ._acl import AclOperation

class DescribeClusterResult:
    controller: Node
    nodes: list[Node]
    cluster_id: str | None
    authorized_operations: list[AclOperation] | None
    def __init__(
        self,
        controller: Node,
        nodes: list[Node],
        cluster_id: str | None = None,
        authorized_operations: list[AclOperation] | None = None,
    ): ...
