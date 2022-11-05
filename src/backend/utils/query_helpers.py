from functools import wraps
from sqlalchemy.exc import OperationalError


def careful_query(func):
    @wraps(func)
    def _careful_query(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except OperationalError as e:
            return [], f'Failed to query: {e.orig}'
        except Exception as e:
            return [], f'Failed to query: {e}'
    return _careful_query
