"""
This type stub file was generated by pyright.
"""

from typing import Any, NamedTuple
from .utils.version import get_version as get_version

VERSION: Any
__version__: str
def setup(set_prefix: bool = ...) -> None:
    ...

class _NamedTupleAnyAttr(NamedTuple):
    def __getattr__(self, item: str) -> Any:
        ...
    
    def __setattr__(self, item: str, value: Any) -> None:
        ...
    


