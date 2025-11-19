"""
Специализированные команды для управления приложением.
"""
import logging

import psycopg2
from django.conf import settings
from django.core.management.base import BaseCommand
from ehandlers.except_handlers.handlers import log_err

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Создание базы данных в postgresql.'

    def add_arguments(self, parser):
        parser.add_argument('db_name',
                            type=str,
                            help='Название БД')
        parser.add_argument('--user',
                            type=str,
                            help='Пользователь',
                            default='postgres')
        parser.add_argument('--password',
                            type=str,
                            help='Пароль')

    def handle(self, *args, **options):
        db_name = options['db_name']
        user_name = options['user']
        password = options['password']

        conn = psycopg2.connect(
            db_name='postgres',
            user=user_name,
            password=password,
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        conn.autocommit = True
        cursor = conn.cursor()

        try:
            cursor.execute(f'CREATE DATABASE IF NOT EXISTS {db_name};')
        except Exception as e:
            log_err(e, log_obj=logger, log_level=logging.WARNING)
        finally:
            cursor.close()
            conn.close()
