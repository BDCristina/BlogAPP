from functools import wraps
from flask import redirect
from injector import inject
from setup.database_config import DataBaseConfig


def setup_required(funct):
    @wraps(funct)
    @inject
    def wrapper(database_config: DataBaseConfig, *args, **kwargs):
        if not database_config.is_configured:
            return redirect('/setup')
        return funct(*args, **kwargs)
    return wrapper

