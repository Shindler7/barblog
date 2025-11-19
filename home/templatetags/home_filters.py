"""
Набор фильтров для шаблонов.
"""
import logging

from django import template

register = template.Library()
logger = logging.getLogger(__name__)


@register.filter
def message_as_css(msg_tag: str) -> str:
    """
    Совместимость тегов для django.message со стилями css приложения. Например,
    в bootstrap нет alert.error, там это alert.danger, а в messages - error.

    :param msg_tag: Тег для проверки и преобразования.
    :returns: Преобразованный тег.
    """

    comparison = {
        'error': 'danger',
    }

    return comparison.get(msg_tag, msg_tag)
