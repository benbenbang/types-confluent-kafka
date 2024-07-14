"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

class DeletedRecords:
    low_watermark: int
    def __init__(self, low_watermark: int) -> None: ...
