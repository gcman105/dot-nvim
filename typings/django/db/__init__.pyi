"""
This type stub file was generated by pyright.
"""

from typing import Any
from .utils import ConnectionDoesNotExist as ConnectionDoesNotExist, ConnectionHandler as ConnectionHandler, DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS, DJANGO_VERSION_PICKLE_KEY as DJANGO_VERSION_PICKLE_KEY, DataError as DataError, DatabaseError as DatabaseError, Error as Error, IntegrityError as IntegrityError, InterfaceError as InterfaceError, InternalError as InternalError, NotSupportedError as NotSupportedError, OperationalError as OperationalError, ProgrammingError as ProgrammingError
from . import migrations

connections: Any
router: Any
connection: Any
class DefaultConnectionProxy:
    def __getattr__(self, item: str) -> Any:
        ...
    
    def __setattr__(self, name: str, value: Any) -> None:
        ...
    
    def __delattr__(self, name: str) -> None:
        ...
    


def close_old_connections(**kwargs: Any) -> None:
    ...

def reset_queries(**kwargs: Any) -> None:
    ...

