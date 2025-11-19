"""
HTTP-ошибки при обработке страниц.
"""

import logging

from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)


# noinspection PyUnusedLocal
def bad_request(request, exception) -> HttpResponse:
    """
    Ошибка 400
    """

    return render(request, 'errors/400.html', status=400)


# noinspection PyUnusedLocal
def permissions_denied(request, exception) -> HttpResponse:
    """
    Ошибка 403
    """

    return render(request, 'errors/403.html', status=403)


# noinspection PyUnusedLocal
def page_not_found(request, exception) -> HttpResponse:
    """
    Ошибка 404
    """

    return render(request, 'errors/404.html', status=404)


# noinspection PyUnusedLocal
def server_error(request) -> HttpResponse:
    """
    Ошибка 500
    """

    return render(request, 'errors/500.html', status=500)
