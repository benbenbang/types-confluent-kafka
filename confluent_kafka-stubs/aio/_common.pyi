"""
types-confluent-kafka: A package providing type hints for the confluent-kafka Python package.
This package is licensed under the Apache 2.0 License.
"""

from __future__ import annotations

# standard library
import asyncio
import concurrent.futures
import logging
from typing import Any, Callable, Dict, Optional, Tuple, TypeVar

T = TypeVar("T")

class AsyncLogger:
    loop: asyncio.AbstractEventLoop
    logger: logging.Logger
    def __init__(self, loop: asyncio.AbstractEventLoop, logger: logging.Logger) -> None: ...
    def log(self, *args: Any, **kwargs: Any) -> None: ...

def wrap_callback(
    loop: asyncio.AbstractEventLoop,
    callback: Callable[..., Any],
    edit_args: Optional[Callable[[Tuple[Any, ...]], Tuple[Any, ...]]] = None,
    edit_kwargs: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]] = None,
) -> Callable[..., Any]: ...
def wrap_conf_callback(loop: asyncio.AbstractEventLoop, conf: Dict[str, Any], name: str) -> None: ...
def wrap_conf_logger(loop: asyncio.AbstractEventLoop, conf: Dict[str, Any]) -> None: ...
async def async_call(
    executor: concurrent.futures.Executor,
    blocking_task: Callable[..., T],
    *args: Any,
    **kwargs: Any,
) -> T: ...
def wrap_common_callbacks(loop: asyncio.AbstractEventLoop, conf: Dict[str, Any]) -> None: ...
