"""
Уточнения по инженерным решениям для БД.
"""
import logging

import django.db
from django.db.backends.postgresql.base import (DatabaseWrapper as
                                                PostgresqlDatabaseWrapper)
from ehandlers.except_handlers.handlers import log_err
from psycopg2 import InterfaceError

logger = logging.getLogger(__name__)


class DatabaseWrapper(PostgresqlDatabaseWrapper):
    """
    Кастомизация диспетчера postgresql для лечения ``InterfaceError``.
    """

    def create_cursor(self, name=None):
        try:
            return super().create_cursor(name=name)

        except InterfaceError as err:
            log_err(err, log_obj=logger)
            django.db.close_old_connections()
            django.db.connection.connect()
            super().create_cursor(name=name)
