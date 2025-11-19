"""
Технические view-функции, позволяющие получить информацию о сайте.
"""
from django.http import JsonResponse


def health_check(request):
    """
    /health check
    """

    response = JsonResponse({'status': 'healthy'})
    return response
