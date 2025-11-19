"""
URL configuration for barmichev project.
"""
from django.conf import settings
from django.conf.urls import (handler404, handler500,  # noqa
                              handler403, handler400)  # noqa
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

from knowledge.views import technical

urlpatterns = [
    path('health/', technical.health_check, name='health_check'),
    path('admin/', admin.site.urls),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    # path('pages/', include(wagtail_urls)),
    path('', include(wagtail_urls)),
    # path('', include('knowledge.urls')),
]

# handler400 = 'knowledge.views.errors.bad_request'  # noqa
# handler404 = 'knowledge.views.errors.page_not_found'  # noqa
# handler403 = 'knowledge.views.errors.permissions_denied'  # noqa
# handler500 = 'knowledge.views.errors.server_error'  # noqa

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
