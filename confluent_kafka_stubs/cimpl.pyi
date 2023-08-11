from __future__ import annotations

# standard library
from typing import Any, Dict, Tuple

# Pre-req Types
ConfigDict = Dict[str, Any]
ClusterMetadata = Any
KafkaValue = str | bytes
KeyValueTuple = Tuple[str, KafkaValue]
